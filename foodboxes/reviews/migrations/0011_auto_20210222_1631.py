# Generated by Django 3.1.6 on 2021-02-22 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_auto_20210222_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 2, 22, 16, 31, 7, 241774)),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='published_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 2, 22, 16, 31, 7, 241793)),
        ),
    ]