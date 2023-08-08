from django.forms import inlineformset_factory
from ordinario.models import Ordinario, DistribucionExterna
from website.forms import AddDistribucionExterna


OrdinarioFormSet = inlineformset_factory(
    Ordinario,  DistribucionExterna,
    form=AddDistribucionExterna,
    fields=['descripcion', 'direccion']
)