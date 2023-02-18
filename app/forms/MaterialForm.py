from django import forms
from django.forms import ModelForm, TextInput, DateInput, NumberInput

from app.models.MaterialModel import MaterialModel


class Material(ModelForm):
    class Meta:
        model = MaterialModel
        fields = ['name', 'certificate', 'date_start', 'date_end', 'count']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'certificate': TextInput(attrs={'class': 'form-control'}),
            'date_start': DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'start'}),
            'date_end': DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'end'}),
            'count': TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            "name": "Название материала",
            "certificate": "Сертификат",
            "date_start": "Дата выдачи сертификата",
            "date_end": "Дата окончания действия сертификата",
            "count": "Количество материалов",
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
    date_end = forms.DateField(label='Дата окончания действия сертификата', widget=forms.DateInput(
        format='%d-%m-%Y',
        attrs={'type': 'date', 'class': 'form-control'}
    ))
    count = forms.CharField(
        label='Количество материалов',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ),
        required=False,
    )

    # def __init__(self, *args, **kwargs):
    #     super(MaterialForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
    #     self.fields['name'].widget.attrs['class'] = 'form-control'
    #     self.fields['certificate'].widget.attrs['class'] = 'form-control'
    #     self.fields['date_start'].widget.attrs['type'] = 'date'
