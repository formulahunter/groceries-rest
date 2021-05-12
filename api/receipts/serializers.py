from rest_framework import serializers
from receipts.models import MarketLocation, PaymentMethod, Receipt


class MarketLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MarketLocation
        fields = '__all__'


class PaymentMethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'


class ReceiptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Receipt
        fields = '__all__'
