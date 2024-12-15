# Generated by Django 5.1.3 on 2024-12-13 09:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='grid_column_span',
            field=models.IntegerField(choices=[(1, '1'), (2, '2')], default=1, validators=[django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='image',
            name='grid_row_span',
            field=models.IntegerField(choices=[(1, '1'), (2, '2')], default=1, validators=[django.core.validators.MaxValueValidator(2)]),
        ),
    ]