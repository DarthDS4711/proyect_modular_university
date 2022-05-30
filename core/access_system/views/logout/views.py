from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


class LogoutUserView(LogoutView):
    next_page = reverse_lazy('app_views:homepage')
    template_name = 'index.html'