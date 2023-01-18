from django.views.generic.base import TemplateView


class Template404View(TemplateView):
    template_name = '404.html'