from django import forms
from app.models.ProjectModel import ProjectModel
from django.forms import ModelForm, Textarea, TextInput


class Project(ModelForm):
    class Meta:
        model = ProjectModel
        fields = ['name_project', 'name_project_documentation', 'building_address', 'project_code']
        widgets = {
            'name_project': TextInput(attrs={'class': 'form-control'}),
            'name_project_documentation': TextInput(attrs={'class': 'form-control'}),
            'building_address': TextInput(attrs={'class': 'form-control'}),
            'project_code': TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            "name_project": "Наименование проекта",
            "name_project_documentation": "Наименование проектной документации",
            "building_address": "Адрес объекта строительства",
            "project_code": "Шифр проекта",
        }


class ProjectForm(forms.Form):
    name_project = forms.CharField(label='Наименование проекта', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    name_project_documentation = forms.CharField(label='Наименование проектной документации', widget=forms.TextInput(
        attrs={'id': 'my_field',
               'class': 'form-control'}
    ))
    building_address = forms.CharField(label='Адрес объекта строительства', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    project_code = forms.CharField(label='Шифр проекта', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
