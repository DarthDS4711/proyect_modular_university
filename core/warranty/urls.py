from django.urls import path
from core.warranty.views.create_warranty.views import CreateWarrantyView
from core.warranty.views.delete_incidence.views import DeleteIncidenceView
from core.warranty.views.delete_warranty.views import DeleteWarrantyView
from core.warranty.views.edit_incidence.views import EditIncidenceView
from core.warranty.views.edit_warranty.views import EditWarrantyView
from core.warranty.views.register_incidence.views import RegisterIncidenceView

from core.warranty.views.view_warranty.views import ShowWarrantyProductView


app_name = "warranty"
urlpatterns = [
    # ruta para visualizar la garantía del producto
    path('show-warranty/', ShowWarrantyProductView.as_view(), name='show-warranty'),
    # ruta para registrar una incidencia 
    path('register-incidence/', RegisterIncidenceView.as_view(), name='register-incidence'),
    # ruta para editar una incidencia 
    path('edit-incidence/', EditIncidenceView.as_view(), name='edit-incidence'),
    # ruta para eliminar una incidencia
    path('drop-incidence/', DeleteIncidenceView.as_view(), name='delete-incidence'),
    # ruta para crear una nueva garantía
    path('create/', CreateWarrantyView.as_view(), name='create'),
    # ruta para editar una garantía 
    path('edit/', EditWarrantyView.as_view(), name='edit'),
    # ruta para eliminar una garantía
    path('delete/', DeleteWarrantyView.as_view(), name='delete')
]