from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..models.ParticipantModel import ParticipantModel
from ..forms.ParticipantForm import ParticipantForm
from ..models.ProjectModel import ProjectModel


class ParticipantView(View):
    @staticmethod
    def get(request: HttpRequest, project_id, participant) -> HttpResponse:
        form = ParticipantForm()

        return render(request, 'participants/creation.html', {'form': form, 'project_id': project_id,
                                                              'participant': participant})

    @staticmethod
    def post(request: HttpRequest, project_id, participant) -> HttpResponse:
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
                details_admin_doc=form.cleaned_data["details_admin_doc"]
            )
            participant_new.save()
            print(participant_new.SubjectType[0])
            project.change_participant(participant_new, participant)

            return HttpResponseRedirect(f'/projects/edit/{project_id}')

    @staticmethod
    def index(request: HttpRequest) -> HttpResponse:
        participants = ParticipantModel.objects.all()

        return render(request, 'participants/index.html', {'participants': participants})

    @staticmethod
    def view(request: HttpRequest, value) -> HttpResponse:
        participant = ParticipantModel.objects.get(id=value)

        return render(request, 'participant/participant.html', {'participant': participant})
