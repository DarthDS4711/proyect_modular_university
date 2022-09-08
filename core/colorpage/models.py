from django.db import models

# modelo que obtiene el color de nuestra página web(bordes, botones)
class ColorPage(models.Model):
    color_selected = models.IntegerField(default=3, verbose_name='Color pagina')


    class Meta:
        verbose_name = 'ColorPage'
        verbose_name_plural = 'ColorPage'
        ordering = ['id']
        # nombre de la tabla en la base de datos
        db_table = 'colorpage'
