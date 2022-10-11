from django.urls import path
from core.status_send.views.create_status_send_sale.views import RegisterStatusSendSaleView
from core.status_send.views.edit_status_sale.views import UpdateStatusSendSaleView
from core.status_send.views.list_status_send_for_user.views import ListStatusUserSendView
from core.status_send.views.list_status_send_user.views import ListStatusUserAdminSendView
from core.status_send.views.delete_status.views import DeleteStatusSendView
from core.status_send.views.list_status.views import ListStatusView
from core.status_send.views.options_status.views import OptionsStatusSendView
from core.status_send.views.register_status.views import RegisterStatusView
from core.status_send.views.render_pdf_send.views import RenderDetailInvoiceSendView

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
    path('list-status/', ListStatusView.as_view(), name='list'),
    # ruta para listar los estados de envio (administradores)
    path('list-status-send-admin/', ListStatusUserAdminSendView.as_view(), name='list_status_send_admin'),
    # ruta relacionada a las opciones de administrador relacionada a los estados de envio
    path('options/', OptionsStatusSendView.as_view(), name='options'),
    # ruta para registar un nuevo estado de envio a los usuarios
    path('add-status-send-user/', RegisterStatusSendSaleView.as_view(), name='add_status_send_user'),
    # ruta para editar un estado de envio para un usuario
    path('update-status-send-user/<pk>', UpdateStatusSendSaleView.as_view(), name='update_status_send_user'),
    # ruta para listar todos los estados de envio relacionados con el usuario
    path('list-status-send-user/', ListStatusUserSendView.as_view(), name='list_status_send_user'),
    # ruta para renderizar un pdf de una factura
    path('render-pdf-send/<pk>', RenderDetailInvoiceSendView.as_view(), name='render_pdf_send')
]