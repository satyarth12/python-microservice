from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Products, User
from products.serializers import ProductSerializer
from products.producer import publish

import random
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

    # def list(self, request):
    #     pass

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print("IN create")
        publish(method="product_created", body=serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def retrieve(self, request, pk=None):
    #     pass

    def update(self, request, pk=None):
        product = Products.objects.get(id=pk)
        serializer = self.serializer_class(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish(method="product_updated", body=serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk=None):
        product = Products.objects.get(id=pk)
        product.delete()
        publish(method="product_deleted", body=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })
