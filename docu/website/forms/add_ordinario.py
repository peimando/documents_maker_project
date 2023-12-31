from django import forms
from ckeditor.widgets import CKEditorWidget
from common.utils.servicios_hls import ServiciosChoices
from ordinario.models import Ordinario


class AddOrdinarioForm(forms.ModelForm):

    distribuciones_internas_asociadas = forms.MultipleChoiceField(
        label='Distribuciones Internas',
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control'
            }
        ),
        help_text='Para seleccionar más de una distribución, mantenga presionada la tecla Ctrl.',
        required=False,
        choices=ServiciosChoices.SERVICIOS_CHOICES
    )

    class Meta:

        model = Ordinario

        fields = [
            'antecedente',
            'materia',
            'de',
            'cargo_de',
            'a',
            'cargo_a',
            'cuerpo',
            'adjunto',
            'servicio',
            'telefono',
            'distribuciones_internas_asociadas',
            'tiene_distribucion_externa',
        ]

        labels = {
            'antecedente': 'Antecedentes',
            'cargo_de': 'Cargo',
            'cargo_a': 'Cargo',
            'distribuciones_internas_asociadas':'Distribuciones Internas Asociadas',
            'telefono': 'Teléfono',
        }

    def __init__(self, *args, **kwargs):

        super(AddOrdinarioForm, self).__init__(*args, **kwargs)

        for field_key in [
            'antecedente',
            'materia',
            'de',
            'cargo_de',
            'a',
            'cargo_a',
            'cuerpo',
            'adjunto',
            'servicio',
            'telefono',
            'distribuciones_internas_asociadas',
            'tiene_distribucion_externa',
        ]:
            self.fields[field_key].widget.attrs['class'] = \
                'form-control'
            
            if self.fields in (
                'antecedente',
                'cargo_de',
                'cargo_a',
                'adjunto',
                'tiene_distribucion_externa'
            ):
                
                self.fields[field_key].required = False   

        self.fields['de'].widget.attrs['placeholder'] = \
                'Nombre de quién envía el ordinario'
            
        self.fields['cargo_de'].widget.attrs['placeholder'] = \
            'Cargo de quién envía'
        
        self.fields['cargo_a'].required = False
        
        self.fields['a'].widget.attrs['placeholder'] = \
            'Nombre hacia quién va dirigido el ordinario'
        
        self.fields['cargo_a'].widget.attrs['placeholder'] = \
            'Cargo de la persona a quien se le envía el ordinario'
        
        self.fields['telefono'].widget.attrs['placeholder'] = \
                'Número teléfonico del servicio que envía el ordinario'
        
        self.fields['adjunto'].widget.attrs['placeholder'] = \
                'Cantidad de adjuntos que se enviarán'

        self.fields['cuerpo'].widget = CKEditorWidget()

        self.fields['tiene_distribucion_externa'] = forms.ChoiceField(
            widget=forms.RadioSelect(),
            choices=[
                (True, 'Sí'),
                (False, 'No')
            ]
        )

    # Validar que la lista de distribuciones_internas no venga vacia
    def clean_distribuciones_internas_asociadas(self):

        data = self.cleaned_data['distribuciones_internas_asociadas']
        all_choices = dict(self.fields['distribuciones_internas_asociadas'].choices)

        selected_choices_values = [all_choices[selected_key] for selected_key in all_choices.keys() if selected_key in data]

        if not data:

            raise forms.ValidationError('La lista de campos no puede ser vacía.')

        return selected_choices_values

    # Validar si viene es_distribucion_externa, que haya seleccionado al menos un elemento de la lista