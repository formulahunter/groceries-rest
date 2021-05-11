from django.db import models


class MarketLocation(models.Model):

    label = models.CharField(max_length=128)
    chain = models.CharField(max_length=128, null=True)

    addr = models.CharField(max_length=128, null=True)
    city_name = models.CharField(max_length=64)
    state_name = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=10, null=True)

    tax_rate = models.DecimalField('tax applied to purchases, in %', max_digits=5, decimal_places=3)

    class Meta:
        ordering = ['chain', 'label']


class PaymentMethod(models.Model):

    name = models.CharField(max_length=64, unique=True)
    card = models.CharField(max_length=4, unique=True, null=True, verbose_name='optional, last 4 digits of card #')

    class Meta:
        ordering = ['name']


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

    class Meta:
        ordering = ['-date', '-time']
