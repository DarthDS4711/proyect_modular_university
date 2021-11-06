from core.homepage.app_views.views import HomepageView
from django.urls import path
from core.homepage.app_views.views import HomepageView

app_name = 'app_views'
urlpatterns = [
    # paths for the mainpage
    path('', HomepageView.as_view(), name='homepage')
]
