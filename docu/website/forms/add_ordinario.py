from django import forms
from common.utils.distribucion import TipoDistribucion
from ckeditor.widgets import CKEditorWidget
from common.utils.servicios_hls import ServiciosChoices

from ordinario.models import Ordinario, DistribucionExterna
from django.forms import inlineformset_factory


class AddOrdinarioForm(forms.ModelForm):

    distribuciones_internas_asociadas = forms.MultipleChoiceField(
        label='Distribuciones Internas',
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control'
            }
        ),
        # help_text='Para seleccionar más de una distribución, mantenga presionada la tecla Ctrl.',
        required=False,
        choices=ServiciosChoices.SERVICIOS_CHOICES
    )

    # tipo_distribucion = forms.MultipleChoiceField(
    #     label='Tipo de Distribución',
    #     widget=forms.CheckboxSelectMultiple(),
    #     required=False,
    #     choices=TipoDistribucion.DISTRIBUCION_CHOICES
    # )

    class Meta:

        model = Ordinario

        fields = [
            'antecendente',
            'materia',
            'de',
            'cargo_de',
            'a',
            'cargo_a',
            'cuerpo',
            'adjunto',
            'servicio',
            'telefono',
            # 'es_distribucion_interna',
            # 'distribuciones_internas_asociadas',
            # 'es_distribucion_externa',
            # 'distribuciones_externas_asociadas',
        ]

        labels = {
            'antecendente': 'Antecedentes',
            'cargo_de': 'Cargo',
            'cargo_a': 'Cargo',
            # 'distribuciones_internas_asociadas':'Distribuciones Internas Asociadas',
            # 'distribuciones_externas_asociadas': 'Distribuciones externas asociadas',
            'telefono': 'Teléfono',
        }

    def __init__(self, *args, **kwargs):
        super(AddOrdinarioForm, self).__init__(*args, **kwargs)

        for field_key in [
            'antecendente',
            'materia',
            'de',
            'cargo_de',
            'a',
            'cargo_a',
            'cuerpo',
            'adjunto',
            'servicio',
            'telefono',
            # 'es_distribucion_interna',
            # 'distribuciones_internas_asociadas',
            # 'es_distribucion_externa',
            # 'distribuciones_externas_asociadas',
        ]:
            self.fields[field_key].widget.attrs['class'] = \
                'form-control'
            
            if self.fields in (
                'ant',
                'cargo_de',
                'cargo_a',
                'adj',
                # 'distribuciones_internas_asociadas',
                # 'es_distribucion_externa',
                # 'distribuciones_externas_asociadas',
            ):
                
                self.fields[field_key].required = False

        self.fields['de'].widget.attrs['placeholder'] = \
                'Nombre de quién envía el ordinario'
            
        self.fields['cargo_de'].widget.attrs['placeholder'] = \
            'Cargo de quién envía'
        
        self.fields['a'].widget.attrs['placeholder'] = \
            'Nombre hacia quién va dirigido el ordinario'
        
        self.fields['cargo_a'].widget.attrs['placeholder'] = \
            'Cargo de la persona a quien se le envía el ordinario'
        
        self.fields['cuerpo'].widget = CKEditorWidget()

    # Validar si viene es_distribucion_interna, que haya seleccionado al menos un elemento de la lista

    # Validar si viene es_distribucion_externa, que haya seleccionado al menos un elemento de la lista

    def clean_servicio(self):

        servicio_name_value = self.cleaned_data['servicio']
        servicio_name_value = dict(self.fields['servicio'].choices)[servicio_name_value]

        return servicio_name_value
    
    def clean_distribucion_interna(self):

        # selected_choices = self.cleaned_data['distribucion_interna']
        # all_choices = dict(self.fields['distribucion_interna'].choices)

        # selected_choices_values = [all_choices[selected_key] for selected_key in all_choices.keys() if selected_key in selected_choices]

        # return list(selected_choices_values)
        pass


# Completar formset

# OrdinarioFormSet = inlineformset_factory(
#     Ordinario, DistribucionExterna,
#     form=AddOrdinarioForm,
#     extra=1,
#     can_delete=True,
#     can_delete_extra=True
# )