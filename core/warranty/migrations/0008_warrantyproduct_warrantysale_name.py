# Generated by Django 4.0.3 on 2022-04-26 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warranty', '0007_incidence_is_active_warrantypurchase_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarrantyProduct',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='warrantysale',
            name='name',
            field=models.CharField(default='', max_length=80, verbose_name='name'),
        ),
    ]