from django.urls import path
from core.status_send.views.delete_status.views import DeleteStatusSendView
from core.status_send.views.list_status.views import ListStatusView
from core.status_send.views.register_status.views import RegisterStatusView

from core.status_send.views.status_send.views import StatusSendView
from core.status_send.views.edit_status.views import UpdateStatusSendView


app_name = "status_send"
urlpatterns = [
    # ruta para consultar el estado del envio de nuestros productos
    path('status/', StatusSendView.as_view(), name='status'),
    # ruta para crear estados de envio de los productos
    path('register/', RegisterStatusView.as_view(), name='register'),
    # ruta para editar los estados de envio de los productos
    path('edit/<pk>/', UpdateStatusSendView.as_view(), name='update'),
    # ruta para eliminar los estado de envio de los productos
    path('drop/<pk>/', DeleteStatusSendView.as_view(), name='delete'),
    # ruta para listar los estados de envio de los productos
    path('list-status/', ListStatusView.as_view(), name='list')
]