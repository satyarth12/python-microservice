from django.urls import path, include
from rest_framework import routers
from products.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet,
                basename='products')


urlpatterns = [

    path('', include(router.urls)),
]
