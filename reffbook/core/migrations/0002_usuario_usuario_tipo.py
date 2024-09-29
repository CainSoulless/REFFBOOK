# Generated by Django 5.0.4 on 2024-09-29 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='usuario_tipo',
            field=models.CharField(choices=[('cliente', 'Cliente'), ('empleado', 'Empleado'), ('administrador', 'Administrador')], default='cliente', max_length=15),
        ),
    ]
