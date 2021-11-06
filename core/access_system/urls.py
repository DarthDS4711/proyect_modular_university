from core.homepage.app_views.views import HomepageView
from django.urls import path
from core.access_system.views import LoginView

app_name = 'access'
urlpatterns = [
    # paths for the mainpage
    path('', LoginView.as_view(), name='Login')
]
