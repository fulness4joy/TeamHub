# Generated by Django 5.1.3 on 2024-12-17 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0002_alter_image_grid_column_span_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='media/gallery_images/'),
        ),
    ]