from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.product.models import Product
from django.http import JsonResponse

from core.user.models import User


class StatePageView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, TemplateView):
    template_name = 'statePage.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def best_ranking_product(self):
        best_ranking = Product.objects.filter(product_rating__gt = 4.0).order_by('product_rating')[0]
        return best_ranking
    
    
    def get_newwest_user(self):
        newest_user = User.objects.all().last()
        return newest_user
    
    def worst_product(self):
        worst_ranking = Product.objects.filter(product_rating__lt = 1.1)[0]
        return worst_ranking

    def get_number_users_newest_session(self):
        date = datetime.now()
        number_in_session = User.objects.filter(last_login__date = date).count()
        return number_in_session

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Estado de la página'
        context['best_product'] = self.best_ranking_product()
        context['newest_user'] = self.get_newwest_user()
        context['worst_product'] = self.worst_product()
        context['users_session'] = self.get_number_users_newest_session()
        context['color'] = self.get_number_color()
        return context
