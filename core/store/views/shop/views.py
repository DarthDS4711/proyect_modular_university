from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from core.product.models import Product


class MainShopView(TemplateView):
	template_name = 'shopMainPage.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Tienda"
		context["image"] = "img/dress.png"
		context["category"] = reverse_lazy('shop:list_category_shop')
		context["discount"] = reverse_lazy('shop:list_discount')
		context["best_products"] = reverse_lazy('shop:list_best_products')
		context["list"] = reverse_lazy('shop:list_all')
		context['best'] = Product.objects.all()[0:4]
		return context

		
