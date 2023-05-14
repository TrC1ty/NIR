import os
from pathlib import Path

from app.models.ProjectSection import ProjectSection
from app.models.WorkModel import WorkModel
from app.models.MaterialModel import MaterialModel
from app.models.LegalActModel import LegalActModel

from django.views import View
from docxtpl import DocxTemplate


class ProjectSectionView(View):
    @staticmethod
    def get_registry(request, project_section_id):
        project_section = ProjectSection.objects.get(id=project_section_id)
        project = project_section.project
        works = WorkModel.objects.filter(project_section_id=project_section_id)
        context = {
            "object": f"Объект: {project.name_project_documentation}\n"
                      f"({project.building_address})",
            "object_name": f"Наименование объекта: {project.name_project}"
        }
        table = []
        index = 1
        list_index = 1
        for work in works:
            if project.person_performed_work:
                provider = project.person_performed_work.legal_name
            else:
                provider = "не заполнено"

            data = {
                "index": index,
                "code": project.project_code,
                "chapter": project_section.name,
                "name": work.name_hidden_works,
                "number": f"{work.number_working_doc} {work.start_date_work}",
                "provider": provider,
                "list_count": 3,
                "list_number": calculate_the_number_of_pages(3, list_index)
            }
            table.append(data)
            list_index += 3
            index += 1

            for act in LegalActModel.objects.filter(work=work):
                data = {
                    "index": index,
                    "code": project.project_code,
                    "chapter": project_section.name,
                    "name": act.name,
                    "number": f"{act.document_number} от {act.document_date}",
                    "provider": provider,
                    "list_count": act.list_count,
                    "list_number": calculate_the_number_of_pages(int(act.list_count), list_index)
                }
                table.append(data)
                list_index += int(act.list_count)
                index += 1

            for material in MaterialModel.objects.filter(work=work):
                data = {
                    "index": index,
                    "code": project.project_code,
                    "chapter": project_section.name,
                    "name": material.certificate_name,
                    "number": f"{material.certificate_number} от {material.date_start}",
                    "provider": material.provider,
                    "list_count": material.list_count,
                    "list_number": calculate_the_number_of_pages(int(material.list_count), list_index)
                }
                table.append(data)
                list_index += int(material.list_count)
                index += 1

        context['table'] = table
        base_path = Path(__file__).resolve().parent.parent.parent
        path = os.path.join(base_path, 'documentation/registry.docx')
        doc = DocxTemplate(path)
        doc.render(context)


def calculate_the_number_of_pages(list_count, cur_page):
    if list_count > 1:
        return f"{cur_page}-{cur_page+list_count-1}"
    else:
        return f"{cur_page}"
