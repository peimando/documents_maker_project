from django.contrib import messages
from django.shortcuts import reverse
from django.views.generic import UpdateView
from ordinario.models import Ordinario
from website.forms import AddOrdinarioForm


class EditOrdinario(UpdateView):

    template_name = 'website/ordinario/add_edit_ordinario_inline.html'

    model = Ordinario

    form_class = AddOrdinarioForm

    extra_content = {
        'title': 'Editar Ordinario',
        'action': 'edit'
    }

    def get_success_url(self) -> str:

        return reverse(
            'website:list_ordinarios'
        )

    