# Generated by Django 4.2.3 on 2023-07-28 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordinario', '0002_rename_ordinariomodel_ordinario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordinario',
            name='adjunto',
            field=models.CharField(max_length=50),
        ),
    ]