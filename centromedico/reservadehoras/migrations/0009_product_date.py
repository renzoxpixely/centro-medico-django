# Generated by Django 2.2.7 on 2019-11-20 19:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservadehoras', '0008_auto_20191120_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Fecha'),
        ),
    ]
