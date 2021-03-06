# Generated by Django 3.1.1 on 2020-11-19 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('imagen', models.ImageField(null=True, upload_to='')),
                ('armazon', models.BooleanField()),
                ('distancia', models.CharField(choices=[('Lejos', 'Lejos'), ('Cerca', 'Cerca')], default='Cerca', max_length=30)),
                ('lado', models.CharField(choices=[('Izquierda', 'Izquierda'), ('Derecha', 'Derecha')], default='Derecha', max_length=20)),
                ('precio', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=12)),
                ('obra_social', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('imagen', models.ImageField(null=True, upload_to='')),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('asistencia', models.BooleanField(default=False)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo_pago', models.CharField(choices=[('Tarjeta de crédito', 'Tarjeta de crédito'), ('Tarjeta de débito', 'Tarjeta de débito'), ('Billetera virtual', 'Billetera virtual'), ('Efectivo', 'Efectivo')], default='Efectivo', max_length=30)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Pedido', 'Pedido'), ('Taller', 'Taller'), ('Finalizado', 'Finalizado')], default='Pendiente', max_length=30)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('lentes', models.ManyToManyField(blank=True, to='main.Lente')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.paciente')),
                ('productos', models.ManyToManyField(blank=True, to='main.Producto')),
                ('vendedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialMedico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observaciones', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.paciente')),
            ],
        ),
    ]
