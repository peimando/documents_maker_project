from django.db import models
from ordinario.models import Ordinario


class DistribucionExterna(models.Model):

    descripcion = models.CharField(max_length=100)

    direccion = models.CharField(max_length=200)

    ordinario = models.ForeignKey(
        'Ordinario',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return f'{self.ordinario.id}-{self.ordinario.materia}: {self.descripcion} - {self.direccion}'