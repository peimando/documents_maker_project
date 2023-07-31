from django.contrib import admin
from .models import (
    Ordinario,
    DistribucionExterna
)

# Register your models here.
admin.site.register(Ordinario)
admin.site.register(DistribucionExterna)
