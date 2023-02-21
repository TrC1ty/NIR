from django import forms
from app.models.WorkModel import WorkModel
from django.forms import ModelForm, Textarea, TextInput, NumberInput, DateInput
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Work(ModelForm):
    class Meta:
        model = WorkModel
        fields = ['name_hidden_works', 'number_project_doc', 'number_working_doc', 'other_details_project_drawing',
                  'other_details_working_drawing', 'name_project_doc', 'name_working_doc',
                  'information_persons_prepare_doc', 'submitted_doc', 'start_date_work', 'end_date_work',
                  'permitted_works', 'additional_information', 'number_instances']
        widgets = {
            'name_hidden_works': TextInput(attrs={'class': 'form-control'}),
            'number_project_doc': TextInput(attrs={'class': 'form-control'}),
            'number_working_doc': TextInput(attrs={'class': 'form-control'}),
            'other_details_project_drawing': TextInput(attrs={'class': 'form-control'}),
            'other_details_working_drawing': TextInput(attrs={'class': 'form-control'}),
            'name_project_doc': TextInput(attrs={'class': 'form-control'}),
            'name_working_doc': TextInput(attrs={'class': 'form-control'}),
            'information_persons_prepare_doc': TextInput(attrs={'class': 'form-control'}),
            'submitted_doc': TextInput(attrs={'class': 'form-control'}),
            'start_date_work': DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'start'}),
            'end_date_work': DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'end'}),
            'permitted_works': TextInput(attrs={'class': 'form-control'}),
            'additional_information': TextInput(attrs={'class': 'form-control'}),
            'number_instances': NumberInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name_hidden_works': 'Наименование скрытых работ',
            'number_project_doc': 'Номер проектной документации',
            'number_working_doc': 'Номер рабочей документации',
            'other_details_project_drawing': 'Другие реквизиты проектного чертежа',
            'other_details_working_drawing': 'Другие реквизиты рабочего чертежа',
            'name_project_doc': 'Наименование проектной документации',
            'name_working_doc': 'Наименование рабочей документации',
            'information_persons_prepare_doc': 'Сведения о лицах, осуществялющих подготовку раздела документации',
            'submitted_doc': 'Предоставленные документы',
            'start_date_work': 'Дата начала работ',
            'end_date_work': 'Дата окончания работ',
            'permitted_works': 'Разрешенные работы',
            'additional_information': 'Дополнительная информация',
            'number_instances': 'Количество экземпляров',
        }


class WorkForm(forms.Form):
    name_hidden_works = forms.CharField(label='Наименование скрытых работ', widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        required=False,
    )
    number_project_doc = forms.CharField(label='Номер проектной документации', widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        required=False,
    )
    number_working_doc = forms.CharField(label='Номер рабочей документации', widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        required=False,
    )
    # todo: что это за поле вообще, какой его смысл
    other_details_project_drawing = forms.CharField(label='Другие реквизиты проектного чертежа', widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        required=False,
    )
    # todo: что это за поле вообще, какой его смысл
    other_details_working_drawing = forms.CharField(label='Другие реквизиты рабочего чертежа', widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        required=False,
    )
    name_project_doc = forms.CharField(label='Наименование проектной документации', widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        required=False,
    )
    name_working_doc = forms.CharField(label='Наименование рабочей документации', widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        required=False,
    )
    information_persons_prepare_doc = forms.CharField(label='Сведения о лицах, осуществялющих подготовку '
                                                            'раздела документации', widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        required=False,
    )
    submitted_doc = forms.CharField(label='Предоставленные документы', widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        required=False,
    )
    start_date_work = forms.DateField(label='Дата начала работ', widget=forms.DateInput(
        format='%d-%m-%Y',
        attrs={'type': 'date', 'class': 'form-control'}),
    )
    end_date_work = forms.DateField(label='Дата окончания работ', widget=forms.DateInput(
        format='%d-%m-%Y',
        attrs={'type': 'date', 'class': 'form-control'}),
    )
    permitted_works = forms.CharField(label='Разрешенные работы', widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        required=False,
    )
    additional_information = forms.CharField(label='Дополнительная информация', widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        required=False,
    )
    number_instances = forms.IntegerField(label='Количество экземпляров', widget=forms.NumberInput(
        attrs={'class': 'form-control'}),
        required=False,
    )


    def clean(self):
        cleaned_data = super().clean()
        start_date_work = cleaned_data.get("start_date_work")
        end_date_work = cleaned_data.get("end_date_work")

        if start_date_work and end_date_work:
            if start_date_work >= end_date_work:
                raise ValidationError("'Дата начала работ' должна быть меньше 'Даты окончания работ'")
        return cleaned_data
