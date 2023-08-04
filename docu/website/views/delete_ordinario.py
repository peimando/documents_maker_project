from django.views.generic import DeleteView
from django.urls import reverse_lazy
from ordinario.models import Ordinario

class DeleteOrdinario(DeleteView):

    model = Ordinario

    template_name = 'website/ordinario/delete_ordinario.html'

    success_url = reverse_lazy(
        'website:list_ordinarios'
    )

    extra_context = {
        'title': 'Eliminar Ordinario'
    }