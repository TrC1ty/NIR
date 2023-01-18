from django import forms
from django.forms import ModelForm, Textarea, TextInput, NumberInput, DateInput, Select
from app.models.ParticipantModel import ParticipantModel

SubjectType = (
    ('ЮЛ', 'Юридическое лицо'),
    ('ФЛ', 'Физическое лицо'),
    ('ИП', 'Индивидуальный предприниматель'),
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
        widget=forms.Select(choices=ParticipantType, attrs={'class': 'form-select', 'id': 'participant_type'})
    )
    # todo: нужно сделать поле с выбором Типа объекта
    subject_type = forms.CharField(
        label='Тип объекта',
        max_length=2,
        widget=forms.Select(choices=SubjectType, attrs={'class': 'form-select', 'id': 'subject_type'})
    )
    surname = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'surname'}),
        required=False,
    )
    name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
        required=False,
    )
    patronymic = forms.CharField(
        label='Отчество',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'patronymic'}),
        required=False,
    )
    post = forms.CharField(
        label='Должность',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'post'}),
        required=False,
    )
    passport_data = forms.CharField(
        label='Паспортные данные',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'passport_data'}),
        required=False,
    )
    register_of_specialists = forms.IntegerField(
        label='Номер в национальном реестре специалистов',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'register_of_specialists'}),
        required=False,
    )
    ogrn = forms.CharField(
        label='ОГРН',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'ogrn'}),
        required=False,
    )
    inn = forms.CharField(
        label='ИНН',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inn'}),
        required=False,
    )
    address = forms.CharField(
        label='Адрес',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'address'}),
        required=False,
    )
    phone = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'phone'}),
        required=False,
    )
    legal_name = forms.CharField(
        label='Юридическое название',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'legal_name'}),
        required=False,
    )
    details_admin_doc = forms.CharField(
        label='Реквизиты распорядительного документа',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'details_admin_doc'}),
        required=False,
    )
    sro_name = forms.CharField(
        label='Наименование СРО',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'sro_name'}),
        required=False,
    )
    sro_inn = forms.CharField(
        label='ИНН СРО',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'sro_inn'}),
        required=False,
    )
    sro_ogrn = forms.CharField(
        label='ОГРН СРО',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'sro_ogrn'}),
        required=False,
    )


class Participant(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['surname'].required = False
        self.fields['name'].required = False
        self.fields['patronymic'].required = False
        self.fields['passport_data'].required = False
        self.fields['register_of_specialists'].required = False
        self.fields['ogrn'].required = False
        self.fields['inn'].required = False
        self.fields['address'].required = False
        self.fields['phone'].required = False
        self.fields['legal_name'].required = False
        self.fields['details_admin_doc'].required = False
        self.fields['sro_name'].required = False
        self.fields['sro_inn'].required = False
        self.fields['sro_ogrn'].required = False

    class Meta:
        model = ParticipantModel
        fields = ['surname', 'name', 'patronymic', 'post', 'passport_data', 'register_of_specialists', 'ogrn', 'inn',
                  'address', 'phone', 'legal_name', 'details_admin_doc', 'participant_type', 'subject_type', 'sro_name',
                  'sro_inn', 'sro_ogrn']
        widgets = {
            'surname': TextInput(attrs={'class': 'form-control', 'id': 'surname'}),
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'patronymic': TextInput(attrs={'class': 'form-control', 'id': 'patronymic'}),
            'post': TextInput(attrs={'class': 'form-control', 'id': 'post'}),
            'passport_data': TextInput(attrs={'class': 'form-control', 'id': 'passport_data'}),
            'register_of_specialists': NumberInput(attrs={'class': 'form-control', 'id': 'register_of_specialists'}),
            'ogrn': TextInput(attrs={'class': 'form-control', 'id': 'ogrn'}),
            'inn': TextInput(attrs={'class': 'form-control', 'id': 'inn'}),
            'address': TextInput(attrs={'class': 'form-control', 'id': 'address'}),
            'phone': DateInput(attrs={'class': 'form-control', 'id': 'phone'}),
            'legal_name': TextInput(attrs={'class': 'form-control', 'id': 'legal_name'}),
            'details_admin_doc': TextInput(attrs={'class': 'form-control', 'id': 'details_admin_doc'}),
            'participant_type': Select(choices=ParticipantType, attrs={'class': 'form-select',
                                                                       'id': 'participant_type'}),
            'subject_type': Select(choices=SubjectType, attrs={'class': 'form-select', 'id': 'subject_type'}),
            'sro_name': TextInput(attrs={'class': 'form-control', 'id': 'sro_name'}),
            'sro_inn': TextInput(attrs={'class': 'form-control', 'id': 'sro_inn'}),
            'sro_ogrn': TextInput(attrs={'class': 'form-control', 'id': 'sro_ogrn'}),
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
            'details_admin_doc': 'Реквизиты распорядительного документа',
            'participant_type': 'Тип участника',
            'subject_type': 'Тип объекта',
            'sro_name': 'Наименование СРО',
            'sro_inn': 'СРО ИНН',
            'sro_ogrn': 'СРО ОГРН'
        }
