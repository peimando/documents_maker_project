from django import forms
from ordinario.models import DistribucionExterna


class AddDistribucionExterna(forms.ModelForm):

    class Meta:

        model = DistribucionExterna

        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddDistribucionExterna, self).__init__(*args, **kwargs)

        for field_key in [
            'descripcion',
            'direccion'
        ]:
            self.fields[field_key].widget.attrs['class'] = \
                'form-control'