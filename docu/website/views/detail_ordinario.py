from typing import Any, Dict
from django.views.generic import DetailView
from ordinario.models import Ordinario


class DetailOrdinario(DetailView):

    template_name = 'website/ordinario/detail_ordinario.html'

    model = Ordinario

    extra_context = {
          'title':  'Detalle Ordinario'
    }
