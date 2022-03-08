from django.urls import path
from core.product.views.delete.views import DeleteProductView, DeleteSizeView
from core.product.views.edit.views import EditProductView, EditSizeView, UpdateCategoryView
from core.product.views.list.views import ListCategoryView, ListSizeView

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
    path('register-category/', RegisterCategoryView.as_view(), name='register_cat'),
    # ruta para editar una categoría
    path('update-category/<pk>', UpdateCategoryView.as_view(), name='edit_category'),
    # ruta para listar categorías
    path('list-categories/', ListCategoryView.as_view(), name='list_cat'),
    # ruta para registrar una nueva talla
    path('register-size/', RegisterSizeView.as_view(), name='register_size'),
    # ruta para listar los tamaños disponibles
    path('list-sizes/', ListSizeView.as_view(), name='list_sizes'),
    # ruta para editar los tamaños disponibles
    path('update-size/<pk>/', EditSizeView.as_view(), name='edit_size'),
    # ruta para eliminar una medida
    path('delete-size/<pk>/', DeleteSizeView.as_view(), name='delete_size'),
]

