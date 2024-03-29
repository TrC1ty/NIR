from django import forms
from django.forms import ModelForm, TextInput
from app.models.ParticipantModel import ParticipantModel


class IndividualEntrepreneurForm(forms.Form):
    legal_name = forms.CharField(
        label='Полное наименование',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'legal_name'}),
        required=False,
    )
    short_name = forms.CharField(
        label='Краткое наименование',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'short_name'}),
        required=False,
    )
    address = forms.CharField(
        label='Адрес регистрации',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'address'}),
        required=False,
    )
    post_address = forms.CharField(
        label='Фактический адрес',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'post_address'}),
        required=False,
    )
    mail = forms.CharField(
        label='Электронная почта',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'mail'}),
        required=False,
    )
    phone = forms.CharField(
        label='Телефон',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'phone'}),
        required=False,
    )
    inn = forms.CharField(
        label='ИНН',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inn'}),
        required=False,
    )
    ogrn = forms.CharField(
        label='ОГРНИП',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'ogrn'}),
        required=False,
    )
    bank_name = forms.CharField(
        label='Наименование банка',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'bank_name'}),
        required=False,
    )
    bic = forms.CharField(
        label='БИК',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'bic'}),
        required=False,
    )
    cor_account = forms.CharField(
        label='К/С',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'cor_account'}),
        required=False,
    )
    payment_account = forms.CharField(
        label='Р/С',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'payment_account'}),
        required=False,
    )
    okved = forms.CharField(
        label='ОКВЭД',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'okved'}),
        required=False,
    )
    taxation_system = forms.CharField(
        label='Система налогообложения',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'taxation_system'}),
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


class IndividualEntrepreneur(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['legal_name'].required = False
        self.fields['short_name'].required = False
        self.fields['address'].required = False
        self.fields['post_address'].required = False
        self.fields['mail'].required = False
        self.fields['phone'].required = False
        self.fields['inn'].required = False
        self.fields['ogrn'].required = False
        self.fields['bank_name'].required = False
        self.fields['bic'].required = False
        self.fields['cor_account'].required = False
        self.fields['payment_account'].required = False
        self.fields['okved'].required = False
        self.fields['taxation_system'].required = False
        self.fields['sro_name'].required = False
        self.fields['sro_inn'].required = False
        self.fields['sro_ogrn'].required = False

    class Meta:
        model = ParticipantModel
        fields = ['legal_name', 'short_name', 'address', 'post_address', 'mail', 'phone', 'inn', 'ogrn', 'bank_name',
                  'bic', 'cor_account', 'payment_account', 'okved', 'taxation_system', 'sro_name', 'sro_inn',
                  'sro_ogrn']
        widgets = {
            'legal_name': TextInput(attrs={'class': 'form-control', 'id': 'legal_name'}),
            'short_name': TextInput(attrs={'class': 'form-control', 'id': 'short_name'}),
            'address': TextInput(attrs={'class': 'form-control', 'id': 'address'}),
            'post_address': TextInput(attrs={'class': 'form-control', 'id': 'post_address'}),
            'mail': TextInput(attrs={'class': 'form-control', 'id': 'mail'}),
            'phone': TextInput(attrs={'class': 'form-control', 'id': 'phone'}),
            'inn': TextInput(attrs={'class': 'form-control', 'id': 'inn'}),
            'ogrn': TextInput(attrs={'class': 'form-control', 'id': 'ogrn'}),
            'bank_name': TextInput(attrs={'class': 'form-control', 'id': 'bank_name'}),
            'bic': TextInput(attrs={'class': 'form-control', 'id': 'bic'}),
            'cor_account': TextInput(attrs={'class': 'form-control', 'id': 'cor_account'}),
            'payment_account': TextInput(attrs={'class': 'form-control', 'id': 'payment_account'}),
            'okved': TextInput(attrs={'class': 'form-control', 'id': 'okved'}),
            'taxation_system': TextInput(attrs={'class': 'form-control', 'id': 'taxation_system'}),
            'sro_name': TextInput(attrs={'class': 'form-control', 'id': 'sro_name'}),
            'sro_inn': TextInput(attrs={'class': 'form-control', 'id': 'sro_inn'}),
            'sro_ogrn': TextInput(attrs={'class': 'form-control', 'id': 'sro_ogrn'})
        }

        labels = {
            'legal_name': 'Полное наименование',
            'short_name': 'Краткое наименование',
            'address': 'Адрес регистрации',
            'post_address': 'Фактический адрес',
            'mail': 'Электронная почта',
            'phone': 'Телефон',
            'inn': 'ИНН',
            'ogrn': 'ОГРНИП',
            'bank_name': 'Наименование банка',
            'bic': 'БИК',
            'cor_account': 'К/С',
            'payment_account': 'Р/С',
            'okved': 'ОКВЭД',
            'taxation_system': 'Система налогообложения',
            'sro_name': 'Наименование СРО',
            'sro_inn': 'ИНН СРО',
            'sro_ogrn': 'ОГРН СРО',
        }
