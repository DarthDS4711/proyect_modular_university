from django.urls import path
from core.user_admin.views.massive_email.views import MassiveEmailView
from core.user_admin.views.update_active_user.views import UpdateStatusUserView
from core.user_admin.views.active_user.views import ListBlockUserView
from core.user_admin.views.admin_user.views import ListAdminUserView

from core.user_admin.views.superuser.views import ListSuperUserView
from core.user_admin.views.update_admin_user.views import UpdateAdminUserView
from core.user_admin.views.update_superuser.views import UpdateSuperUserView


app_name = 'user_admin'
urlpatterns = [
    # ruta para cambiar al usuario actual por un usperusuario y viceversa
    path('list/super-users/', ListSuperUserView.as_view(), name='list_super_user'),
    # ruta donde haremos la busqueda e inserción del username 
    path('list/super-users/<str:name>', ListSuperUserView.as_view(), name='list_super_user_n'),
    # ruta en la que actualizaremos el estado de superusuario del usuario seleccionado
    path('update-superuser/<pk>', UpdateSuperUserView.as_view(), name='update_superuser'),
    # ruta en la que se mostrará los usuarios que estén activos o dados de baja
    path('list/block-users/', ListBlockUserView.as_view(), name='list_block_user'),
    # ruta secundaria que mostrará los resultados de búsqueda de los usuarios
    path('list/block-users/<str:name>', ListBlockUserView.as_view(), name='list_block_user_n'),
    # ruta primaria que nos lista los usuarios que son o no administradores
    path('list/admin-users/', ListAdminUserView.as_view(), name='list_admin_user'),
    # ruta secundaria que nos lista los usuarios admin buscados
    path('list/admin-users/<str:name>', ListAdminUserView.as_view(), name='list_admin_user_n'),
    # ruta para actualizar el estado actual de los usuarios (activo o no)
    path('update/active-user/<pk>', UpdateStatusUserView.as_view(), name='update_status_user'),
    # ruta para actualizar el grupo de administrador de un usuario
    path('update/admin-user/<pk>', UpdateAdminUserView.as_view(), name='update_admin_user'),
    # ruta para seleccionar el tipo de plantilla además de los usuarios de correo masivo
    path('massive-email/select', MassiveEmailView.as_view(), name='massive_email'),
    # ruta que envia el correo masivo acorde a lo selecionado
    path('massive-email/send/<str:type>', MassiveEmailView.as_view(), name='massive_email_send')
]