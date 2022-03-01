from django.urls import path
from core.product.views.delete.views import DeleteProductView
from core.product.views.edit.views import EditProductView

from core.product.views.register.views import RegisterCategoryView, RegisterProductView, RegisterSizeView


app_name = "product"
urlpatterns = [
    # rutas para agregar un nuevo producto
    path('register/', RegisterProductView.as_view(), name="register_product"),
    # rutas para editar a un producto existente
    path('edit/', EditProductView.as_view(), name="edit_product"),
    # rutas para eliminar un producto existente
    path('drop/', DeleteProductView.as_view(), name='delete_product'),
    # rutas para registrar una categoría
    path('register-category/', RegisterCategoryView.as_view(), name='register_product'),
    # ruta para registrar una nueva talla
    path('register-size/', RegisterSizeView.as_view(), name='register_size')
]

