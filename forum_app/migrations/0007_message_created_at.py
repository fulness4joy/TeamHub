# Generated by Django 5.1.3 on 2024-12-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0006_section_tag_section_tag_color_theme_tag_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]