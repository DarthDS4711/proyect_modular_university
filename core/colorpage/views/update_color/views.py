from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.colorpage.models import ColorPage


class UpdateColorPage(LoginRequiredMixin, ObtainColorMixin, TemplateView):
    template_name = 'updateColorPage.html'
    login_url = reverse_lazy('access:Login')

    # sobrescritura del método post para el guardado de los datos
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            number_color = int(request.POST['color'])
            color = ColorPage.objects.using('color').get(id=1)
            if color is not None:
                color.color_selected = number_color
                color.save(using='color')
            else:
                data['error'] = 'Error al obtener el color de la página'
        except Exception as e:
            data['error'] = str(e)
        # regreso de la respuesta del servidor
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Actualizar color página"
        context['list'] = reverse_lazy('app_views:homepage')
        context['action'] = 'update' 
        context['btn'] = 'Actualizar color'
        context['color'] = self.get_number_color()
        return context