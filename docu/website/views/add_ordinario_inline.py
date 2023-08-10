from typing import Any, Dict
from django.views.generic import CreateView
from .ordinario_inline import OrdinarioInline
from website.forms import DistribucionExternaFormSet


class AddOrdinarioInline(
    OrdinarioInline, 
    CreateView
):

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        
        context = super(AddOrdinarioInline, self).get_context_data(**kwargs)
        context['named_formsets'] = self.get_named_formsets()

        print('CONTEXT ====> ', context['named_formsets'])

        return context
    
    def get_named_formsets(self):

        if self.request.method == 'GET':

            return {
                'distribuciones_externas': DistribucionExternaFormSet(prefix='distribuciones_externas')  
            }
        
        else:

            return {
                'distribuciones_externas': DistribucionExternaFormSet(self.request.POST or None, prefix='distribuciones_externas')  
            }