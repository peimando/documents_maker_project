from django.contrib import messages
from django.views.generic import UpdateView
from ordinario.models import Ordinario
from website.forms import AddOrdinarioForm

class EditOrdinario(UpdateView):

    template_name = 'website/add_ordinario.html'

    model = Ordinario

    form_class = AddOrdinarioForm

    extra_content = {
        'action': 'edit'
    }

    def get_success_url(self) -> str:
        
        messages.success