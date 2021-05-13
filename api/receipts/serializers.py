from rest_framework import serializers
from receipts.models import *


class MarketLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MarketLocation
        fields = '__all__'


class PaymentMethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'


class GroceryDepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroceryDepartment
        fields = '__all__'


class GroceryItemBrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroceryItemBrand
        fields = '__all__'


class GroceryItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroceryItem
        fields = '__all__'


class GroceryItemVarietySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroceryItemVariety
        fields = '__all__'


class GroceryItemSizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroceryItemSize
        fields = '__all__'


class ReceiptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Receipt
        fields = '__all__'


class ReceiptListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Receipt
        fields = ['date', 'time', 'location', 'url']


class ReceiptLineItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReceiptLineItem
        fields = '__all__'
