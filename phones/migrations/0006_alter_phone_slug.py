# Generated by Django 4.0.2 on 2022-02-14 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0005_alter_phone_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default='', max_length=100),
        ),
    ]
