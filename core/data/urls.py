from django.urls import path

from core.data.views.update_datarepplication.views import UpdateDataRepplicationView


app_name = 'data'
urlpatterns = [
    # ruta para actualizar la autoreplicación de los datos
    path('update/', UpdateDataRepplicationView.as_view(), name='update_rep')
]