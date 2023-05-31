from django import forms
from django.forms import ModelForm, Textarea, TextInput, NumberInput, DateInput, Select
from app.models.ParticipantModel import ParticipantModel


class NaturalPersonForm(forms.Form):
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
    passport_data = forms.CharField(
        label='Паспортные данные',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'passport_data'}),
        required=False,
    )
    address = forms.CharField(
        label='Адрес',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'address'}),
        required=False,
    )
    inn = forms.CharField(
        label='ИНН',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inn'}),
        required=False,
    )
    payment_account = forms.CharField(
        label='Р/С',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'payment_account'}),
        required=False,
    )
    post = forms.CharField(
        label='Должность',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'post'}),
        required=False,
    )
    register_of_specialists = forms.CharField(
        label='Номер в национальном реестре специалистов',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'register_of_specialists'}),
        required=False,
    )
    details_admin_doc = forms.CharField(
        label='Реквизиты распорядительного документа',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'details_admin_doc'}),
        required=False,
    )


class NaturalPerson(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['surname'].required = False
        self.fields['name'].required = False
        self.fields['patronymic'].required = False
        self.fields['passport_data'].required = False
        self.fields['address'].required = False
        self.fields['inn'].required = False
        self.fields['payment_account'].required = False
        self.fields['post'].required = False
        self.fields['register_of_specialists'].required = False
        self.fields['details_admin_doc'].required = False

    class Meta:
        model = ParticipantModel
        fields = ['surname', 'name', 'patronymic', 'passport_data', 'address', 'inn', 'payment_account', 'post',
                  'register_of_specialists', 'details_admin_doc']
        widgets = {
            'surname': TextInput(attrs={'class': 'form-control', 'id': 'surname'}),
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'patronymic': TextInput(attrs={'class': 'form-control', 'id': 'patronymic'}),
            'passport_data': TextInput(attrs={'class': 'form-control', 'id': 'passport_data'}),
            'address': TextInput(attrs={'class': 'form-control', 'id': 'address'}),
            'inn': TextInput(attrs={'class': 'form-control', 'id': 'inn'}),
            'payment_account': TextInput(attrs={'class': 'form-control', 'id': 'payment_account'}),
            'post': TextInput(attrs={'class': 'form-control', 'id': 'post'}),
            'register_of_specialists': TextInput(attrs={'class': 'form-control', 'id': 'register_of_specialists'}),
            'details_admin_doc': TextInput(attrs={'class': 'form-control', 'id': 'details_admin_doc'})
        }

        labels = {
            'surname': 'Фамилия',
            'name': 'Имя',
            'patronymic': 'Отчество',
            'passport_data': 'Паспортные данные',
            'address': 'Юридический адрес',
            'inn': 'ИНН',
            'payment_account': "Р/С",
            'post': 'Должность',
            'register_of_specialists': 'Номер в национальном реестре специалистов',
            'details_admin_doc': 'Реквизиты распорядительного документа'
        }
