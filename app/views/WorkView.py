from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..forms.WorkForm import WorkForm


class WorkView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = WorkForm()
        return render(request, 'creation/work.html', {'form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = WorkForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')
