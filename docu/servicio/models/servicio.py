from django.db import models


class Servicio(models.Model):

    nombre = models.CharField(
        max_length=150
    )

    sigla = models.CharField(
        max_length=15
    )
