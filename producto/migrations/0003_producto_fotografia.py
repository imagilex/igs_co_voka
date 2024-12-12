# Generated by Django 5.1.2 on 2024-12-11 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_producto_mostrar_en_galeria'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='fotografia',
            field=models.FileField(default='', help_text='Archivo *.jpg, *.png, etc., correspondiente a la imagen del producto en galería', upload_to='producto/'),
            preserve_default=False,
        ),
    ]
