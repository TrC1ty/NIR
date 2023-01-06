from django import forms


SubjectType = (
    ('ЮЛ', 'Юридическое лицо'),
    ('ФЛ', 'Физическое лицо'),
    ('ИП', 'Индивидуальный предприниматель'),
    ('СО', 'Саморегулируемая организация'),
)

ParticipantType = (
    ('SUP', 'Поставщик'),
    ('DEV', 'Разработчик'),
    ('REP', 'Представитель'),
    ('OTH', 'Другое'),
)


class ParticipantForm(forms.Form):
    # todo: нужно сделать поле с выбором типа участника
    participant_type = forms.CharField(
        label='Тип участника',
        max_length=2,
        widget=forms.Select(choices=ParticipantType, attrs={'class': 'form-select'})
    )
    # todo: нужно сделать поле с выбором Типа объекта
    subject_type = forms.CharField(
        label='Тип объекта',
        max_length=2,
        widget=forms.Select(choices=SubjectType, attrs={'class': 'form-select'})
    )
    surname = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,
    )
    name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,
    )
    patronymic = forms.CharField(
        label='Отчество',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,
    )
    post = forms.CharField(
        label='Должность',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,
    )
    passport_data = forms.CharField(
        label='Паспортные данные',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,
    )
    register_of_specialists = forms.IntegerField(
        label='Номер а национальном реестре специалистов',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=False,
    )
    ogrn = forms.CharField(
        label='ОГРН',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,
    )
    inn = forms.CharField(
        label='ИНН',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,
    )
    address = forms.CharField(
        label='Адрес',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,
    )
    phone = forms.CharField(
        label='Телефон',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,
    )
    legal_name = forms.CharField(
        label='Юридическое название',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,
    )
    # todo: забыл что значит это поле
    details_admin_doc = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,
    )

    project_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    project_field = forms.CharField(widget=forms.HiddenInput(), required=False)
