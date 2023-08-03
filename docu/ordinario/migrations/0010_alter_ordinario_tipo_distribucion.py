# Generated by Django 4.2.3 on 2023-08-02 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordinario', '0009_ordinario_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordinario',
            name='tipo_distribucion',
            field=models.CharField(blank=True, choices=[('INT', 'Interna'), ('EXT', 'Externa')], max_length=3, null=True),
        ),
    ]
