from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..models.ParticipantModel import ParticipantModel
from ..forms.ParticipantForm import ParticipantForm
from ..models.ProjectModel import ProjectModel


class ParticipantView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        participants = ParticipantModel.objects.all()

        return render(request, 'participants/index.html', {'participants': participants})

    @staticmethod
    def create(request: HttpRequest, project_id, participant) -> HttpResponse:
        form = ParticipantForm()
        form.project_id = project_id
        form.project_field = participant

        return render(request, 'participants/creation.html', {'form': form})

    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:
        form = ParticipantForm(request.POST)
        if form.is_valid():
            project_id = form.cleaned_data["project_id"]
            project = ProjectModel.objects.get(id=project_id)

            participant = ParticipantModel.objects.create(
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
            participant.save()
            project_field = form.cleaned_data['project_field']
            project[f"{project_field}"] = participant
            project.save()

            return render(request, 'participants/creation.html', {'form': form})
