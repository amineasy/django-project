from django.shortcuts import render
from .models import *
from rest_framework.generics import ListCreateAPIView

from .serializers import ProductSerializer


class ProductGenericApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

