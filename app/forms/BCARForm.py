from django import forms


class BCARForm(forms.Form):
    name = forms.CharField(label='Название', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
