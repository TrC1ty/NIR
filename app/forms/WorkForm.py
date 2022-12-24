from django import forms


class WorkForm(forms.Form):
    name_hidden_works = forms.CharField()
    number_project_doc = forms.CharField()
    number_working_doc = forms.CharField()
    other_details_project_drawing = forms.CharField()
    other_details_working_drawing = forms.CharField()
    name_project_doc = forms.CharField()
    name_working_doc = forms.CharField()
    information_persons_prepare_doc = forms.CharField()
    submitted_doc = forms.CharField()
    start_date_work = forms.CharField()
    regulatory_acts = forms.CharField()
    permitted_works = forms.CharField()
    additional_information = forms.CharField()
    number_instances = forms.CharField()
    applications = forms.CharField()
