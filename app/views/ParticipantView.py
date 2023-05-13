from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..models.ParticipantModel import ParticipantModel
from ..models.ProjectParticipant import ProjectParticipant
from ..forms.ParticipantForm import ParticipantForm, Participant
from ..models.ProjectModel import ProjectModel
from ..forms.NaturalPerson import NaturalPersonForm


class ParticipantView(View):
    @staticmethod
    def post(request: HttpRequest, project_id, participant_number) -> HttpResponse:
        form = ParticipantForm(request.POST)

        if form.is_valid():
            project = ProjectModel.objects.get(id=project_id)

            participant_new = ParticipantModel.objects.create(
                surname=form.cleaned_data['surname'],
                name=form.cleaned_data['name'],
                patronymic=form.cleaned_data['patronymic'],
                post=form.cleaned_data['post'],
                passport_data=form.cleaned_data['passport_data'],
                register_of_specialists=form.cleaned_data['register_of_specialists'],
                ogrn=form.cleaned_data['ogrn'],
                inn=form.cleaned_data['inn'],
                kpp=form.cleaned_data['kpp'],
                bic=form.cleaned_data['bic'],
                payment_account=form.cleaned_data['payment_account'],
                cor_account=form.cleaned_data['cor_account'],
                okpo=form.cleaned_data['okpo'],
                okato=form.cleaned_data['okato'],
                okved=form.cleaned_data['okved'],
                mail=form.cleaned_data['mail'],
                site=form.cleaned_data['site'],
                address=form.cleaned_data['address'],
                post_address=form.cleaned_data['post_address'],
                phone=form.cleaned_data['phone'],
                legal_name=form.cleaned_data['legal_name'],
                short_name=form.cleaned_data['short_name'],
                details_admin_doc=form.cleaned_data['details_admin_doc'],
                sro_name=form.cleaned_data['sro_name'],
                sro_inn=form.cleaned_data['sro_inn'],
                sro_ogrn=form.cleaned_data['sro_ogrn'],
                bank_name=form.cleaned_data['bank_name'],
                taxation_system=form.cleaned_data['taxation_system'],
                general_manager=form.cleaned_data['general_manager'],
                participant_type=form.cleaned_data['participant_type'],
                subject_type=form.cleaned_data['subject_type'],
            )

            ProjectParticipant.objects.create(
                project=project,
                participant=participant_new,
                participant_type=participant_number
            )

            return HttpResponseRedirect(f'/projects/{project_id}')
