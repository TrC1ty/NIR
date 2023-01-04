from django.urls import path

from app.views.ParticipantView import ParticipantView
from app.views.HomeView import HomeView
from app.views.ProjectView import ProjectView
from app.views.WorkView import WorkView
from app.views.MaterialView import MaterialView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # for projects
    path('projects/create', ProjectView.as_view(), name='project-create'),
    path('projects/index', ProjectView.index, name='project-index'),
    path('projects/project/<int:value>', ProjectView.view, name='project-view'),


    path('create-participant', ParticipantView.as_view(), name='create-participant'),
    path('create-work', WorkView.as_view(), name='create-work'),
    path('create-material', MaterialView.as_view(), name='create-material'),
]
