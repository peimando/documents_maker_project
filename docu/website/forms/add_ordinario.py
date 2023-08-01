from django.forms import ModelForm
from ordinario.models import Ordinario


class AddOrdinarioForm(ModelForm):

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
            'distribucion_externa'
        ]

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
        ]:
            self.fields[field_key].widget.attrs['class'] = \
                'form-control'