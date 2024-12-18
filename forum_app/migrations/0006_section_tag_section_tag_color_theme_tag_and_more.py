# Generated by Django 5.1.3 on 2024-12-18 14:07

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0005_alter_message_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='tag',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='section',
            name='tag_color',
            field=colorfield.fields.ColorField(blank=True, default='', image_field=None, max_length=25, samples=None),
        ),
        migrations.AddField(
            model_name='theme',
            name='tag',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='theme',
            name='tag_color',
            field=colorfield.fields.ColorField(blank=True, default='', image_field=None, max_length=25, samples=None),
        ),
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/forum_images/'),
        ),
    ]
