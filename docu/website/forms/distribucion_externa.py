from django import forms


class DistribucionExterna(forms.Form):

    descripcion = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        required=False
    )

    direccion = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        required=False
    )
