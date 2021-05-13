from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from receipts.models import *
from receipts.serializers import *


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'locations': reverse('locations-list', request=request, format=format),
        'accounts': reverse('accounts-list', request=request, format=format),
        'receipts': reverse('receipts-list', request=request, format=format),
        'departments': reverse('grocerydepartments-list', request=request, format=format),
        'items': reverse('groceryitems-list', request=request, format=format),
        'varieties': reverse('groceryitemvarietys-list', request=request, format=format),
        'sizes': reverse('groceryitemsizes-list', request=request, format=format),
        'lines': reverse('receiptlineitems-list', request=request, format=format),
    })


class MarketLocationViewSet(viewsets.ModelViewSet):

    queryset = MarketLocation.objects.all()
    serializer_class = MarketLocationSerializer
    permission_classes = [permissions.IsAuthenticated]


class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroceryDepartmentViewSet(viewsets.ModelViewSet):
    queryset = GroceryDepartment.objects.all()
    serializer_class = GroceryDepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroceryItemBrandViewSet(viewsets.ModelViewSet):
    queryset = GroceryItemBrand.objects.all()
    serializer_class = GroceryItemBrandSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroceryItemViewSet(viewsets.ModelViewSet):
    queryset = GroceryItem.objects.all()
    serializer_class = GroceryItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroceryItemVarietyViewSet(viewsets.ModelViewSet):
    queryset = GroceryItemVariety.objects.all()
    serializer_class = GroceryItemVarietySerializer
    permission_classes = [permissions.IsAuthenticated]


class GroceryItemSizeViewSet(viewsets.ModelViewSet):
    queryset = GroceryItemSize.objects.all()
    serializer_class = GroceryItemSizeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return ReceiptListSerializer

        return ReceiptSerializer


class ReceiptLineItemViewSet(viewsets.ModelViewSet):
    queryset = ReceiptLineItem.objects.all()
    serializer_class = ReceiptLineItemSerializer
    permission_classes = [permissions.IsAuthenticated]
