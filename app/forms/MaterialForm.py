from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, DateInput, NumberInput

from app.models.MaterialModel import MaterialModel


class Material(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['count'].required = False
        self.fields['units_of_measurement'].required = False
        self.fields['list_count'].required = False

    class Meta:
        model = MaterialModel
        fields = ['name', 'count', 'units_of_measurement', 'list_count', 'provider', 'certificate_name',
                  'certificate_number', 'date_start', 'date_end']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'count': TextInput(attrs={'class': 'form-control'}),
            'units_of_measurement': TextInput(attrs={'class': 'form-control'}),
            'list_count': TextInput(attrs={'class': 'form-control'}),
            'provider': TextInput(attrs={'class': 'form-control'}),
            'certificate_name': TextInput(attrs={'class': 'form-control'}),
            'certificate_number': TextInput(attrs={'class': 'form-control'}),
            'date_start': DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'start'}),
            'date_end': DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'end'}),
        }

        labels = {
            "name": "Наименование материала",
            "count": "Количество материалов",
            "units_of_measurement": "Единицы измерения",
            "list_count": "Количество листов",
            "provider": "Сертификат выдан",
            "certificate_name": "Наименование сертификата",
            "certificate_number": "Номер сертификата",
            "date_start": "Дата выдачи сертификата",
            "date_end": "Дата окончания действия сертификата",
        }


class MaterialForm(forms.Form):
    name = forms.CharField(label='Наименование материала', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    count = forms.CharField(
        label='Количество материалов',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ),
        required=False,
    )
    units_of_measurement = forms.CharField(
        label='Единицы измерения',
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
    provider = forms.CharField(
        label='Сертификат выдан',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    certificate_name = forms.CharField(
        label='Наименование сертификата',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    certificate_number = forms.CharField(
        label='Номер сертификата',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    date_start = forms.DateField(label='Дата выдачи сертификата', widget=forms.DateInput(
        format='%d-%m-%Y',
        attrs={'type': 'date', 'class': 'form-control'}
    ))
    date_end = forms.DateField(label='Дата окончания действия сертификата', widget=forms.DateInput(
        format='%d-%m-%Y',
        attrs={'type': 'date', 'class': 'form-control'}
    ))

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
