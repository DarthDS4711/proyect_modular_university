from django.urls import path
from core.access_system.views.login.views import LoginView
from core.access_system.views.signin.views import SignInView

app_name = 'access'
urlpatterns = [
    # paths for the loginform
    path('login/', LoginView.as_view(), name='Login'),
    # paths for the signinform
    path('signin/', SignInView.as_view(), name='signin')
]
