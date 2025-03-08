from django.urls import path,include
from . import views
from . import api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', api_views.ProductViewSet)

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('product_gen',api_views.ProductGenericApiView.as_view(), name='product_gen'),
    path('music-gen',api_views.MusicGenericApiView.as_view(), name='music_gen'),
    #____________
    path('productmixin/', api_views.ProductMixinApiView.as_view(), name='product-list-create'),
    path('productmixin/<int:pk>/', api_views.ProductMixinApiView.as_view(), name='product-mixin-detail'),
    #____________
    path('productgeneric/', api_views.ProductGenericApiView.as_view(), name='product-generic'),
    path('productgeneric/<int:pk>', api_views.ProductDetailApiView.as_view(), name='product-generic'),
    path('viewsets_product/',include(router.urls)),

]
