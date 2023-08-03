from django.views.generic import DetailView
from ordinario.models import Ordinario


class DetailOrdinario(DetailView):

    template_name = 'website/detail_ordinario.html'

    queryset = Ordinario.objects.all()