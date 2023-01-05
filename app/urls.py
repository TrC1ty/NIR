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
    path('projects/edit/<int:value>', ProjectView.edit, name='project-edit'),
    path('projects/index', ProjectView.index, name='project-index'),
    path('projects/<int:value>', ProjectView.view, name='project-view'),
    path('projects/delete/<int:value>', ProjectView.delete, name='project-delete'),

    # for participants
    path('participants/index', ParticipantView.as_view(), name='participant-index'),
    path('projects/<int:project_id>/add/<str:participant>', ParticipantView.create, name='participant-create'),

    # for works
    path('works/index', WorkView.as_view(), name='work-index'),
    path('projects/<int:project_id>/add/work', WorkView.create, name='work-create'),

    path('create-material', MaterialView.as_view(), name='create-material'),
]

