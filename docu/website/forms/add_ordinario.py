from django import forms
from django.forms import ModelForm
from ordinario.models import Ordinario
from common.utils.distribucion import TipoDistribucion
from ckeditor.widgets import CKEditorWidget
from common.utils.servicios_hls import ServiciosChoices


class AddOrdinarioForm(ModelForm):

    distribucion_interna = forms.MultipleChoiceField(
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
            'tipo_distribucion',
            'distribucion_interna',
            'distribucion_externa',
            'servicio'
        ]

        labels = {
            'antecendente': 'Antecedentes',
            'cargo_de': 'Cargo',
            'cargo_a': 'Cargo',
            'tipo_distribucion': 'Tipo de distribución',
            'distribucion_interna': 'Distribuciones Internas',
            'distribucion_externa': 'Distribución externa'
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
            'tipo_distribucion',
            'distribucion_externa',
            'servicio'
        ]:
            self.fields[field_key].widget.attrs['class'] = \
                'form-control'
            
            self.fields['de'].widget.attrs['placeholder'] = \
                'Nombre de quién envía el ordinario.'
            
            if self.fields in (
                'ant',
                'cargo_de',
                'cargo_a',
                'adj',
                'distribuciones_internas',
                'distribucion_externa',
                'direccion_distribucion_externa',
            ):
                
                self.fields[field_key].required = False

            self.fields['cargo_de'].widget.attrs['placeholder'] = \
                'Cargo de quién envía.'

            self.fields['cuerpo'].widget = CKEditorWidget()
