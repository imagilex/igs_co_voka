# Generated by Django 5.1.2 on 2025-04-29 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalizacion_producto', '0004_alter_personalizaciondetalle_valor'),
        ('producto', '0009_alter_campoparteproducto_opciones_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalizaciondetalle',
            name='campo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='personalizaciones', to='producto.campoparteproducto'),
        ),
    ]
