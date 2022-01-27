from django.urls import path
from core.store.views.shopCart.views import ShopCartView

from core.store.views.showProduct.views import DetailProductView


app_name = "shop"
urlpatterns = [
    # vista acerca de la vista a detalle del producto para su compra
    path('detail-product/', DetailProductView.as_view(), name='detail_product'),
    # vista relacionada al carrito de compra 
    path('shop-cart/', ShopCartView.as_view(), name='shop_cart')
]