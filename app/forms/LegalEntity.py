from django import forms
from django.forms import ModelForm, TextInput
from app.models.ParticipantModel import ParticipantModel


class IndividualEntrepreneurForm(forms.Form):
    legal_name = forms.CharField(
        label='Полное наименование',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'legal_name'}),
        required=False,
    )
    address = forms.CharField(
        label='Юридический адрес',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'address'}),
        required=False,
    )
    post_address = forms.CharField(
        label='Почтовый адрес',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'post_address'}),
        required=False,
    )
    inn = forms.CharField(
        label='ИНН',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inn'}),
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
    ogrn = forms.CharField(
        label='ОГРН',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'ogrn'}),
        required=False,
    )
    general_manager = forms.CharField(
        label='Генеральный директор',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'general_manager'}),
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
    site = forms.CharField(
        label='Сайт',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'site'}),
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
        self.fields['address'].required = False
        self.fields['post_address'].required = False
        self.fields['inn'].required = False
        self.fields['kpp'].required = False
        self.fields['bic'].required = False
        self.fields['payment_account'].required = False
        self.fields['cor_account'].required = False
        self.fields['okpo'].required = False
        self.fields['okato'].required = False
        self.fields['okved'].required = False
        self.fields['ogrn'].required = False
        self.fields['general_manager'].required = False
        self.fields['mail'].required = False
        self.fields['phone'].required = False
        self.fields['site'].required = False
        self.fields['sro_name'].required = False
        self.fields['sro_inn'].required = False
        self.fields['sro_ogrn'].required = False

    class Meta:
        model = ParticipantModel
        fields = ['legal_name', 'address', 'post_address', 'inn', 'kpp', 'bic', 'payment_account', 'cor_account',
                  'okpo', 'okato', 'okved', 'ogrn', 'general_manager', 'mail', 'phone', 'site', 'sro_name', 'sro_inn',
                  'sro_ogrn']
        widgets = {
            'legal_name': TextInput(attrs={'class': 'form-control', 'id': 'legal_name'}),
            'address': TextInput(attrs={'class': 'form-control', 'id': 'address'}),
            'post_address': TextInput(attrs={'class': 'form-control', 'id': 'post_address'}),
            'inn': TextInput(attrs={'class': 'form-control', 'id': 'inn'}),
            'kpp': TextInput(attrs={'class': 'form-control', 'id': 'kpp'}),
            'bic': TextInput(attrs={'class': 'form-control', 'id': 'bic'}),
            'payment_account': TextInput(attrs={'class': 'form-control', 'id': 'payment_account'}),
            'cor_account': TextInput(attrs={'class': 'form-control', 'id': 'cor_account'}),
            'okpo': TextInput(attrs={'class': 'form-control', 'id': 'okpo'}),
            'okato': TextInput(attrs={'class': 'form-control', 'id': 'okato'}),
            'okved': TextInput(attrs={'class': 'form-control', 'id': 'okved'}),
            'ogrn': TextInput(attrs={'class': 'form-control', 'id': 'ogrn'}),
            'general_manager': TextInput(attrs={'class': 'form-control', 'id': 'general_manager'}),
            'mail': TextInput(attrs={'class': 'form-control', 'id': 'mail'}),
            'phone': TextInput(attrs={'class': 'form-control', 'id': 'phone'}),
            'site': TextInput(attrs={'class': 'form-control', 'id': 'site'}),
            'sro_name': TextInput(attrs={'class': 'form-control', 'id': 'sro_name'}),
            'sro_inn': TextInput(attrs={'class': 'form-control', 'id': 'sro_inn'}),
            'sro_ogrn': TextInput(attrs={'class': 'form-control', 'id': 'sro_ogrn'})
        }

        labels = {
            'legal_name': 'Полное наименование',
            'address': 'Юридический адрес',
            'post_address': 'Почтовый адрес',
            'inn': 'ИНН',
            'kpp': 'КПП',
            'bic': 'БИК',
            'payment_account': 'Р/С',
            'cor_account': 'К/С',
            'okpo': 'ОКПО',
            'okato': 'ОКАТО',
            'okved': 'ОКВЭД',
            'ogrn': 'ОГРН',
            'general_manager': 'Генеральный директор',
            'mail': 'Электронная почта',
            'phone': 'Телефон',
            'site': 'Сайт',
            'sro_name': 'Наименование СРО',
            'sro_inn': 'ИНН СРО',
            'sro_ogrn': 'ОГРН СРО',
        }
