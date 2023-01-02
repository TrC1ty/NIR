from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..forms.ProjectForm import ProjectForm


class ProjectView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = ProjectForm()

        return render(request, 'creation/project.html', {'form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = ProjectForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')
