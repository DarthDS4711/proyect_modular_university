# Generated by Django 4.0.3 on 2022-05-05 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0003_sale_warranty_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailsale',
            name='color',
            field=models.CharField(default='', max_length=8),
        ),
    ]
