from datetime import datetime
from django.db import models
from django.forms import model_to_dict
from core.user.models import User

# tabla categoria
class Category(models.Model):
    # identificador modificado con un campo más grande de datos
    id = models.BigAutoField(primary_key=True)
    # nombre de la categoria
    name = models.CharField(max_length=80, verbose_name='name', unique=True)
    # imagen de la categoria
    image = models.ImageField(
        upload_to='category/%Y/%m/%d', null=True, blank=True, verbose_name='image')
    #  texto descriptivo de la categoria
    description = models.CharField(max_length=150, verbose_name='description')
    # status de la categoria
    is_active = models.BooleanField(verbose_name='is_active', default=True)

    class Meta:
        # clase meta que nos porporciona el nombre de la base de datos
        # y como se identifica en el panel de django
        verbose_name = "Categoria"
        verbose_name_plural = 'Categorias'
        ordering = ['id']
        db_table = 'category'


# tabla tamaño del producto (prendas)
class Size(models.Model):
    id = models.BigAutoField(primary_key=True)
    size_product = models.CharField(max_length=50, verbose_name='size_product')

    class Meta:
         verbose_name = "Size"
         verbose_name_plural = 'Sizes'
         ordering = ['id']
         db_table = 'size'

# tabla Color
class Color(models.Model):
    id = models.BigAutoField(primary_key=True)
    color_name = models.CharField(max_length=150, verbose_name='color_name')


    class Meta:
         verbose_name = "Color"
         verbose_name_plural = 'Colors'
         ordering = ['id']
         db_table = 'color'


# tabla productos
class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='name', unique=True)
    # llave foranea que nos indica el color del producto, acorde a los registrados
    color = models.ForeignKey(Color, verbose_name="color", on_delete=models.PROTECT)
    # categoria del producto en base a una relación con la tabla categoria
    category = models.ForeignKey(Category, verbose_name='category', on_delete=models.PROTECT)
    # tamanio del producto en caso de que sea una prenda representado en una relacion
    size = models.ForeignKey(Size, verbose_name='size', on_delete=models.PROTECT)
    # altura del producto
    heigth = models.DecimalField(verbose_name='heigth', max_digits=8, decimal_places=3)
    # largo del producto
    length = models.DecimalField(verbose_name='length', max_digits=8, decimal_places=3)
    # precio de venta al publico del producto
    pvp = models.DecimalField(verbose_name='pvp', max_digits=9, decimal_places=2)
    # imagen del producto
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='image')
    # descuento del producto 
    discount = models.DecimalField(verbose_name='discount', max_digits=3, decimal_places=2)
    # status de producto activo en la base de datos
    is_active = models.BooleanField(verbose_name='is_active', default=True)


    class Meta:
         verbose_name = "Product"
         verbose_name_plural = 'Products'
         ordering = ['id']
         db_table = 'products'

# table comments
class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, verbose_name='product_id', on_delete=models.PROTECT)
    user = models.ForeignKey(User, verbose_name='user_id', on_delete=models.PROTECT)
    product_raiting = models.IntegerField(default=0, verbose_name='product_raiting')


    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['id']
        db_table = 'comment'
