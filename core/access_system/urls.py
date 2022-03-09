from django.urls import path
from core.access_system.views.login.views import LoginView
from core.access_system.views.signin.views import SigninView

app_name = 'access'
urlpatterns = [
    # paths for the loginform
    path('login/', LoginView.as_view(), name='Login'),
    # paths for the signinform
    path('signin/', SigninView.as_view(), name='signin')
]
