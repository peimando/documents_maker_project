from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from ordinario.models import Ordinario
from website.forms import AddOrdinarioForm, OrdinarioFormSet


### ORIGINAL

# class AddOrdinario(CreateView):

#     form_class = AddOrdinarioForm

#     template_name = 'website/ordinario/add_edit_ordinario_inline.html'

#     def get_context_data(self, **kwargs):
 
#         context = super(AddOrdinario, self).get_context_data(**kwargs)
#         context['ordinario_distribucion_externa_formset'] = OrdinarioFormSet()
#         context['title'] = f'Generar Ordinario'
#         context['action'] = 'create'
 
#         return context

#     def post(self, request, *args, **kwargs):

#         self.object = None

#         form_class = self.get_form_class()

#         form = self.get_form()

#         ordinario_distribucion_externa_formset = OrdinarioFormSet(self.request.POST)

#         if form.is_valid() and ordinario_distribucion_externa_formset.is_valid():

#             return self.form_valid(form, ordinario_distribucion_externa_formset)
        
#         else:
            
#             return self.form_invalid(form, ordinario_distribucion_externa_formset)
        
#     def form_valid(self, form, ordinario_distribucion_externa_formset):

#         self.object = form.save(commit=False)

#         # Saving DistribucionesExternas Instance
#         distribuciones_externas = ordinario_distribucion_externa_formset.save(commit=False)

#         for distribucion_externa in distribuciones_externas:

#             distribucion_externa.ordinario = self.object

#             distribucion_externa.save(commit=False)

#             # 

#             distribucion_externa.save()

#         self.object.save()

#         messages.add_message(
#             self.request,
#             messages.SUCCESS,
#             f"El ordinario '{self.object.materia}' se ha generado correctamente."
#         )

#         return super().form_valid(form)

#     def form_invalid(self, form, ordinario_distribucion_externa_formset):

#         return self.render_to_response(
#             self.get_context_data(
#                 form=form,
#                 ordinario_distribucion_externa_formset= ordinario_distribucion_externa_formset
#             )
#         )
    
#     def get_success_url(self) -> str:
        
#         return reverse_lazy(
#             'website:detail_ordinario',
#             kwargs={
#                 'slug': self.object.slug,
#             }
#         )


class OrdinarioInline():

    form_class = AddOrdinarioForm

    model = Ordinario

    template_name = 'website/add_edit_ordinario_inline.html'

    def form_valid(self, form):

        named_formsets = self.get_named_formsets()

        if not all( (f.is_valid() for f in named_formsets.values())):

            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        for name, formset in named_formsets.items():

            formset_save_func = getattr(self, f'formset_{0}_valid', None)

            if formset_save_func is not None:

                formset_save_func(formset)

            else:

                formset.save()

            return redirect('website:list_ordinarios')
            
    def formset_distribucion_externa_valid(self, formset):

        """
        Hook for custom formset saving... useful if you have multiple formsets
        """

        distribuciones_externas_formset = formset.save(commit=False)

        for obj in formset.deleted_objects:
            
            obj.delete()

        for distribucion in distribuciones_externas_formset:

            distribucion.ordinario = self.object
            distribucion.save()

