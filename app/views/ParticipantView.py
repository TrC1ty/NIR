from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render

from ..forms.IndividualEntrepreneur import IndividualEntrepreneur
from ..forms.LegalEntity import LegalEntity
from ..models.ParticipantModel import ParticipantModel
from ..models.ProjectParticipant import ProjectParticipant
from ..forms.ParticipantForm import ParticipantForm
from ..models.ProjectModel import ProjectModel
from ..forms.NaturalPerson import NaturalPerson


def get_participant_name(participant):
    if participant:
        name = ""
        if participant.surname:
            name += participant.surname
        if participant.name:
            name += f" {participant.name[0]}"
        if participant.patronymic:
            name += f" {participant.patronymic[0]}"

        return name

    return "Имя не введено"


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

    @staticmethod
    def edit_participant(request: HttpRequest, project_id, participant_id):
        participant = ParticipantModel.objects.get(id=participant_id)
        if request.method == "POST":
            match participant.subject_type:
                case "ЮЛ":
                    form = LegalEntity(request.POST)
                case "ФЛ":
                    form = NaturalPerson(request.POST)
                case _:
                    form = IndividualEntrepreneur(request.POST)

            if form.is_valid():
                participant.surname = form.cleaned_data.get('surname')
                participant.name = form.cleaned_data.get('name')
                participant.patronymic = form.cleaned_data.get('patronymic')
                participant.post = form.cleaned_data.get('post')
                participant.passport_data = form.cleaned_data.get('passport_data')
                participant.register_of_specialists = form.cleaned_data.get('register_of_specialists')
                participant.ogrn = form.cleaned_data.get('ogrn')
                participant.inn = form.cleaned_data.get('inn')
                participant.kpp = form.cleaned_data.get('kpp')
                participant.bic = form.cleaned_data.get('bic')
                participant.payment_account = form.cleaned_data.get('payment_account')
                participant.cor_account = form.cleaned_data.get('cor_account')
                participant.okpo = form.cleaned_data.get('okpo')
                participant.okato = form.cleaned_data.get('okato')
                participant.okved = form.cleaned_data.get('okved')
                participant.mail = form.cleaned_data.get('mail')
                participant.site = form.cleaned_data.get('site')
                participant.address = form.cleaned_data.get('address')
                participant.post_address = form.cleaned_data.get('post_address')
                participant.phone = form.cleaned_data.get('phone')
                participant.legal_name = form.cleaned_data.get('legal_name')
                participant.short_name = form.cleaned_data.get('short_name')
                participant.details_admin_doc = form.cleaned_data.get('details_admin_doc')
                participant.sro_name = form.cleaned_data.get('sro_name')
                participant.sro_inn = form.cleaned_data.get('sro_inn')
                participant.sro_ogrn = form.cleaned_data.get('sro_ogrn')
                participant.bank_name = form.cleaned_data.get('bank_name')
                participant.taxation_system = form.cleaned_data.get('taxation_system')
                participant.general_manager = form.cleaned_data.get('general_manager')

                participant.save()

        else:
            match participant.subject_type:
                case "ЮЛ":
                    form = LegalEntity(instance=participant)
                case "ФЛ":
                    form = NaturalPerson(instance=participant)
                case _:
                    form = IndividualEntrepreneur(instance=participant)

        match participant.subject_type:
            case "ЮЛ":
                participant_name = participant.legal_name
            case "ФЛ":
                participant_name = get_participant_name(participant)
            case _:
                participant_name = participant.legal_name

        if participant.participant_type == 'CONSTR':
            show_sro = True
        else:
            show_sro = False

        data = {
            'form': form,
            'project_id': project_id,
            'participant_id': participant_id,
            'participant_name': participant_name,
            'show_sro': show_sro
        }

        return render(request, 'participants/Edit.html', data)

    @staticmethod
    def delete_participant(request: HttpRequest, project_id, participant_id):
        participant = ParticipantModel.objects.get(id=participant_id)
        participant.delete()

        return HttpResponseRedirect(f'/projects/{project_id}')
