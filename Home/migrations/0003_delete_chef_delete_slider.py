# Generated by Django 4.1.3 on 2024-11-26 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_slider'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Chef',
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
    ]