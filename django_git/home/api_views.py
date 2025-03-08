from django.shortcuts import render
from .models import *
from rest_framework.generics import ListCreateAPIView
from .serializers import ProductSerializer, MusicSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.pagination import LimitOffsetPagination


@extend_schema(
    request=ProductSerializer,
    responses={201: ProductSerializer},
    description="شاهکار",
)
class ProductGenericApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination


class MusicGenericApiView(ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
