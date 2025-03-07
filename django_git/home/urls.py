from django.urls import path
from . import views
from . import api_views


app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('product_gen',api_views.ProductGenericApiView.as_view(), name='product_gen'),
]
