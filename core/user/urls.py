from django.urls import path

from core.user.views.user_edit.views import EditUserView
from core.user.views.user_view.views import ProfileUserView

app_name = 'user'
urlpatterns = [
    # ruta para poder editar el perfil del usuario
    path('edit-profile/', EditUserView.as_view(), name='profile-edit'),
    # ruta para visualizar el perfil del usuario
    path('view-profile/', ProfileUserView.as_view(), name='view_profile')
]