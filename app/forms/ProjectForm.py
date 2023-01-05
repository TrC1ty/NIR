from django import forms
from app.models.ProjectModel import ProjectModel
from django.forms import ModelForm, Textarea, TextInput


class Project(ModelForm):
    class Meta:
        model = ProjectModel
        fields = ['name_project', 'name_project_documentation', 'building_address', 'number_document']
        widgets = {
            'name_project': TextInput(attrs={'class': 'form-control'}),
            'name_project_documentation': TextInput(attrs={'class': 'form-control'}),
            'building_address': TextInput(attrs={'class': 'form-control'}),
            'number_document': TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            "name_project": "Название проекта",
            "name_project_documentation": "Наименование проектной документации",
            "building_address": "Адресс объекта строительства",
            "number_document": "Номер документа",
        }

class ProjectForm(forms.Form):
    # todo: как я понял, нужно тут вытаскивать из базы данных челов, сделать из них список и сделать поле с выбором?
    # builder = forms.CharField(label='Застройщик', widget=forms.TextInput(
    #     attrs={'class': 'form-control'}
    # ))

    name_project = forms.CharField(label='Название проекта', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    name_project_documentation = forms.CharField(label='Наименование проектной документации', widget=forms.TextInput(
        attrs={'id': 'my_field',
               'class': 'form-control'}
    ))
    building_address = forms.CharField(label='Адресс объекта строительства', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    number_document = forms.CharField(label='Номер документа', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
