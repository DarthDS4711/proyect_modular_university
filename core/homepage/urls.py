from django.urls import path
from core.homepage.views.dashboard_admin.views import DashboardAdminView
from core.homepage.views.dashboard_user.views import DashboardUserView

from core.homepage.views.home.views import HomepageView
app_name = 'app_views'

urlpatterns = [
    # paths for the mainpage
    path('', HomepageView.as_view(), name='homepage'),
    # ruta para el dashboard del usuario
    path('dashboard-user/', DashboardUserView.as_view(), name='dashboard_user'),
    # ruta para el dashboard del administrador
    path('dashboard-admin/', DashboardAdminView.as_view(), name='dashboard_admin')
]
