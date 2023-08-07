from datetime import datetime
from typing import Any, Dict
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
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
                'slug': self.object.slug,
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
