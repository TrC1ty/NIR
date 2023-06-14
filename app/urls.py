from django.urls import path

from app.controllers.MaterialController import MaterialController
from app.controllers.ProjectSectionController import ProjectSectionController
from app.controllers.WorkController import WorkController
from app.controllers.PDFController import PDFController
from app.views.LegalActView import LegalActView
from app.views.ParticipantView import ParticipantView
from app.views.ProjectView import ProjectView
from app.views.WorkView import WorkView
from app.views.MaterialView import MaterialView
from app.views.ProjectSectionView import ProjectSectionView

urlpatterns = [
    # for projects
    path('', ProjectView.index, name='project-index'),
    path('projects/create', ProjectView.create_project, name='project-create'),
    path('projects/post', ProjectView.post, name='project-post'),
    path('projects/<int:value>', ProjectView.view, name='project-view'),
    path('projects/<int:value>/edit', ProjectView.edit, name='project-edit'),
    path('projects/delete/<int:project_id>', ProjectView.delete, name='delete-project'),

    # for participants
    path('projects/<int:project_id>/add/<int:participant_number>',
         ParticipantView.as_view(), name='participant-create'),
    path('projects/<int:project_id>/delete-participant/<int:participant_id>',
         ParticipantView.delete_participant, name='delete-participant'),
    path('projects/<int:project_id>/edit-participant/<int:participant_id>',
         ParticipantView.edit_participant, name='edit-participant'),

    # for works
    path('project-section/<int:project_section_id>/add-work', WorkView.as_view(), name='work-create'),
    path('works/<int:value>', WorkView.view, name='work-view'),
    path('works/create_doc/<int:work_id>', WorkView.create_doc, name='work-create-doc'),
    path('works/create_docs/<int:value>', WorkView.create_acts_in_project, name='work-create-acts'),
    path('works/<int:value>/edit', WorkView.edit, name='edit-work'),
    path('works/<int:value>/delete', WorkView.delete, name='delete-work'),

    # for materials
    path('materials/<int:material_id>/certificate', MaterialView.view_certificate, name='view-certificate'),
    path('materials/<int:material_id>/<int:prev_page>', MaterialView.edit_material, name='edit-material'),
    path('materials/delete/<int:material_id>/<int:prev_page>', MaterialView.delete_material, name='delete-material'),

    # for legal acts
    path('legal-acts/view/<int:act_id>', LegalActView.view_act, name='view-legal-act'),
    path('legal-acts/edit/<int:act_id>', LegalActView.edit_legal_act, name='edit-legal-act'),
    path('legal-acts/delete/<int:act_id>', LegalActView.delete_legal_act, name='delete-legal-act'),

    # for project sections
    path('project-section/<int:project_section_id>/get-registry', ProjectSectionView.get_registry, name='get-registry'),
    path('project-section/<int:project_section_id>/get-pdf', ProjectSectionView.get_pdfs, name='get-pdf'),

    # api
    path('api/works/<int:project_section_id>', WorkController.get),
    path('api/works/<int:work_id>/bcar', WorkController.create_bcar),
    path('api/works/<int:work_id>/act', WorkController.create_act),
    path('api/works/create/<int:section_id>', WorkController.create_work),
    path('api/sections/get/<int:project_id>', ProjectSectionController.get),
    path('api/sections/<int:project_id>', ProjectSectionController.post, name='create-section'),
    path('api/sections/delete/<int:section_id>', ProjectSectionController.delete, name='delete-section'),
    path('api/materials/<int:work_id>', MaterialController.post),
    path('api/materials', MaterialController.get_by_filter),
    path('api/pdf/certificate/<int:material_id>', PDFController.get_certificate),
    path('api/pdf/save', PDFController.save_pdf),
    path('api/pdf/view/<int:pdf_id>', PDFController.view_pdf),
    path('api/pdf/delete/<int:pdf_id>', PDFController.delete_pdf),
]
