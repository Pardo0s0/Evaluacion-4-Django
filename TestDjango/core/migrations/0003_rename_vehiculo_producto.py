# Generated by Django 4.0.5 on 2022-07-02 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_categoria_idcategoria_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vehiculo',
            new_name='Producto',
        ),
    ]
