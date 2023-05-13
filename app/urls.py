from django.urls import path

from app.controllers.MaterialController import MaterialController
from app.controllers.ProjectSectionController import ProjectSectionController
from app.controllers.WorkController import WorkController
from app.views.LegalActView import LegalActView
from app.views.ParticipantView import ParticipantView
from app.views.ProjectView import ProjectView
from app.views.WorkView import WorkView
from app.views.MaterialView import MaterialView


urlpatterns = [
    # for projects
    path('', ProjectView.index, name='project-index'),
    path('projects/create', ProjectView.create_project, name='project-create'),
    path('projects/post', ProjectView.post, name='project-post'),
    path('projects/<int:value>', ProjectView.view, name='project-view'),

    # for participants
    path('projects/<int:project_id>/add/<int:participant_number>', ParticipantView.as_view(), name='participant-create'),

    # for works
    path('project-section/<int:project_section_id>/add-work', WorkView.as_view(), name='work-create'),
    path('works/<int:value>', WorkView.view, name='work-view'),
    path('works/create_doc/<int:value>', WorkView.create_doc, name='work-create-doc'),
    path('works/create_docs/<int:value>', WorkView.create_acts_in_project, name='work-create-acts'),

    # for materials
    path('materials/<int:material_id>/certificate', MaterialView.view_certificate, name='view-certificate'),

    # for legal acts
    path('legal-acts/view/<int:act_id>', LegalActView.view_act, name='view-legal-act'),

    # api
    path('api/works/<int:project_section_id>', WorkController.get),
    path('api/works/<int:work_id>/bcar', WorkController.create_bcar),
    path('api/works/<int:work_id>/act', WorkController.create_act),
    path('api/sections/<int:project_id>', ProjectSectionController.post, name='create-section'),
    path('api/materials/<int:work_id>', MaterialController.post),
    path('api/materials', MaterialController.get_by_filter)
]

