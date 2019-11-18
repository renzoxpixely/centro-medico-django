# Generated by Django 2.2.7 on 2019-11-18 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservadehoras', '0005_auto_20191113_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Available to borrow'), (2, 'Borrowed by someone'), (3, 'Archived - not available anymore')], default=1),
        ),
        migrations.AlterField(
            model_name='project',
            name='phone',
            field=models.IntegerField(verbose_name='Numero de telefono'),
        ),
    ]
