from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, DateInput, NumberInput

from app.models.MaterialModel import MaterialModel


class Material(ModelForm):
    class Meta:
        model = MaterialModel
        fields = ['name', 'certificate', 'date_start', 'date_end', 'count', 'list_count']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'certificate': TextInput(attrs={'class': 'form-control'}),
            'date_start': DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'start'}),
            'date_end': DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'end'}),
            'count': TextInput(attrs={'class': 'form-control'}),
            'list_count': TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            "name": "Название материала",
            "certificate": "Сертификат",
            "date_start": "Дата выдачи сертификата",
            "date_end": "Дата окончания действия сертификата",
            "count": "Количество материалов",
            "list_count": "Количество листов",
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
    list_count = forms.CharField(
        label='Количество листов',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ),
        required=False,
    )

    def clean(self):
        cleaned_data = super(MaterialForm, self).clean()
        date_start = cleaned_data.get("date_start")
        date_end = cleaned_data.get("date_end")

        if date_start and date_end:
            if date_start >= date_end:
                raise ValidationError("«Дата начала» должна быть меньше «Даты конца»")
        return cleaned_data

    # def __init__(self, *args, **kwargs):
    #     super(MaterialForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
    #     self.fields['name'].widget.attrs['class'] = 'form-control'
    #     self.fields['certificate'].widget.attrs['class'] = 'form-control'
    #     self.fields['date_start'].widget.attrs['type'] = 'date'
