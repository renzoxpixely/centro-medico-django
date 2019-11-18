# Generated by Django 2.2.7 on 2019-11-14 04:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservadehoras', '0004_auto_20191113_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='nsucursal',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='Nombre de sucursal'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='phone',
            field=models.IntegerField(max_length=200, verbose_name='Numero de telefono'),
        ),
    ]
