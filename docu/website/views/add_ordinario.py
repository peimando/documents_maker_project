from datetime import datetime
from typing import Any, Dict
from django.contrib import messages
from django.views.generic import View, FormView, CreateView
from django.urls import reverse_lazy

from website.forms import AddOrdinarioForm
from ordinario.models import Ordinario


class AddOrdinario(CreateView):

    models = Ordinario

    form_class = AddOrdinarioForm

    template_name = 'website/ordinario/add_edit_ordinario.html'

    extra_context = {
        'title': 'Generar Ordinario',
        'action': 'create'
    }
   
    def form_valid(self, form):
        
        self.object = form.save(commit=False)

        antecendente = form.cleaned_data['antecendente']
        materia = form.cleaned_data['materia']
        de = form.cleaned_data['de']
        cargo_de = form.cleaned_data['cargo_de']
        a = form.cleaned_data['a']
        cargo_a = form.cleaned_data['cargo_a']
        cuerpo = form.cleaned_data['cuerpo']
        adjunto = form.cleaned_data['adjunto']
        tipo_distribucion = form.cleaned_data['tipo_distribucion']
        distribucion_interna = form.cleaned_data['distribucion_interna']
        distribucion_externa = form.cleaned_data['distribucion_externa']
        # direccion_distribucion_externa = form.cleaned_data['direccion_distribucion_externa']
        servicio = form.cleaned_data['servicio']
        servicio = dict(form.fields['servicio'].choices)[servicio]
        telefono = form.cleaned_data['telefono']

        selected_choices = distribucion_interna
        choices = dict(form.fields['distribucion_interna'].choices)

        selected_choices_values = [choices[selected_key] for selected_key in choices.keys() if selected_key in selected_choices]

        self.form_data = {
            'antecendente': antecendente,
            'materia': materia,
            'de': de,
            'cargo_de': cargo_de,
            'a': a,
            'cargo_a': cargo_a,
            'cuerpo': cuerpo,
            'adjunto': adjunto,
            'tipo_distribucion': tipo_distribucion,
            'distribucion_interna': selected_choices_values,
            'distribucion_externa': distribucion_externa,
            # 'direccion_distribucion_externa': direccion_distribucion_externa,
            'servicio': servicio,
            'telefono': str(telefono)
        }

        self.object = form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            f"El ordinario '{self.object.materia}'\
                se ha generado correctamente."
        )

        return super().form_valid(form)

    def get_success_url(self) -> str:
        
        return reverse_lazy(
            'website:detail_ordinario',
            kwargs={
                'slug': self.slug,
            }
        )

# class OrdinarioInline():

#     form_class = AddOrdinarioForm

#     model = Ordinario

#     template_name = 'website/add_ordinario.html'

#     def form_valid(self, form):

#         named_formsets = self.get_named_formsets()

#         if not all((f.is_valid() for f in named_formsets.values())):

#             return self.render_to_response(self.get_context_data(form=form))

#         self.object = form.save()

#         # for every formset, attempt to find a specific formset save function
#         # otherwise, just save.
#         for name, formset in named_formsets.items():

#             formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            
#             if formset_save_func is not None:
            
#                 formset_save_func(formset)
            
#             else:
            
#                 formset.save()
        
#         return redirect('website:home')

#     def formset_ordinario_valid(self, formset):

#         """
#         Hook for custom formset saving.Useful if you have multiple formsets
#         """
#         variants = formset.save(commit=False)  # self.save_formset(formset, contact)
#         # add this 2 lines, if you have can_delete=True parameter 
#         # set in inlineformset_factory func
        
#         for obj in formset.deleted_objects:
        
#             obj.delete()
        
#         for variant in variants:
        
#             variant.ordinario = self.object
        
#             variant.save()
