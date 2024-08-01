from product.views import ProductViewSet

from django.urls import path, include
from rest_framework import routers

app_name = 'product'

router = routers.DefaultRouter()

router.register('products', ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
