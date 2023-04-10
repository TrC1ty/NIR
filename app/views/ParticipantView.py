from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..models.ParticipantModel import ParticipantModel
from ..forms.ParticipantForm import ParticipantForm, Participant
from ..models.ProjectModel import ProjectModel
from ..forms.NaturalPerson import NaturalPersonForm


class ParticipantView(View):
    @staticmethod
    def get(request: HttpRequest, project_id, participant) -> HttpResponse:
        form = ParticipantForm()
        naturalPerson = NaturalPersonForm()
        participant_name = get_participant_name(participant)

        return render(request, 'participants/creation.html', {'form': form, 'project_id': project_id,
                                                              'participant': participant,
                                                              'participant_name': participant_name,
                                                              'naturalPerson': naturalPerson})

    @staticmethod
    def post(request: HttpRequest, project_id) -> HttpResponse:
        form = ParticipantForm(request.POST)

        if form.is_valid():
            project = ProjectModel.objects.get(id=project_id)

            participant_new = ParticipantModel.objects.create(
                participant_type=form.cleaned_data["participant_type"],
                subject_type=form.cleaned_data["subject_type"],
                surname=form.cleaned_data["surname"],
                name=form.cleaned_data["name"],
                patronymic=form.cleaned_data["patronymic"],
                post=form.cleaned_data["post"],
                passport_data=form.cleaned_data["passport_data"],
                register_of_specialists=form.cleaned_data["register_of_specialists"],
                ogrn=form.cleaned_data["ogrn"],
                inn=form.cleaned_data["inn"],
                address=form.cleaned_data["address"],
                phone=form.cleaned_data["phone"],
                legal_name=form.cleaned_data["legal_name"],
                details_admin_doc=form.cleaned_data["details_admin_doc"],
                sro_name=form.cleaned_data["sro_name"],
                sro_inn=form.cleaned_data["sro_inn"],
                sro_ogrn=form.cleaned_data["sro_ogrn"],
                kpp=form.cleaned_data["kpp"],
                bic=form.cleaned_data["bic"],
                payment_account=form.cleaned_data["payment_account"],
                cor_account=form.cleaned_data["cor_account"],
                okpo=form.cleaned_data["okpo"],
                okato=form.cleaned_data["okato"],
                okved=form.cleaned_data["okved"],
                mail=form.cleaned_data["mail"],
                site=form.cleaned_data["site"],
                post_address=form.cleaned_data["post_address"],
                bank_name=form.cleaned_data["bank_name"],
                taxation_system=form.cleaned_data["taxation_system"],
                general_manager=form.cleaned_data["general_manager"]
            )
            participant_new.save()
            print(participant_new.SubjectType[0])
            project.change_participant(participant_new, participant)

            return HttpResponseRedirect(f'/projects/{project_id}')

    @staticmethod
    def index(request: HttpRequest) -> HttpResponse:
        participants = ParticipantModel.objects.all().order_by('-id')

        return render(request, 'participants/index.html', {'participants': participants})

    @staticmethod
    def view(request: HttpRequest, value) -> HttpResponse:
        participant = ParticipantModel.objects.get(id=value)

        return render(request, 'participants/participant.html', {'participant': participant})

    @staticmethod
    def delete(request: HttpRequest, value) -> HttpResponse:
        participant = ParticipantModel.objects.get(id=value)
        participant.delete()
        participants = ParticipantModel.objects.all()

        return render(request, 'participants/index.html', {'participants': participants})

    @staticmethod
    def edit(request: HttpRequest, value) -> HttpResponse:
        participant = ParticipantModel.objects.get(id=value)
        if request.method == 'POST':
            form = ParticipantForm(request.POST)
            if form.is_valid():
                participant.participant_type = form.cleaned_data["participant_type"]
                participant.subject_type = form.cleaned_data["subject_type"]
                participant.surname = form.cleaned_data["surname"]
                participant.name = form.cleaned_data["name"]
                participant.patronymic = form.cleaned_data["patronymic"]
                participant.post = form.cleaned_data["post"]
                participant.passport_data = form.cleaned_data["passport_data"]
                participant.register_of_specialists = form.cleaned_data["register_of_specialists"]
                participant.ogrn = form.cleaned_data["ogrn"]
                participant.inn = form.cleaned_data["inn"]
                participant.address = form.cleaned_data["address"]
                participant.phone = form.cleaned_data["phone"]
                participant.legal_name = form.cleaned_data["legal_name"]
                participant.details_admin_doc = form.cleaned_data["details_admin_doc"]
                participant.sro_name = form.cleaned_data["sro_name"]
                participant.sro_inn = form.cleaned_data["sro_inn"]
                participant.sro_ogrn = form.cleaned_data["sro_ogrn"]
                participant.kpp = form.cleaned_data["kpp"],
                participant.bic = form.cleaned_data["bic"],
                participant.payment_account = form.cleaned_data["payment_account"],
                participant.cor_account = form.cleaned_data["cor_account"],
                participant.okpo = form.cleaned_data["okpo"],
                participant.okato = form.cleaned_data["okato"],
                participant.okved = form.cleaned_data["okved"],
                participant.mail = form.cleaned_data["mail"],
                participant.site = form.cleaned_data["site"],
                participant.post_address = form.cleaned_data["post_address"]
                participant.bank_name = form.cleaned_data["bank_name"]
                participant.taxation_system = form.cleaned_data["taxation_system"]
                participant.general_manager = form.cleaned_data["general_manager"]
                participant.save()

                return render(request, 'participants/participant.html', {'participant': participant})

        form = Participant(instance=participant)

        return render(request, 'participants/edit.html', {'participant': participant, 'form': form})


def get_participant_name(column):
    participant_name = ""

    match column:
        case "builder":
            participant_name = "Застройщике"
        case "person_the_construction":
            participant_name = "Лице, осуществляющем строительство"
        case "person_prepares_doc":
            participant_name = "Лице, осуществляющем подготовку проектной документации"
        case "representative_builder":
            participant_name = "Представителе застройщика по вопросам строительного контроля"
        case "representative_person_the_construction":
            participant_name = "Представителе лица, осуществляющего строительство"
        case "specialist_organization_construction":
            participant_name = "Представителе лица, осуществляющего строительство, по вопросам строительного контроля"
        case "representative_person_preparing_project_doc":
            participant_name = "Представителе лица, осуществляющего подготовку проектной документации"
        case "representative_person_performed_examined":
            participant_name = "Представителе лица, выполнившего работы, подлежащие освидетельствованию"
        case "other_persons_participated_examination":
            participant_name = "Иных представителях лиц, участвующих в освидетельствовании"

    return participant_name
