# Generated by Django 3.1.6 on 2021-02-28 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_auto_20210227_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='status',
            field=models.CharField(max_length=10),
        ),
    ]
