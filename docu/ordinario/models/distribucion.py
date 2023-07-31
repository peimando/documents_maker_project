from django.db import models


class DistribucionExterna(models.Model):

    descripcion = models.CharField(max_length=100)

    direccion = models.CharField(max_length=200)
