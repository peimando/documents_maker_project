from django.db import models
from .distribucion import DistribucionExterna


class Ordinario(models.Model):

    antecendente = models.CharField(
        max_length=100
    )

    materia = models.CharField(
        max_length=100
    )

    de = models.CharField(
        max_length=200
    )

    cargo_de = models.CharField(
        max_length=200
    )

    a = models.CharField(
        max_length=200
    )

    cargo_a = models.CharField(
        max_length=300
    )

    cuerpo = models.TextField()

    adjunto = models.CharField(
        max_length=50
    )

    tipo_distribucion = models.BooleanField(
        default=True,
        choices=[
            ('INT', 'Interna'),
            ('EXT', 'Externa')
        ]
    )
    
    # distribucion_interna = models.

    distribucion_externa = models.ForeignKey(
        to=DistribucionExterna,
        on_delete=models.CASCADE
    )