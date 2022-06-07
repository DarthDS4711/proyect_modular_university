# Generated by Django 4.0.3 on 2022-06-02 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataReplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autoreplication', models.BooleanField(default=True, verbose_name='autoreplicacion')),
            ],
            options={
                'verbose_name': 'DataReplication',
                'verbose_name_plural': 'DataReplicacions',
                'db_table': 'datareplication',
                'ordering': ['id'],
            },
        ),
    ]