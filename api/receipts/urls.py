from django.urls import path, include
from rest_framework.routers import DefaultRouter
from receipts import views

router = DefaultRouter()
router.register(r'locations', views.MarketLocationViewSet)
router.register(r'accounts', views.PaymentMethodViewSet)
router.register(r'receipts', views.ReceiptViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.api_root)
]
