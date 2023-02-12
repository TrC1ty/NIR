from django import forms


class BCARForm(forms.Form):
    name = forms.CharField(label='Название bcar', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    code_of_rules_number = forms.CharField(label='Номер свода правил', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
