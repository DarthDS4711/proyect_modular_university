from django.urls import path
from core.homepage.views.about.views import AboutPageView
from core.homepage.views.dashboard_admin.views import DashboardAdminView
from core.homepage.views.dashboard_user.views import DashboardUserView
from core.homepage.views.error_page.views import ErrorPageView

from core.homepage.views.home.views import HomepageView
from core.homepage.views.not_found_404.views import Template404View
from core.homepage.views.our_mission.views import OurMissionPageView
from core.homepage.views.state_page.views import StatePageView
from core.homepage.views.support_email.views import SupportEmailView
from core.homepage.views.test_databases.views import StateDatabasesView
from core.homepage.views.user_flow.views import UserPageFlowView
app_name = 'app_views'

urlpatterns = [
    # paths for the mainpage
    path('', HomepageView.as_view(), name='homepage'),
    # ruta para el dashboard del usuario
    path('dashboard-user/', DashboardUserView.as_view(), name='dashboard_user'),
    # ruta para el dashboard del administrador
    path('dashboard-admin/', DashboardAdminView.as_view(), name='dashboard_admin'),
    # ruta para la página de error 404
    path('404/', Template404View.as_view(), name='404_page'),
    # ruta para la pagina de flujo de usuarios
    path('flow-users/', UserPageFlowView.as_view(), name='flow_users'),
    # ruta para obtener el estado de la página
    path('state-page/', StatePageView.as_view(), name='state_page'),
    # ruta para obtener el estado actual de las bases de datos
    path('state-databases/', StateDatabasesView.as_view(), name='state_databases'),
    # ruta para manejar el estado de protección de la página
    path('error/', ErrorPageView.as_view(), name='error_page'),
    # ruta para ver un about del sitio
    path('about', AboutPageView.as_view(), name='about'),
    # ruta para ver las misiones de la compañia
    path('our-mission/', OurMissionPageView.as_view(), name='our_mission'),
    # ruta para mostrar el correo de soporte del sitio
    path('support-team/', SupportEmailView.as_view(), name='support_team')
]
