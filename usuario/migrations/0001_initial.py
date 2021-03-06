# Generated by Django 3.1.1 on 2020-10-18 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='nombre de usuario')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='correo electronico')),
                ('nombres', models.CharField(blank=True, max_length=150, verbose_name='nombres')),
                ('apellidos', models.CharField(blank=True, max_length=150, null=True, verbose_name='apellidos')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='perfil/', verbose_name='imagen del perfil')),
                ('usuario_activo', models.BooleanField(default=True)),
                ('usuario_aadministrador', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
