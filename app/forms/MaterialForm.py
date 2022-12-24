from django import forms


class MaterialForm(forms.Form):
    name = forms.CharField(label='Название')
    certificate = forms.CharField(label='Сертификат')
    date_start = forms.CharField(label='Дата выдачи сертификата')
    date_end = forms.CharField(label='Дата окончания сертификата')
