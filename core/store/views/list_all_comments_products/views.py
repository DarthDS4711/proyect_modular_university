from django.urls import reverse_lazy
from django.views.generic.list import ListView
from core.classes.obtain_color import ObtainColorMixin
from core.product.models import Comment, Product
from django.contrib.auth.mixins import LoginRequiredMixin



class ListAllCommentsProduct(LoginRequiredMixin, ObtainColorMixin, ListView):
    model = Comment
    paginate_by = 10
    template_name = 'list_all_comments.html'
    login_url = reverse_lazy('access:Login')
    
    def get_queryset(self):
        product_to_rating = Product.objects.get(id = self.kwargs['id_product'])
        data_set = Comment.objects.filter(product = product_to_rating)
        return data_set
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Comentarios y valoraciones"
        context['color'] = self.get_number_color()
        return context

