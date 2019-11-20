# Generated by Django 2.2.7 on 2019-11-20 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservadehoras', '0012_auto_20191120_1506'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='fnac',
        ),
        migrations.RemoveField(
            model_name='product',
            name='nclient',
        ),
        migrations.RemoveField(
            model_name='product',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rclient',
        ),
    ]
