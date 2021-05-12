from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from receipts.models import MarketLocation, PaymentMethod, Receipt
from receipts.serializers import MarketLocationSerializer, PaymentMethodSerializer, ReceiptSerializer, ReceiptListSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'locations': reverse('locations-list', request=request, format=format),
        'accounts': reverse('accounts-list', request=request, format=format),
        'receipts': reverse('receipts-list', request=request, format=format),
    })


class MarketLocationViewSet(viewsets.ModelViewSet):

    queryset = MarketLocation.objects.all()
    serializer_class = MarketLocationSerializer
    permission_classes = [permissions.IsAuthenticated]


class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return ReceiptListSerializer

        return ReceiptSerializer
