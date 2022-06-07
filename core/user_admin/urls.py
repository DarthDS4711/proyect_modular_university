from django.urls import path

from core.user_admin.views.superuser.views import ListSuperUserView
from core.user_admin.views.update_superuser.views import UpdateSuperUserView


app_name = 'user_admin'
urlpatterns = [
    # ruta para cambiar al usuario actual por un usperusuario y viceversa
    path('list/super-users/', ListSuperUserView.as_view(), name='list_super_user'),
    # ruta donde haremos la busqueda e inserción del username 
    path('list/super-users/<str:name>', ListSuperUserView.as_view(), name='list_super_user_n'),
    # ruta en la que actualizaremos el estado de superusuario del usuario seleccionado
    path('update-superuser/<pk>', UpdateSuperUserView.as_view(), name='update_superuser')
]