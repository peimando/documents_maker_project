# Generated by Django 4.2.3 on 2023-08-09 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordinario', '0002_alter_ordinario_adjunto'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordinario',
            name='distribuciones_externas_asociadas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='distribuciones_externas', to='ordinario.distribucionexterna'),
        ),
    ]