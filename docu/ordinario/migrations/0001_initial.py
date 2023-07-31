# Generated by Django 4.2.3 on 2023-07-28 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DistribucionExterna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=10)),
                ('direccion', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrdinarioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antecendente', models.CharField(max_length=100)),
                ('materia', models.CharField(max_length=100)),
                ('de', models.CharField(max_length=200)),
                ('cargo_de', models.CharField(max_length=200)),
                ('a', models.CharField(max_length=200)),
                ('cargo_a', models.CharField(max_length=300)),
                ('cuerpo', models.TextField()),
                ('adjunto', models.TextField(max_length=50)),
                ('tipo_distribucion', models.BooleanField(choices=[('INT', 'Interna'), ('EXT', 'Externa')], default=True)),
                ('distribucion_externa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordinario.distribucionexterna')),
            ],
        ),
    ]
