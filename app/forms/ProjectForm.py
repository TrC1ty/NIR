from django import forms


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
    date_act = forms.DateField(label='Дата составления акта', widget=forms.DateInput(
        format='%d-%m-%Y',
        attrs={'type': 'date', 'class': 'form-control'}
    ))
    number_document = forms.CharField(label='Номер документа', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))