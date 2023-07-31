from django import forms
from common.utils.servicios_hls import ServiciosChoices
from common.utils.distribucion import TipoDistribucion
from ckeditor.widgets import CKEditorWidget


class OrdinarioPdfForm(forms.Form):

    ant = forms.CharField(
        initial='No hay',
        label='Antecedentes',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        required=False
    )
    mat = forms.CharField(
        initial='Envío factura',
        label='Materia',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        required=True
    )

    de = forms.CharField(
        initial='Alejandra Ramírez Flores',
        label='De',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de quién envía el ordinario.'
            }
        ),
        required=True
    )

    cargo_de = forms.CharField(
        initial='Jefe de subdepartamento de Finanza(s)',
        label='Cargo',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Cargo de quién envía.'
            }
        ),
        required=False
    )

    a = forms.CharField(
        initial='Jefatura ejecutiva de administración de los fondos de salud del ejército',
        label='A',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre hacia quién va dirigido el ordinario'
            }
        ),
        required=True
    )

    cargo_a = forms.CharField(
        initial='Jefe de subdepartamento de Finanza(s)',
        label='Cargo',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Cargo de la persona a quien se le envía el ordinario.'
            }
        ),
        required=False
    )

    cuerpo = forms.CharField(
        widget=CKEditorWidget(),
        label='Cuerpo',
        required=True
    )

    adj = forms.CharField(
        label='Adjuntos',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        required=False
    )

    tipo_distribucion = forms.MultipleChoiceField(
        label='Tipo de Distribución',
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        choices=TipoDistribucion.DISTRIBUCION_CHOICES
    )

    distribuciones_internas = forms.MultipleChoiceField(
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

    distribucion_externa = forms.CharField(
        label='Distribución Externa',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la distribución a cual se dirige este ordinario.'
            }
        ),
        required=False
    )

    direccion_distribucion_externa = forms.CharField(
        label='Dirección de distribución',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        required=False
    )

    servicio = forms.ChoiceField(
        label='Servicio o Unidad',
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        ),
        required=False,
        choices=ServiciosChoices.SERVICIOS_CHOICES
    )

    telefono = forms.IntegerField(
        label='Teléfono',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        ),
        required=True,
    )
