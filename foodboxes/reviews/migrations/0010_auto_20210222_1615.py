# Generated by Django 3.1.6 on 2021-02-22 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20210222_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='published_at',
            field=models.DateTimeField(),
        ),
    ]
