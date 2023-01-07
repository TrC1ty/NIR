from django import forms
from django.forms import ModelForm, Textarea, TextInput, NumberInput, DateInput, Select
from app.models.ParticipantModel import ParticipantModel

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
        max_length=3,
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
        label='Номер телефона',
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


class Participant(ModelForm):
    class Meta:
        model = ParticipantModel
        fields = ['surname', 'name', 'patronymic', 'post', 'passport_data', 'register_of_specialists', 'ogrn', 'inn',
                  'address', 'phone', 'legal_name', 'details_admin_doc', 'participant_type', 'subject_type']
        widgets = {
            'surname': TextInput(attrs={'class': 'form-control'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'patronymic': TextInput(attrs={'class': 'form-control'}),
            'post': TextInput(attrs={'class': 'form-control'}),
            'passport_data': TextInput(attrs={'class': 'form-control'}),
            'register_of_specialists': NumberInput(attrs={'class': 'form-control'}),
            'ogrn': TextInput(attrs={'class': 'form-control'}),
            'inn': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            'phone': DateInput(attrs={'class': 'form-control'}),
            'legal_name': TextInput(attrs={'class': 'form-control'}),
            'details_admin_doc': TextInput(attrs={'class': 'form-control'}),
            'participant_type': Select(choices=ParticipantType, attrs={'class': 'form-select'}),
            'subject_type': Select(choices=SubjectType, attrs={'class': 'form-select'}),
        }

        labels = {
            'surname': 'Фамилия',
            'name': 'Имя',
            'patronymic': 'Отчество',
            'post': 'Должность',
            'passport_data': 'Паспортные данные',
            'register_of_specialists': 'Номер а национальном реестре специалистов',
            'ogrn': 'ОГРН',
            'inn': 'ИНН',
            'address': 'Адрес',
            'phone': 'Номер телефона',
            'legal_name': 'Юридическое название',
            'details_admin_doc': '',
            'participant_type': 'Тип участника',
            'subject_type': 'Тип объекта',
        }