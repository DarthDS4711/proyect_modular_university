from multiprocessing import context
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from core.product.models import Size


class ListSizeView(ListView):
    model = Size
    paginate_by = 3
    template_name = 'listSize.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de tamaños disponibles"
        context["create"] = reverse_lazy('product:register_size')
        context["image"] = 'img/list.png'
        return context