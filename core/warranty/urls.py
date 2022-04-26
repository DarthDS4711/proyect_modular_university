from django.urls import path
from core.warranty.views.create_warranty.views import CreateWarrantyView
from core.warranty.views.delete_incidence.views import DeleteIncidenceView
from core.warranty.views.delete_warranty.views import DeleteWarrantyView
from core.warranty.views.edit_incidence.views import EditIncidenceView
from core.warranty.views.edit_warranty.views import EditWarrantyView
from core.warranty.views.list_incidences.views import ListIncidencesView
from core.warranty.views.list_warrantys.views import ListWarrantyView
from core.warranty.views.options_warranty.views import OptionsWarrantyView
from core.warranty.views.register_incidence.views import RegisterIncidenceView

from core.warranty.views.view_warranty.views import ShowWarrantyProductView


app_name = "warranty"
urlpatterns = [
    # ruta para visualizar la garantía del producto
    path('show-warranty/', ShowWarrantyProductView.as_view(), name='show-warranty'),
    # ruta para registrar una incidencia 
    path('register-incidence/', RegisterIncidenceView.as_view(), name='register_incidence'),
    # ruta para editar una incidencia 
    path('edit-incidence/<pk>', EditIncidenceView.as_view(), name='edit-incidence'),
    # ruta para eliminar una incidencia
    path('drop-incidence/', DeleteIncidenceView.as_view(), name='delete-incidence'),
    # ruta para listar todas las incidencias del sistema
    path('list-incidence/', ListIncidencesView.as_view(), name='list_incidences'),
    # ruta para crear una nueva garantía
    path('create/', CreateWarrantyView.as_view(), name='create'),
    # ruta para editar una garantía 
    path('edit/<pk>', EditWarrantyView.as_view(), name='edit'),
    # ruta para eliminar una garantía
    path('delete/', DeleteWarrantyView.as_view(), name='delete'),
    # ruta para mostrar las opciones de las garantías
    path('options-warranty/', OptionsWarrantyView.as_view(), name='options_warranty'),
    # ruta para mostrar el listado de garantías 
    path('list/', ListWarrantyView.as_view(), name='list_warranty')
]