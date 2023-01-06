from django import forms
from app.models.WorkModel import WorkModel
from django.forms import ModelForm, Textarea, TextInput

class Work(ModelForm):
    class Meta:
        model = WorkModel
        fields = ['name_hidden_works', 'number_project_doc', 'number_working_doc', 'other_details_project_drawing']
        # widgets = {
        #     'name_project': TextInput(attrs={'class': 'form-control'}),
        #     'name_project_documentation': TextInput(attrs={'class': 'form-control'}),
        #     'building_address': TextInput(attrs={'class': 'form-control'}),
        #     'number_document': TextInput(attrs={'class': 'form-control'}),
        # }
        #
        # labels = {
        #     "name_project": "Название проекта",
        #     "name_project_documentation": "Наименование проектной документации",
        #     "building_address": "Адресс объекта строительства",
        #     "number_document": "Номер документа",
        # }


class WorkForm(forms.Form):
    name_hidden_works = forms.CharField(label='Наименование скрытых работ', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    number_project_doc = forms.CharField(label='Номер проектной документации', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    number_working_doc = forms.CharField(label='Номер рабочей документации', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    # todo: что это за поле вообще, какой его смысл
    other_details_project_drawing = forms.CharField(label='Другие реквизиты проектного чертежа', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    # todo: что это за поле вообще, какой его смысл
    other_details_working_drawing = forms.CharField(label='Другие реквизиты проектного чертежа', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    name_project_doc = forms.CharField(label='Наименование проектной документации', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    name_working_doc = forms.CharField(label='Наименование рабочей документации', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    information_persons_prepare_doc = forms.CharField(label='Сведения о лицах, осуществялющих подготовку '
                                                            'раздела документации', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    submitted_doc = forms.CharField(label='Предоставленные документы', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    start_date_work = forms.DateField(label='Дата начала работ', widget=forms.DateInput(
        format='%d-%m-%Y',
        attrs={'type': 'date', 'class': 'form-control'}
    ))
    regulatory_acts = forms.CharField(label='Нормативные акты', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    permitted_works = forms.CharField(label='Разрешенные работы', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    additional_information = forms.CharField(label='Дополнительная информация', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    number_instances = forms.IntegerField(label='Количество экземпляров', widget=forms.NumberInput(
        attrs={'class': 'form-control'}
    ))
    applications = forms.CharField(label='Приложения', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
