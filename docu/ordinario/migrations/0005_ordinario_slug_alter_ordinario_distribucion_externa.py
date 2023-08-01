# Generated by Django 4.2.3 on 2023-08-01 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordinario', '0004_alter_distribucionexterna_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordinario',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ordinario',
            name='distribucion_externa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ordinario.distribucionexterna'),
        ),
    ]