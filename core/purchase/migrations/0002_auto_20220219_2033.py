# Generated by Django 3.2.9 on 2022-02-19 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warranty', '0005_auto_20220210_0348'),
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='user',
            new_name='supplier',
        ),
        migrations.AddField(
            model_name='purchase',
            name='warranty_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='warranty.warrantypurchase', verbose_name='warranty_purchase'),
        ),
    ]
