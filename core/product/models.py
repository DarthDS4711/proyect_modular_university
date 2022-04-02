from datetime import datetime
from django.db import models
from django.forms import model_to_dict
from config.settings import MEDIA_URL, STATIC_URL
from core.user.models import User
from django.contrib.postgres import fields
from core.supplier.models import Supplier


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

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        # clase meta que nos porporciona el nombre de la base de datos
        # y como se identifica en el panel de django
        verbose_name = "Categoria"
        verbose_name_plural = 'Categorias'
        ordering = ['id']
        db_table = 'category'

    def __str__(self):
        return self.name


# tabla tamaño del producto (prendas)
class Size(models.Model):
    id = models.BigAutoField(primary_key=True)
    size_product = models.CharField(max_length=80, verbose_name='size_product')

    class Meta:
        verbose_name = "Size"
        verbose_name_plural = 'Sizes'
        ordering = ['id']
        db_table = 'size'
    
    def __str__(self):
        return self.size_product


# tabla productos
class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='name', unique=True)
    # llave foranea que nos indica el color del producto, acorde a los registrados
    primary_color = models.CharField(max_length=8, default='')
    secondary_color = models.CharField(max_length=8, default='')
    last_color = models.CharField(max_length=8, default='')
    # categoria del producto en base a una relación con la tabla categoria
    category = models.ForeignKey(Category, verbose_name='category', on_delete=models.PROTECT)
    # tamanio del producto en caso de que sea una prenda representado en una relacion
    size = models.ManyToManyField(Size, verbose_name='sizes')
    # precio de venta al publico del producto
    pvp = models.DecimalField(verbose_name='pvp', max_digits=9, decimal_places=2)
    # imagen del producto
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='image')
    # descuento del producto
    discount = models.DecimalField(verbose_name='discount', max_digits=3, decimal_places=2)
    # status de producto activo en la base de datos
    is_active = models.BooleanField(verbose_name='is_active', default=True)
    # descripción del producto
    description = models.CharField(max_length=2000, verbose_name='description', default='')
    # valoración total del producto en base a los valoration_user 
    product_rating = models.DecimalField(
        verbose_name='rating', max_digits=3, decimal_places=2, default=0)
    # proveedor relacionado
    supplier_id = models.ForeignKey(Supplier, verbose_name='supplier', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = 'Products'
        ordering = ['id']
        db_table = 'products'
    
    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')
    
    def get_discount_product(self):
        return self.discount * 100
    
    def get_pvp_with_discount(self):
        pvp_d = self.pvp - (self.pvp * self.discount)
        return round(pvp_d, 2)
    
    def __str__(self):
        return self.name
        


# table comments
class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    # relacion uno a uno con el producto a comentar
    product = models.ForeignKey(Product, verbose_name='product_id', on_delete=models.PROTECT)
    # relación uno a uno con el usuario que comenta
    user = models.ForeignKey(User, verbose_name='user_id', on_delete=models.PROTECT)
    # valoración (entero) del producto
    valoration_user = models.IntegerField(default=0, verbose_name='product_raiting')
    # descripción de la valoración
    description = models.CharField(max_length=2000, verbose_name='description', default='')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['id']
        db_table = 'comment'
