from django.db import models


class MarketLocation(models.Model):

    label = models.CharField(max_length=128)
    chain = models.CharField(max_length=128, null=True)

    addr = models.CharField(max_length=128, null=True)
    city_name = models.CharField(max_length=64)
    state_name = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=10, null=True)

    tax_rate = models.DecimalField('tax applied to purchases, in %', max_digits=5, decimal_places=3)

    def __str__(self):
        return self.chain + ': ' + self.label

    class Meta:
        ordering = ['chain', 'label']


class PaymentMethod(models.Model):

    name = models.CharField(max_length=64, unique=True)
    card = models.CharField(max_length=4, unique=True, null=True, verbose_name='optional, last 4 digits of card #')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class GroceryDepartment(models.Model):

    name = models.CharField(max_length=32)
    location = models.ForeignKey(MarketLocation, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['location', 'name']


class GroceryItemBrand(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class GroceryItem(models.Model):
    """
    grocery items represent literal products. they can generally be described
    by manufacturer, variety, size, etc.

    the unit price paid for a grocery item may vary between locations and
    over time, and is considered an aspect of an individual purchase (receipt)
    rather than the product itself (see `ReceiptLineItem`)
    """

    name = models.CharField(max_length=128)
    brand = models.ForeignKey(GroceryItemBrand, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.brand) + ' ' + self.name

    class Meta:
        ordering = ['brand', 'name']


class GroceryItemVariety(models.Model):
    item = models.ForeignKey(GroceryItem, on_delete=models.PROTECT)
    desc = models.CharField(max_length=64, verbose_name='description')

    def __str__(self):
        return self.desc

    class Meta:
        ordering = ['item', 'desc']


class GroceryItemSize(models.Model):
    item = models.ForeignKey(GroceryItem, on_delete=models.PROTECT)
    quantity = models.DecimalField(verbose_name='quantitative measure of size (if applicable)', max_digits=6, decimal_places=3, null=True)
    desc = models.CharField(max_length=32, verbose_name='description of size (taken as unit of measure if quantity is given)')

    def __str__(self):
        if self.quantity != None:
            return str(self.quantity) + self.desc

        return self.desc

    class Meta:
        ordering = ['item', 'desc']


class Receipt(models.Model):
    """
    total balance is required and unambiguous. the other three accounting
    fields are all optional and used mainly for display purposes. the client
    may choose to derive some of these fields when reasonable, but in such
    cases should indicate that the results are not empirically verified.

    no arithmetic validation is performed for any input values.
    """

    date = models.DateField('purchase date')
    time = models.TimeField('purchase time', null=True)

    location = models.ForeignKey(MarketLocation, on_delete=models.PROTECT, verbose_name='market/store location')

    balance = models.DecimalField('total balance due, including tax and discounts', max_digits=6, decimal_places=2)
    subtotal = models.DecimalField('balance due before tsx and discounts', max_digits=6, decimal_places=2, null=True)
    discounts = models.DecimalField('balance deductions for coupons, rewards programs, etc.', max_digits=6, decimal_places=2, null=True)
    tax = models.DecimalField('tax charges incurred', max_digits=6, decimal_places=2, null=True)

    account = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT, verbose_name='payment method')

    def __str__(self):
        return str(self.date) + ' @ ' + str(self.location)

    class Meta:
        ordering = ['-date', '-time']


class ReceiptLineItem(models.Model):

    receipt = models.ForeignKey(Receipt, on_delete=models.PROTECT)
    department = models.ForeignKey(GroceryDepartment, on_delete=models.PROTECT)

    item = models.ForeignKey(GroceryItem, on_delete=models.PROTECT)
    variety = models.ForeignKey(GroceryItemVariety, on_delete=models.PROTECT)
    size = models.ForeignKey(GroceryItemSize, on_delete=models.PROTECT)

    price = models.DecimalField(verbose_name='unit price', max_digits=6, decimal_places=2)
    quantity = models.DecimalField(max_digits=6, decimal_places=3, default=1.0)
    units = models.CharField(max_length=2, verbose_name='unit of measure', default='ct')
    tax_code = models.CharField(max_length=2, verbose_name='character printed next to item name/price, if any')

    def __str__(self):
        return str(self.item) + ' .. ' + str(self.quantity) + self.units + ' @ ' + str(self.price)

    class Meta:
        ordering = ['receipt', 'item']
