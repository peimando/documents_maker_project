from typing import Any, Dict
from django.views.generic import UpdateView
from .ordinario_inline import OrdinarioInline
from website.forms import DistribucionExternaFormSet


class EditOrdinario(
    OrdinarioInline,
    UpdateView
):

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        
        context = super(EditOrdinario, self ).get_context_data(**kwargs)
        context['named_formsets'] = self.get_named_formsets()

        return context
    
    def get_named_formsets(self):

        return {
            'distribuciones_externas': DistribucionExternaFormSet(
                self.request.POST or None,
                instance=self.object,
                prefix='distribuciones_externas'
            )  
        }