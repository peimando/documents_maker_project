# Generated by Django 4.2.3 on 2023-08-08 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordinario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordinario',
            name='adjunto',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
