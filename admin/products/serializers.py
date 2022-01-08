"""To return the objects in an API
"""
from rest_framework import serializers
from products.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
