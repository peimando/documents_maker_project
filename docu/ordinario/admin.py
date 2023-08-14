from django.contrib import admin
from .models import (
    Ordinario,
    DistribucionExterna
)

# Register your models here.
@admin.register(Ordinario)
class OrdinarioAdmin(admin.ModelAdmin):

    ordering = ['-id']

    list_display = ['id', 'materia', 'servicio']


@admin.register(DistribucionExterna)
class DistribucionExternaAdmin(admin.ModelAdmin):

    ordering = ['-id']

    