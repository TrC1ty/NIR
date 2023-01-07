from django import forms
from django.forms import ModelForm, TextInput, DateInput

from app.models.MaterialModel import MaterialModel


class Material(ModelForm):
    class Meta:
        model = MaterialModel
        fields = ['name', 'certificate', 'date_start', 'date_end']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'certificate': TextInput(attrs={'class': 'form-control'}),
            'date_start': DateInput(attrs={'class': 'form-control'}),
            'date_end': DateInput(attrs={'class': 'form-control'}),
        }

        labels = {
            "name": "Название материала",
            "certificate": "Сертификат",
            "date_start": "Дата начала",
            "date_end": "Дата конца",
        }


class MaterialForm(forms.Form):
    name = forms.CharField(label='Название', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    certificate = forms.CharField(label='Сертификат', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    date_start = forms.DateField(label='Дата выдачи сертификата', widget=forms.DateInput(
        format='%d-%m-%Y',
        attrs={'type': 'date', 'class': 'form-control'}
    ))
    date_end = forms.DateField(label='Дата окончания сертификата', widget=forms.DateInput(
        format='%d-%m-%Y',
        attrs={'type': 'date', 'class': 'form-control'}
    ))

    # def __init__(self, *args, **kwargs):
    #     super(MaterialForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
    #     self.fields['name'].widget.attrs['class'] = 'form-control'
    #     self.fields['certificate'].widget.attrs['class'] = 'form-control'
    #     self.fields['date_start'].widget.attrs['type'] = 'date'
