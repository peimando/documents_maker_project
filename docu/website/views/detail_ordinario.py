from typing import Any, Dict
from django.views.generic import DetailView
from ordinario.models import Ordinario


class DetailOrdinario(DetailView):

    template_name = 'website/ordinario/detail_ordinario.html'

    model = Ordinario

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        
        context = super().get_context_data(**kwargs)

        context['title'] = 'Detalle Ordinario'

        context['object'] = self.object

        # print(type(self.object.distribucion_interna))

        # for obj in self.object.distribucion_interna:
        #     print(type(obj))

        context['distribuciones_internas'] = list(self.object.distribucion_interna)

        return context