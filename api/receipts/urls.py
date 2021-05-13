from django.urls import path, include
from rest_framework.routers import DefaultRouter
from receipts import views

router = DefaultRouter()
router.register(r'locations', views.MarketLocationViewSet)
router.register(r'accounts', views.PaymentMethodViewSet)
router.register(r'receipts', views.ReceiptViewSet)
router.register(r'grocery-departments', views.GroceryDepartmentViewSet)
router.register(r'grocery-item-brands', views.GroceryItemBrandViewSet)
router.register(r'grocery-items', views.GroceryItemViewSet)
router.register(r'grocery-item-varieties', views.GroceryItemVarietyViewSet)
router.register(r'grocery-item-sizes', views.GroceryItemSizeViewSet)
router.register(r'receipt-line-items', views.ReceiptLineItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.api_root)
]
