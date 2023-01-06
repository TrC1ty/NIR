from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..forms.WorkForm import WorkForm
from app.models.WorkModel import WorkModel
from app.models.ProjectModel import ProjectModel


class WorkView(View):
    @staticmethod
    def get(request: HttpRequest, project_id) -> HttpResponse:
        form = WorkForm()
        form.project_id = project_id

        return render(request, 'works/creation.html', {'form': form, 'project_id': project_id})

    @staticmethod
    def post(request: HttpRequest, project_id) -> HttpResponse:
        form = WorkForm(request.POST)
        if form.is_valid():
            project = ProjectModel.objects.get(id=project_id)

            work = WorkModel.objects.create(
                name_hidden_works=form.cleaned_data["name_hidden_works"],
                number_project_doc=form.cleaned_data["number_project_doc"],
                number_working_doc=form.cleaned_data["number_working_doc"],
                other_details_project_drawing=form.cleaned_data["other_details_project_drawing"],
                other_details_working_drawing=form.cleaned_data["other_details_working_drawing"],
                name_project_doc=form.cleaned_data["name_project_doc"],
                name_working_doc=form.cleaned_data["name_working_doc"],
                information_persons_prepare_doc=form.cleaned_data["information_persons_prepare_doc"],
                submitted_doc=form.cleaned_data["submitted_doc"],
                start_date_work=form.cleaned_data["start_date_work"],
                regulatory_acts=form.cleaned_data["regulatory_acts"],
                permitted_works=form.cleaned_data["permitted_works"],
                additional_information=form.cleaned_data["additional_information"],
                number_instances=form.cleaned_data["number_instances"],
                applications=form.cleaned_data["applications"],
                project=project
            )
            work.save()

            return HttpResponseRedirect(f'/works/{work.id}')

    @staticmethod
    def index(request: HttpRequest) -> HttpResponse:
        works = WorkModel.objects.all()

        return render(request, 'works/index.html', {'works': works})

    @staticmethod
    def view(request: HttpRequest, value) -> HttpResponse:
        work = WorkModel.objects.get(id=value)

        return render(request, 'works/work.html', {'work': work})