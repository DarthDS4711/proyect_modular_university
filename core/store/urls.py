from django.urls import path
from core.store.views.add_comment.views import AddComentProduct
from core.store.views.cancel.views import CancelPaymentView
from core.store.views.list_all_comments_products.views import ListAllCommentsProduct
from core.store.views.list_all_products.views import ListAllProductsView
from core.store.views.list_best_ranking_prod.views import ListBestProductsView
from core.store.views.list_categories.views import ListCategoryShopView
from core.store.views.list_discount_prod.views import ListDiscountProductView
from core.store.views.list_products.views import ListProductsShopView
from core.store.views.list_search_prod.views import ListSearchProductView
from core.store.views.shopCart.views import ShopCartView

from core.store.views.showProduct.views import DetailProductView
from core.store.views.shop.views import MainShopView
from core.store.views.success.views import SuccessPaymentView


app_name = "shop"
urlpatterns = [
    # vista acerca de la vista a detalle del producto para su compra
    path('detail-product/<int:pk>', DetailProductView.as_view(), name='detail_product'),
    # vista relacionada al carrito de compra 
    path('shop-cart/', ShopCartView.as_view(), name='shop_cart'),
    # vista relacionada a la página principal de la tienda
    path('', MainShopView.as_view(), name='main_shop'),
    # vista relacionada a mostrar en lista los productos de la tienda
    path('list/<int:id_category>', ListProductsShopView.as_view(), name='list_products'),
    # vista relacionada a mostrar todas las categorías de la tienda (cliente),
    path('list-categories/', ListCategoryShopView.as_view(), name='list_category_shop'),
    # vista para mostrar los productos con descuento
    path('list-discount/', ListDiscountProductView.as_view(), name='list_discount'),
    # vista relacionada a mostrar los productos con mejor valoración
    path('list-bests/', ListBestProductsView.as_view(), name='list_best_products'),
    # vista relacionada a ver todos los productos
    path('list-all/', ListAllProductsView.as_view(), name='list_all'),
    # vista relacionada a desplegar los productos relacionados a la búsqueda
    path('list-search/', ListSearchProductView.as_view(), name='list_search'),
    path('list-search/<str:name>', ListSearchProductView.as_view(), name='list_search_s'),
    # vista relacionada a agregar los comentarios de un producto
    path('add-comment-product/<int:id_product>', AddComentProduct.as_view(), name='add_comment'),
    # vista relacionada a mostrar los comentarios de un producto
    path('view-comments-product/<int:id_product>', ListAllCommentsProduct.as_view(), name='list_comments'),
    # ruta de la vista de cancelación de la compra
    path('cancel/', CancelPaymentView.as_view(), name='cancel'),
    # ruta de pago exitoso
    path('success/', SuccessPaymentView.as_view(), name='success')
]