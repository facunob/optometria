# Generated by Django 3.1.1 on 2020-10-20 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20201020_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='usuario_activo',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='usuario_administrador',
            new_name='is_staff',
        ),
    ]
