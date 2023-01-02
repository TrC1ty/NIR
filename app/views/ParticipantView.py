from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..forms.ParticipantForm import ParticipantForm


class ParticipantView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = ParticipantForm()

        return render(request, 'creation/participant.html', {'form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = ParticipantForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')
