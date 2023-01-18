from django.urls import path
from core.stock.views.create_stock.views import CreateStockView
from core.stock.views.delete_stock.views import DeleteStockView

from core.stock.views.detail_stock.views import DetailStockProduct
from core.stock.views.edit_stock.views import UpdateStockView
from core.stock.views.listStock.views import ListStockView


app_name = 'stock'

urlpatterns = [
    # ruta para el detalle del stock de un producto
    path('detail/<pk>', DetailStockProduct.as_view(), name='detail_stock'),
    # ruta para listar los stock de la tienda
    path('list/', ListStockView.as_view(), name='list_stock'),
    path('list/<str:name>', ListStockView.as_view(), name='list_stock_search'),
    # ruta para crear nuevos stock
    path('create/', CreateStockView.as_view(), name='create_stock'),
    # ruta para editar un stock
    path('edit/<pk>', UpdateStockView.as_view(), name='edit_stock'),
    # ruta para eliminar un stock
    path('delete/<pk>', DeleteStockView.as_view(), name='delete_stock')
]