from django.urls import path
from core.supplier.views.delete.views import DeleteSupplierView
from core.supplier.views.edit.views import EditSupplierView

from core.supplier.views.register.views import RegisterSupplierView

app_name = "supplier_app"
urlpatterns = [
    # rutas para registrar a un proveedor
    path('register/', RegisterSupplierView.as_view(), name="register_supplier"),
    # rutas para editar a un proveedor
    path('edit/', EditSupplierView.as_view(), name="register_supplier"),
    # rutas para eliminar a un proveedor
    path('drop/', DeleteSupplierView.as_view(), name="delete_supplier")
]
