# Generated by Django 3.1.1 on 2020-11-06 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0007_auto_20201106_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('paciente', 'paciente'), ('manager', 'manager')], default='paciente', max_length=30),
        ),
    ]
