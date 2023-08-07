from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.urls import reverse
from common.utils.servicios_hls import ServiciosChoices


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
    
    distribuciones_internas_asociadas = models.JSONField(
        null=True,
        blank=True
    )

    tiene_distribucion_externa = models.BooleanField(
        null=True,
        blank=True,
        default=False
    )

    distribuciones_externas_asociadas = models.ForeignKey(
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

    telefono = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    slug = models.SlugField(
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.materia
    
    def get_absolute_url(self):

        return reverse(
            'website:detail_ordinario', 
            kwargs={
                'slug': self.slug
            }
        )


def ordinario_post_save(sender, instance, created, *args, **kwargs):
    if created or instance.slug in [None, ""]:
        instance.slug = slugify(f"{str(instance.id)}-{instance.materia}")

        instance.save()

post_save.connect(ordinario_post_save, sender=Ordinario)