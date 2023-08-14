from django import template
from common.utils.servicios_hls import ServiciosChoices


register = template.Library()

@register.filter
def get_servicio_value(key):
    
    servicios = ServiciosChoices.SERVICIOS_CHOICES

    return dict(servicios)[key]
