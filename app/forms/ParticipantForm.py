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
    ('DEV', 'Участник'),
    ('REP', 'Представитель участника'),
    ('OTH', 'Другое'),
)


class ParticipantForm(forms.Form):
    # todo: нужно сделать поле с выбором типа участника
    participant_type = forms.CharField(
        label='Тип участника',
        max_length=6,
        widget=forms.Select(choices=ParticipantType, attrs={'class': 'form-select', 'id': 'participant_type'})
    )
    # todo: нужно сделать поле с выбором Типа объекта
    subject_type = forms.CharField(
        label='Статус участника',
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
    register_of_specialists = forms.CharField(
        label='Номер в национальном реестре специалистов',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'register_of_specialists'}),
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
        label='Юридический адрес',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'address'}),
        required=False,
    )
    phone = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'phone'}),
        required=False,
    )
    legal_name = forms.CharField(
        label='Наименование юридического лица',
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
    kpp = forms.CharField(
        label='КПП',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'kpp'}),
        required=False,
    )
    bic = forms.CharField(
        label='БИК',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'bic'}),
        required=False,
    )
    payment_account = forms.CharField(
        label='Р/С',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'payment_account'}),
        required=False,
    )
    cor_account = forms.CharField(
        label='К/С',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'cor_account'}),
        required=False,
    )
    okpo = forms.CharField(
        label='ОКПО',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'okpo'}),
        required=False,
    )
    okato = forms.CharField(
        label='ОКАТО',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'okato'}),
        required=False,
    )
    okved = forms.CharField(
        label='ОКВЭД',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'okved'}),
        required=False,
    )
    mail = forms.CharField(
        label='Электронная почта',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'mail'}),
        required=False,
    )
    site = forms.CharField(
        label='Сайт',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'site'}),
        required=False,
    )
    post_address = forms.CharField(
        label='Почтовый адрес',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'post_address'}),
        required=False,
    )
    bank_name = forms.CharField(
        label='Наименование банка',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'bank_name'}),
        required=False,
    )
    taxation_system = forms.CharField(
        label='Система налогообложения',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'taxation_system'}),
        required=False,
    )
    general_manager = forms.CharField(
        label='Генеральный директор',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'general_manager'}),
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
        self.fields['post'].required = False
        self.fields['kpp'].required = False
        self.fields['bic'].required = False
        self.fields['payment_account'].required = False
        self.fields['cor_account'].required = False
        self.fields['okpo'].required = False
        self.fields['okato'].required = False
        self.fields['okved'].required = False
        self.fields['mail'].required = False
        self.fields['site'].required = False
        self.fields['post_address'].required = False
        self.fields['bank_name'].required = False
        self.fields['taxation_system'].required = False
        self.fields['general_manager'].required = False

    class Meta:
        model = ParticipantModel
        fields = ['surname', 'name', 'patronymic', 'post', 'passport_data', 'register_of_specialists', 'ogrn', 'inn',
                  'address', 'phone', 'legal_name', 'details_admin_doc', 'participant_type', 'subject_type', 'sro_name',
                  'sro_inn', 'sro_ogrn', 'kpp', 'bic', 'payment_account', 'cor_account', 'okpo', 'okato', 'okved',
                  'mail', 'site', 'post_address', 'bank_name', 'taxation_system', 'general_manager']
        widgets = {
            'surname': TextInput(attrs={'class': 'form-control', 'id': 'surname'}),
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'patronymic': TextInput(attrs={'class': 'form-control', 'id': 'patronymic'}),
            'post': TextInput(attrs={'class': 'form-control', 'id': 'post'}),
            'passport_data': TextInput(attrs={'class': 'form-control', 'id': 'passport_data'}),
            'register_of_specialists': TextInput(attrs={'class': 'form-control', 'id': 'register_of_specialists'}),
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
            'kpp': TextInput(attrs={'class': 'form-control', 'id': 'kpp'}),
            'bic': TextInput(attrs={'class': 'form-control', 'id': 'bic'}),
            'payment_account': TextInput(attrs={'class': 'form-control', 'id': 'payment_account'}),
            'cor_account': TextInput(attrs={'class': 'form-control', 'id': 'cor_account'}),
            'okpo': TextInput(attrs={'class': 'form-control', 'id': 'okpo'}),
            'okato': TextInput(attrs={'class': 'form-control', 'id': 'okato'}),
            'okved': TextInput(attrs={'class': 'form-control', 'id': 'okved'}),
            'mail': TextInput(attrs={'class': 'form-control', 'id': 'mail'}),
            'site': TextInput(attrs={'class': 'form-control', 'id': 'site'}),
            'post_address': TextInput(attrs={'class': 'form-control', 'id': 'post_address'}),
            'bank_name': TextInput(attrs={'class': 'form-control', 'id': 'bank_name'}),
            'taxation_system': TextInput(attrs={'class': 'form-control', 'id': 'taxation_system'}),
            'general_manager': TextInput(attrs={'class': 'form-control', 'id': 'general_manager'})
        }

        labels = {
            'surname': 'Фамилия',
            'name': 'Имя',
            'patronymic': 'Отчество',
            'post': 'Должность',
            'passport_data': 'Паспортные данные',
            'register_of_specialists': 'Номер в национальном реестре специалистов',
            'ogrn': 'ОГРН',
            'inn': 'ИНН',
            'address': 'Юридический адрес',
            'phone': 'Номер телефона',
            'legal_name': 'Наименование юридического лица',
            'details_admin_doc': 'Реквизиты распорядительного документа',
            'participant_type': 'Тип участника',
            'subject_type': 'Статус участника',
            'sro_name': 'Наименование СРО',
            'sro_inn': 'СРО ИНН',
            'sro_ogrn': 'СРО ОГРН',
            'kpp': "КПП",
            'bic': "БИК",
            'payment_account': "Р/С",
            'cor_account': "К/С",
            'okpo': "ОКПО",
            'okato': "ОКАТО",
            'okved': "ОКВЭД",
            'mail': "Электронная почта",
            'site': "Сайт",
            'post_address': "Почтовый адрес",
            'bank_name': "Наименование банка",
            'taxation_system': "Система налогообложения",
            'general_manager': "Генеральный директор"
        }
