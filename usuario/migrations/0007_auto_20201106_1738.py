# Generated by Django 3.1.1 on 2020-11-06 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0006_usuario_rol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='rol',
        ),
        migrations.DeleteModel(
            name='Roles',
        ),
    ]