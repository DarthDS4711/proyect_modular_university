from django.urls import path

from core.colorpage.views.update_color.views import UpdateColorPage

app_name = 'color'
urlpatterns = [
    path('update-color/', UpdateColorPage.as_view(), name='update_page')
]