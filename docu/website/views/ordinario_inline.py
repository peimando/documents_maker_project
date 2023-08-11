from django.contrib import messages
from django.shortcuts import redirect

from ordinario.models import Ordinario
from website.forms import AddOrdinarioForm


class OrdinarioInline():

    form_class = AddOrdinarioForm

    model = Ordinario

    template_name = 'website/ordinario/add_edit_ordinario.html'

    def form_valid(self, form):

        named_formsets = self.get_named_formsets()

        if not all( (f.is_valid() for f in named_formsets.values())):

            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        for name, formset in named_formsets.items():

            formset_save_func = getattr(self, f'formset_{name}_valid', None)

            if formset_save_func is not None:

                formset_save_func(formset)

            else:

                formset.save()

            messages.success(
                self.request,
                'El ordinario se ha modificado correctamente.'
            )

            return redirect('website:list_ordinarios')
            
    def formset_distribuciones_externas_valid(self, formset):

        """
        Hook for custom formset saving... useful if you have multiple formsets
        """

        distribuciones_externas_formset = formset.save(commit=False)

        for obj in formset.deleted_objects:
            
            obj.delete()

        for distribucion in distribuciones_externas_formset:

            distribucion.ordinario = self.object

            distribucion.save()
