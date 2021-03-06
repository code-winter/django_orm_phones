# Generated by Django 4.0.2 on 2022-02-14 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='image',
            field=models.URLField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='phone',
            name='name',
            field=models.CharField(default='Phone', max_length=50),
        ),
        migrations.AddField(
            model_name='phone',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='phone',
            name='release_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default=' '),
        ),
    ]
