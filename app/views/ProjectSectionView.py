from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from app.models.ProjectModel import ProjectModel
from app.models.ProjectSection import ProjectSection


class ProjectSectionView(View):
    @staticmethod
    def post(request: HttpRequest, project_id) -> HttpResponse:
        form = request.POST.dict()
        project = ProjectModel.objects.get(id=project_id)
        if form['section_name']:
            ProjectSection.objects.create(
                project=project,
                name=form['section_name']
            )

        return HttpResponseRedirect(f'/projects/{project_id}')
