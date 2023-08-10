from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ordinario.models import Ordinario
from website.forms import AddOrdinarioForm, DistribucionExternaFormSet


### ORIGINAL

class AddOrdinario(CreateView):

    form_class = AddOrdinarioForm

    template_name = 'website/ordinario/add_edit_ordinario_inline.html'

    def get_context_data(self, **kwargs):
 
        context = super(AddOrdinario, self).get_context_data(**kwargs)
        context['ordinario_distribucion_externa_formset'] = DistribucionExternaFormSet()
        context['title'] = f'Generar Ordinario'
        context['action'] = 'create'
 
        return context

    def post(self, request, *args, **kwargs):

        self.object = None

        form_class = self.get_form_class()

        form = self.get_form()

        ordinario_distribucion_externa_formset = DistribucionExternaFormSet(self.request.POST)

        if form.is_valid() and ordinario_distribucion_externa_formset.is_valid():

            return self.form_valid(form, ordinario_distribucion_externa_formset)
        
        else:
            
            return self.form_invalid(form, ordinario_distribucion_externa_formset)
        
    def form_valid(self, form, ordinario_distribucion_externa_formset):

        self.object = form.save(commit=False)

        # Saving DistribucionesExternas Instance
        distribuciones_externas = ordinario_distribucion_externa_formset.save(commit=False)

        for distribucion_externa in distribuciones_externas:

            distribucion_externa.ordinario = self.object

            distribucion_externa.save(commit=False)

            # 

            distribucion_externa.save()

        self.object.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            f"El ordinario '{self.object.materia}' se ha generado correctamente."
        )

        return super().form_valid(form)

    def form_invalid(self, form, ordinario_distribucion_externa_formset):

        return self.render_to_response(
            self.get_context_data(
                form=form,
                ordinario_distribucion_externa_formset= ordinario_distribucion_externa_formset
            )
        )
    
    def get_success_url(self) -> str:
        
        return reverse_lazy(
            'website:detail_ordinario',
            kwargs={
                'slug': self.object.slug,
            }
        )
