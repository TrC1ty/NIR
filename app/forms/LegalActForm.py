from django import forms
from django.forms import ModelForm, TextInput, DateInput

from app.models.LegalActModel import LegalActModel


class LegalAct(ModelForm):
    class Meta:
        model = LegalActModel
        fields = ['name', 'document_number', 'document_date', 'list_count']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'document_name'}),
            'document_number': TextInput(attrs={'class': 'form-control', 'id': 'document_number'}),
            'document_date': DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date', 'id': 'document_date'}),
            'list_count': TextInput(attrs={'class': 'form-control', 'id': 'document_list_count'}),
        }

        labels = {
            "name": "Наименование",
            "document_number": "Номер документа",
            "document_date": "Дата составления",
            "list_count": "Количество страниц",
        }


class LegalActForm(forms.Form):
    name = forms.CharField(
        label='Наименование',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'document_name'}
        )
    )
    document_number = forms.CharField(
        label='Номер документа',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'document_number'}
        )
    )
    document_date = forms.DateField(
        label='Дата составления',
        widget=forms.DateInput(
            format='%d-%m-%Y',
            attrs={'type': 'date', 'class': 'form-control', 'id': 'document_date'}
        )
    )
    list_count = forms.CharField(
        label='Количество страниц',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'document_list_count'}
        )
    )
