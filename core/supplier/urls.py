from os import name
from django.urls import path
from core.supplier.views.delete.views import DeleteSupplierView
from core.supplier.views.detail.views import DetailSupplierView
from core.supplier.views.edit.views import EditSupplierView
from core.supplier.views.list.views import ListAllProductSupplierView, ListSupplierView

from core.supplier.views.register.views import RegisterSupplierView

app_name = "supplier_app"
urlpatterns = [
    # ruta para registrar a un proveedor
    path('register/', RegisterSupplierView.as_view(), name="register_supplier"),
    # ruta para editar a un proveedor
    path('edit/<pk>', EditSupplierView.as_view(), name="edit_supplier"),
    # ruta para eliminar a un proveedor
    path('drop/<pk>', DeleteSupplierView.as_view(), name="delete_supplier"),
    # ruta para listar a los proveedor 
    path('list/', ListSupplierView.as_view(), name='list_supplier'),
    # ruta para visualizar a nuestro proveedor
    path('details/<pk>', DetailSupplierView.as_view(), name='detail_supplier'),
    # ruta para visualizar los productos de nuestro proveedor
    path('list-product/<int:id_supplier>', ListAllProductSupplierView.as_view(), name='list_products')
]
