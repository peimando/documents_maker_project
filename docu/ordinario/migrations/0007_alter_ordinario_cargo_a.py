# Generated by Django 4.2.3 on 2023-08-10 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordinario', '0006_remove_ordinario_distribuciones_externas_asociadas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordinario',
            name='cargo_a',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
