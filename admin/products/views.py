from rest_framework import viewsets

from products.models import Products
from products.serializers import ProductSerializer

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

    # def list(self, request):
    #     pass

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def delete(self, request, pk=None):
    #     pass
