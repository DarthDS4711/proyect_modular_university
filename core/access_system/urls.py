from django.urls import path
from core.access_system.views.change_password.views import ChangePasswordUseriew
from core.access_system.views.login.views import LoginView
from core.access_system.views.logout.views import *
from core.access_system.views.reset_password.views import ResetPasswordEmailiew
from core.access_system.views.signin.views import SignInView

app_name = 'access'
urlpatterns = [
    # paths for the loginform
    path('login/', LoginView.as_view(), name='Login'),
    # paths for the signinform
    path('signin/', SignInView.as_view(), name='signin'),
    # rutas para cerrar sesión
    path('logout/', LogoutUserView.as_view(), name='logout'),
    # ruta que nos permite enviar un correo al usuario para reestablecer su contraseña
    path('reset-pwd/', ResetPasswordEmailiew.as_view(), name='reset_pwd'),
    # ruta para cambiar la contraseña con el token recibido por correo
    path('change-password/<str:token>/', ChangePasswordUseriew.as_view(), name='change_pwd'),
    # ruta para eliminar todas las sesiones del usuario
    path('logout/all', LogoutAllSessionUserView.as_view(), name='logout_all')
]
