from django.urls import path
from core.user.views.edit_direction.views import UpdateUserDirectionView
from core.user.views.list_directions.views import ListDirectionUserView
from core.user.views.register_direction.views import RegisterDirectionUser

from core.user.views.user_edit.views import UpdateUserView
from core.user.views.user_view.views import ProfileUserView

app_name = 'user'
urlpatterns = [
    # ruta para poder editar el perfil del usuario
    path('edit-profile/', UpdateUserView.as_view(), name='profile_edit'),
    # ruta para visualizar el perfil del usuario
    path('view-profile/', ProfileUserView.as_view(), name='view_profile'),
    # ruta para listar las direcciones registradas del usuario
    path('directions/', ListDirectionUserView.as_view(), name='list_directions'),
    # ruta para registrar las direcciones del usuario
    path('register-direction/', RegisterDirectionUser.as_view(), name='register_direction'),
    # ruta para editar una dirección del usuario
    path('edit-direction/<int:pk>', UpdateUserDirectionView.as_view(), name='edit_direction')
]