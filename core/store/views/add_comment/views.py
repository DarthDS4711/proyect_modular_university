from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.app_functions.rollback_data import rollback_data
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.product.models import Comment, Product
from core.store.forms.form_comment.forms import CommentUserForm
from django.db.models import Avg
from django.db import transaction


class AddComentProduct(EmergencyModeMixin, LoginRequiredMixin, ObtainColorMixin, CreateView):
    template_name = 'add_comment.html'
    login_url = reverse_lazy('access:Login')
    model = Comment
    success_url = ''

    def __return_avg_valoration_of_product(self, product_evaluate):
        valoration = Comment.objects.filter(product = product_evaluate).aggregate(Avg('valoration_user'))
        return valoration['valoration_user__avg']


    # función que nos guarda el comentario en las bases de datos
    def save_comment_user(self, request):
        data = {}
        try:
            status_replication = is_actual_state_autoreplication()
             # obtención de los datos de nuestro comentario
            product_rating_user = int(request.POST['stars'])
            description_comment = request.POST['description']
            user_comment = self.request.user
            comment_product = Comment()
            # agregando la infoermación al modelo
            comment_product.product = Product.objects.get(id = self.kwargs['id_product'])
            comment_product.user = user_comment
            comment_product.description = description_comment
            comment_product.valoration_user = product_rating_user
            comment_product.save()
            if status_replication:
                comment_product.save(using='mirror_database')
            # sección de actualización de la valoración del producto
            product = Product.objects.get(id = self.kwargs['id_product'])
            product.product_rating = self.__return_avg_valoration_of_product(product_evaluate = product)
            product.save()
            if status_replication:
                product.save(using='mirror_database')
        except Exception as e:
            data['error'] = str(e)
        return data


    def post(self, request, *args, **kwargs):
        data = {}
        with transaction.atomic():
            data = self.save_comment_user(request)
            if 'error' in data:
                rollback_data(3)
        return JsonResponse(data, safe=False)


    def get_form(self):
        return super().get_form(CommentUserForm)
    
    def get_context_data(self, **kwargs):
        self.success_url = f"../detail-product/{self.kwargs['id_product']}"
        context = super().get_context_data(**kwargs)
        context["title"] = "Agregar comentario"
        context['action'] = 'register' 
        context['btn'] = 'Valorar producto'
        context['color'] = self.get_number_color()
        context['id_product'] = self.kwargs['id_product']
        return context