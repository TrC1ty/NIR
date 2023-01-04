from django import forms


class ParticipantForm(forms.Form):
    # todo: нужно сделать поле с выбором типа участника
    participant_type = forms.CharField(label='Тип участника', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    # todo: нужно сделать поле с выбором Типа объекта
    subject_type = forms.CharField(label='Тип объекта', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    name = forms.CharField(label='Имя', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    patronymic = forms.CharField(label='Отчество', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    post = forms.CharField(label='Должность', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    passport_data = forms.CharField(label='Паспортные данные', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    register_of_specialists = forms.IntegerField(label='Номер а национальном реестре специалистов',
                                                 widget=forms.NumberInput(
        attrs={'class': 'form-control'}
    ))
    ogrn = forms.IntegerField(label='ОГРН', widget=forms.NumberInput(
        attrs={'class': 'form-control'}
    ))
    inn = forms.IntegerField(label='ИНН', widget=forms.NumberInput(
        attrs={'class': 'form-control'}
    ))
    address = forms.CharField(label='Адрес', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    legal_name = forms.CharField(label='Юридическое название', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    # todo: забыл что значит это поле
    details_admin_doc = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    project_id = forms.IntegerField(widget=forms.NumberInput(
        attrs={'style': 'display: none'}
    ))
    project_field = forms.CharField(widget=forms.TextInput(
        attrs={'style': 'display: none'}
    ))
