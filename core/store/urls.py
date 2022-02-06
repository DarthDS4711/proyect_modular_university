from django.urls import path
from core.store.views.list_products.views import ListProductsShopView
from core.store.views.shopCart.views import ShopCartView

from core.store.views.showProduct.views import DetailProductView
from core.store.views.shop.views import MainShopView


app_name = "shop"
urlpatterns = [
    # vista acerca de la vista a detalle del producto para su compra
    path('detail-product/', DetailProductView.as_view(), name='detail_product'),
    # vista relacionada al carrito de compra 
    path('shop-cart/', ShopCartView.as_view(), name='shop_cart'),
    # vista relacionada a la página principal de la tienda
    path('', MainShopView.as_view(), name='main-shop'),
    # vista relacionada a mostrar en lista los productos de la tienda
    path('list/', ListProductsShopView.as_view(), name='list_products')
]