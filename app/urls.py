from django.urls import path

from app.views.ParticipantView import ParticipantView
from app.views.HomeView import HomeView
from app.views.ProjectView import ProjectView
from app.views.WorkView import WorkView
from app.views.MaterialView import MaterialView
from app.views.BCARView import BCARView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # for projects
    path('projects/create', ProjectView.as_view(), name='project-create'),
    path('projects/index', ProjectView.index, name='project-index'),
    path('projects/<int:value>', ProjectView.view, name='project-view'),
    path('projects/edit/<int:value>', ProjectView.edit, name='project-edit'),
    path('projects/delete/<int:value>', ProjectView.delete, name='project-delete'),

    # for participants
    path('projects/<int:project_id>/add/<str:participant>', ParticipantView.as_view(), name='participant-create'),
    path('participants/index', ParticipantView.index, name='participant-index'),
    path('participants/<int:value>', ParticipantView.view, name='participant-view'),
    path('participants/edit/<int:value>', ParticipantView.edit, name='participant-edit'),
    path('participants/delete/<int:value>', ParticipantView.delete, name='participant-delete'),

    # for works
    path('projects/<int:project_id>/add-work', WorkView.as_view(), name='work-create'),
    path('works/index', WorkView.index, name='work-index'),
    path('works/<int:value>', WorkView.view, name='work-view'),
    path('works/edit/<int:value>', WorkView.edit, name='work-edit'),
    path('works/delete/<int:value>', WorkView.delete, name='work-delete'),
    path('works/create_doc/<int:value>', WorkView.create_doc, name='work-create-doc'),

    # for materials
    path('works/<int:work_id>/material/create', MaterialView.as_view(), name='material-create'),
    path('materials/index', MaterialView.index, name='material-index'),
    path('materials/<int:value>', MaterialView.view, name='material-view'),
    path('materials/edit/<int:value>', MaterialView.edit, name='material-edit'),
    path('materials/delete/<int:value>', MaterialView.delete, name='material-delete'),

    # for bcars
    path('work/<int:work_id>/bcar/create', BCARView.as_view(), name='bcar-create'),
    path('work/<int:work_id>/bcar/delete', BCARView.as_view(), name='bcar-delete'),

]

