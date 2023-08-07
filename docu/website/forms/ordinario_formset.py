from django.forms import inlineformset_factory
from ordinario.models import Ordinario, DistribucionExterna
from website.forms import AddOrdinarioForm


OrdinarioFormSet = inlineformset_factory(
    Ordinario, DistribucionExterna,
    form=AddOrdinarioForm,
    extra=1,
    can_delete=True,
    can_delete_extra=True
)