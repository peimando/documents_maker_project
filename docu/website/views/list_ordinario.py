from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from ordinario.models import Ordinario

class ListOrdinarios(ListView):

    template_name = 'website/ordinario/list_ordinario.html'
    
    extra_context = {
        'title': 'Lista de Ordinarios'
    }
    
    queryset = Ordinario.objects.all().order_by('-id')

    paginate_by = 10