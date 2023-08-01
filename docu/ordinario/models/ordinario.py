from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils.text import slugify

from common.utils.servicios_hls import ServiciosChoices

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
    
    distribucion_interna = models.CharField(
        null=True,
        blank=True
    )

    distribucion_externa = models.ForeignKey(
        'DistribucionExterna',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    servicio = models.CharField(
        null=True,
        blank=True,
        choices=ServiciosChoices.SERVICIOS_CHOICES,
        default=ServiciosChoices.DIR
    )

    slug = models.SlugField(
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.materia
    
    # def get_absolute_url(self):

    #     return reverse(
    #         'website:create_document', kwargs={"slug": self.slug})


def ordinario_post_save(sender, instance, created, *args, **kwargs):
    if created or instance.slug in [None, ""]:
        instance.slug = slugify(f"{str(instance.id)}-{instance.materia}")

        instance.save()

post_save.connect(ordinario_post_save, sender=Ordinario)