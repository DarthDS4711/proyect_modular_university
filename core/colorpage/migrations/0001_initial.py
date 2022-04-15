# Generated by Django 4.0.3 on 2022-04-15 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColorPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_selected', models.IntegerField(default=3, verbose_name='color')),
            ],
            options={
                'verbose_name': 'ColorPage',
                'verbose_name_plural': 'ColorPage',
                'db_table': 'colorpage',
                'ordering': ['id'],
            },
        ),
    ]