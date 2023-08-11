from typing import Any, Dict
from django.views.generic import DetailView
from ordinario.models import Ordinario, DistribucionExterna

class DetailOrdinario(DetailView):

    template_name = 'website/ordinario/detail_ordinario.html'

    model = Ordinario

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        context = super().get_context_data(**kwargs)

        context['title'] = 'Detalle Ordinario'

        distribuciones_externas = DistribucionExterna.objects.filter(ordinario_id=self.object).values('descripcion', 'direccion')

        context['distribuciones_externas'] = distribuciones_externas

        return context