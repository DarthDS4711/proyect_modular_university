from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.product.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin


class MainShopView(EmergencyModeMixin, LoginRequiredMixin, ObtainColorMixin, TemplateView):
	template_name = 'shopMainPage.html'
	login_url = reverse_lazy('access:Login')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Tienda"
		context["category"] = reverse_lazy('shop:list_category_shop')
		context["discount"] = reverse_lazy('shop:list_discount')
		context["best_products"] = reverse_lazy('shop:list_best_products')
		context["list"] = reverse_lazy('shop:list_all')
		context['best'] = Product.objects.all().order_by('-product_rating')[0:4]
		context['color'] = self.get_number_color()
		return context

		
