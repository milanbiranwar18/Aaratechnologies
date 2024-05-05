from django.urls import path
from shop.views import ShopList, ShopDetail

urlpatterns = [
    path('create_get_shops/', ShopList.as_view(), name='shop-list'),
    path('get_shops/', ShopDetail.as_view(), name='shop-detail'),
    path('shops/<int:pk>/', ShopDetail.as_view(), name='shop-detail'),
]
