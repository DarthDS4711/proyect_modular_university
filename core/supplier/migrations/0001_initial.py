# Generated by Django 3.0.4 on 2021-11-06 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_names', models.CharField(max_length=100, verbose_name='first_names')),
                ('last_names', models.CharField(max_length=110, verbose_name='last_names')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('image', models.ImageField(blank=True, null=True, upload_to='supplier/%Y/%m/%d', verbose_name='image')),
                ('telephone', models.CharField(max_length=50, verbose_name='telephone')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Supplier',
                'db_table': 'supplier',
                'ordering': ['id'],
            },
        ),
    ]
