from django.views.generic.base import TemplateView


class MainShopView(TemplateView):
	template_name = 'shopMainPage.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Tienda"
		context["image"] = "img/dress.png"
		return context
		
