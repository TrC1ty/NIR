import datetime
import io
import json
import os
import zipfile
from pathlib import Path

from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.encoding import escape_uri_path
from django.views import View
from django.db.models import Q
from docxtpl import DocxTemplate

from app.models.BCARModel import BCARModel
from app.models.ProjectModel import ProjectModel
from app.models.WorkModel import WorkModel
from app.models.ProjectSection import ProjectSection
from app.models.MaterialModel import MaterialModel
from app.models.LegalActModel import LegalActModel
from app.models.ProjectParticipant import ProjectParticipant
from app.forms.BCARForm import BCARForm
from ..forms.WorkForm import WorkForm, Work
from app.forms.MaterialForm import MaterialForm
from app.forms.LegalActForm import LegalActForm


class WorkView(View):
    @staticmethod
    def get(request: HttpRequest, project_id) -> HttpResponse:
        form = WorkForm()

        return render(request, 'works/creation.html', {'form': form, 'project_id': project_id})

    @staticmethod
    def post(request: HttpRequest, project_section_id) -> HttpResponse:
        form = WorkForm(request.POST)
        project_section = ProjectSection.objects.get(id=project_section_id)
        if form.is_valid():
            work = WorkModel.objects.create(
                name_hidden_works=form.cleaned_data["name_hidden_works"],
                number_project_doc=form.cleaned_data["number_project_doc"],
                number_working_doc=form.cleaned_data["number_working_doc"],
                name_project_doc=form.cleaned_data["name_project_doc"],
                name_working_doc=form.cleaned_data["name_working_doc"],
                start_date_work=form.cleaned_data["start_date_work"],
                end_date_work=form.cleaned_data["end_date_work"],
                projectSection=project_section,
            )

            work.save()

        return HttpResponseRedirect(f'/projects/{project_section.project_id}')

    @staticmethod
    def index(request: HttpRequest) -> HttpResponse:
        works = WorkModel.objects.all().order_by('-id')

        return render(request, 'works/index.html', {'works': works})

    @staticmethod
    def view(request: HttpRequest, value) -> HttpResponse:
        work = WorkModel.objects.get(id=value)
        materials = MaterialModel.objects.filter(work=work)
        bcars = BCARModel.objects.filter(work=work)
        legal_acts = LegalActModel.objects.filter(work=work)

        if request.method == 'POST':
            form = WorkForm(request.POST)
            if form.is_valid():
                work.name_hidden_works = form.cleaned_data["name_hidden_works"]
                work.number_project_doc = form.cleaned_data["number_project_doc"]
                work.number_working_doc = form.cleaned_data["number_working_doc"]
                work.other_details_project_drawing = form.cleaned_data["other_details_project_drawing"]
                work.other_details_working_drawing = form.cleaned_data["other_details_working_drawing"]
                work.name_project_doc = form.cleaned_data["name_project_doc"]
                work.name_working_doc = form.cleaned_data["name_working_doc"]
                work.information_persons_prepare_doc = form.cleaned_data["information_persons_prepare_doc"]
                work.start_date_work = form.cleaned_data["start_date_work"]
                work.end_date_work = form.cleaned_data["end_date_work"]
                work.additional_information = form.cleaned_data["additional_information"]
                work.number_instances = form.cleaned_data["number_instances"]

                work.save()

        form = Work(instance=work)
        material_form = MaterialForm()
        bcar_form = BCARForm()
        legal_act_form = LegalActForm()
        works = WorkModel.objects.filter(projectSection__id=work.projectSection.id).filter(~Q(id=work.id))
        data = {
            'work': work,
            'form': form,
            'material_form': material_form,
            'materials': materials,
            'bcar_form': bcar_form,
            'bcars': bcars,
            'legal_acts': legal_acts,
            'legal_act_form': legal_act_form,
            'works': works,
        }

        return render(request, 'works/View.html', data)

    @staticmethod
    def edit(request: HttpRequest, value) -> HttpResponse:
        work = WorkModel.objects.get(id=value)

        if request.method == 'POST':
            form = Work(request.POST)
            body = request.POST.dict()
            next_work_id = body.get('next-work', None)

            if form.is_valid():
                work.name_hidden_works = form.cleaned_data.get("name_hidden_works", "")
                work.number_project_doc = form.cleaned_data.get("number_project_doc", "")
                work.number_working_doc = form.cleaned_data.get("number_working_doc", "")
                work.other_details_project_drawing = form.cleaned_data.get("other_details_project_drawing", "")
                work.other_details_working_drawing = form.cleaned_data.get("other_details_working_drawing", "")
                work.name_project_doc = form.cleaned_data.get("name_project_doc", "")
                work.name_working_doc = form.cleaned_data.get("name_working_doc", "")
                work.information_persons_prepare_doc = form.cleaned_data.get("information_persons_prepare_doc", "")
                work.start_date_work = form.cleaned_data["start_date_work"]
                work.end_date_work = form.cleaned_data["end_date_work"]
                work.additional_information = form.cleaned_data.get("additional_information", "")
                work.number_instances = form.cleaned_data.get("number_instances", 0)
                if next_work_id:
                    next_work = WorkModel.objects.get(id=next_work_id)
                    work.next_work = next_work

                work.save()

        return HttpResponseRedirect(f'/works/{work.id}')

    @staticmethod
    def delete(request: HttpRequest, value) -> HttpResponse:
        work = WorkModel.objects.get(id=value)
        project_id = work.projectSection.project_id
        work.delete()

        return HttpResponseRedirect(f'/projects/{project_id}')

    @staticmethod
    def create_doc(request: HttpRequest, work_id) -> HttpResponse:
        file_stream, filename = create_documentation(work_id)

        response = HttpResponse(file_stream)
        response['Content-Type'] = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        response['Content-Disposition'] = "attachment; filename=" + escape_uri_path(filename)

        return response

    @staticmethod
    def create_acts_in_project(request: HttpRequest, value) -> HttpResponse:
        project_get = ProjectModel.objects.get(id=value)
        works = WorkModel.objects.filter(project=project_get)
        buffer = io.BytesIO()
        my_zip = zipfile.ZipFile(buffer, 'a')
        name_zip = f'{project_get.name_project}.zip'

        for i in range(works.count()):
            file_stream, filename = create_documentation(works[i].id)

            my_zip.writestr(filename, file_stream)
        my_zip.close()

        # Return zip
        response = HttpResponse(buffer.getvalue())
        response['Content-Type'] = 'application/x-zip-compressed'
        response['Content-Disposition'] = "attachment; filename=" + escape_uri_path(name_zip)

        return response


def create_documentation(work_id):
    months = {'1': 'января', '2': 'февраля', '3': 'марта', '4': 'апреля', '5': 'мая', '6': 'июня', '7': 'июля',
              '8': 'августа', '9': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'}

    base_path = Path(__file__).resolve().parent.parent.parent
    path = os.path.join(base_path, 'documentation/akt.docx')
    doc = DocxTemplate(path)

    work = WorkModel.objects.get(id=work_id)
    project = work.projectSection.project

    # добавление объекта капитального строительства
    # добавление застройщика
    # добавление лица, осуществляющего строительство
    # добавление лица, осуществляющего подготовку проектной документации
    # добавление даты, названия и номера работы
    # добавление представителя застройщика
    # добавление представителя лица, осуществляющего строительство
    # добавление специалиста по организации строительства
    # добавление представителя лица, осуществляющего подготовку проектной документации
    # добавление представителя лица, выполнившего работы, подлежащие освидетельствованию
    # добавление иных представителей лиц, участвующих в освидетельствовании
    context = {
        'name_project_documentation': project.name_project_documentation,
        'building_address': project.building_address,
        'builder':
            get_performer(ProjectParticipant.objects.filter(project=project).filter(participant_type=1).first()),
        'person_the_construction':
            get_performer(ProjectParticipant.objects.filter(project=project).filter(participant_type=2).first()),
        'person_prepares_doc':
            get_performer(ProjectParticipant.objects.filter(project=project).filter(participant_type=3).first()),
        'person_performing_work':
            get_performer(ProjectParticipant.objects.filter(project=project).filter(participant_type=4).first()),
        'number': work.id,
        'date_day': datetime.date.today().day,
        'date_month': months[str(datetime.date.today().month)],
        'date_year': datetime.date.today().year,
        'representative_builder':
            get_performer(ProjectParticipant.objects.filter(project=project).filter(participant_type=5).first()),
        'representative_person_the_construction':
            get_performer(ProjectParticipant.objects.filter(project=project).filter(participant_type=6).first()),
        'specialist_organization_construction':
            get_performer(ProjectParticipant.objects.filter(project=project).filter(participant_type=7).first()),
        'representative_person_preparing_project_doc':
            get_performer(ProjectParticipant.objects.filter(project=project).filter(participant_type=8).first()),
        'representative_person_performed_examined':
            get_performer(ProjectParticipant.objects.filter(project=project).filter(participant_type=9).first()),
        'other_persons_participated_examination':
            get_performer(ProjectParticipant.objects.filter(project=project).filter(participant_type=10).first())
    }

    # добавление названия субъекта, которое осуществляло строительство
    if ProjectParticipant.objects.filter(project=project).filter(participant_type=4).first():
        if ProjectParticipant.objects.filter(project=project).filter(participant_type=4).first().participant:
            if ProjectParticipant.objects.filter(project=project).filter(
                    participant_type=4).first().participant.legal_name:
                context['person_the_construction_name'] = \
                    ProjectParticipant.objects.filter(project=project).filter(
                        participant_type=4).first().participant.legal_name

    # добавление названия работ
    if work.name_hidden_works:
        context['name_hidden_works'] = work.name_hidden_works

    # добавление проектной документации, по которой проведены работы
    if work.number_project_doc:
        context['number_project_doc'] = work.number_project_doc
    if work.number_working_doc:
        context['number_working_doc'] = work.number_working_doc
    if work.other_details_project_drawing:
        context['other_details_project_drawing'] = work.other_details_project_drawing
    if work.other_details_working_drawing:
        context['other_details_working_drawing'] = work.other_details_working_drawing
    if work.name_project_doc:
        context['name_project_doc'] = work.name_project_doc
    if work.name_working_doc:
        context['name_working_doc'] = work.name_working_doc
    if work.information_persons_prepare_doc:
        context['information_persons_prepare_doc'] = work.information_persons_prepare_doc

    # добавление материалов
    row = ""
    for material in MaterialModel.objects.filter(work=work):
        row += f"{material.name}, {material.certificate_name}, срок действия c {material.date_start} по " \
               f"{material.date_end}, "

    if len(row) > 2:
        row = f"{row[:-2]}."

    context['materials'] = row

    # добавление начала работ
    context['start_date_work_day'] = work.start_date_work.day
    context['start_date_work_month'] = months[str(work.start_date_work.month)]
    context['start_date_work_year'] = work.start_date_work.year

    # добавление окончания работ
    context['end_date_work_day'] = work.end_date_work.day
    context['end_date_work_month'] = months[str(work.end_date_work.month)]
    context['end_date_work_year'] = work.end_date_work.year

    # работы выполнены в соответствии с...(добавление СНИПОВ)
    row = ""
    for bcar in BCARModel.objects.filter(work=work):
        row += f"{bcar.name}, "

    # [:-2] Для удаления лишней запятой и пробела
    if len(row) > 2:
        context['bcars'] = row[:-2]

    # добавление разрешенных работ
    if work.next_work:
        context['permitted_works'] = work.next_work.name_hidden_works

    # добавление дополнительных сведений
    if work.additional_information:
        context['additional_information'] = work.additional_information

    # добавление количества экземпляров
    if work.number_instances:
        context['number_instances'] = work.number_instances

    # добавление инициалов представителя застройщика
    context['representative_builder_name'] = \
        get_participant_name(ProjectParticipant.objects.filter(project=project).filter(participant_type=5).first())

    # добавление инициалов представителя лица, осуществляющего строительство
    context['representative_person_the_construction_name'] = \
        get_participant_name(ProjectParticipant.objects.filter(project=project).filter(participant_type=6).first())

    # добавление инициалов специалиста по организации строительства
    context['specialist_organization_construction_name'] = \
        get_participant_name(ProjectParticipant.objects.filter(project=project).filter(participant_type=7).first())

    # добавление инициалов представителя лица, осуществляющего подготовку проектной документации
    context['representative_person_preparing_project_doc_name'] = \
        get_participant_name(ProjectParticipant.objects.filter(project=project).filter(participant_type=8).first())

    # добавление инициалов представителя лица, выполнившего работы, подлежащие освидетельствованию
    context['representative_person_performed_examined_name'] = \
        get_participant_name(ProjectParticipant.objects.filter(project=project).filter(participant_type=9).first())

    # добавление инициалов представителей иных лиц
    context['other_persons_participated_examination_name'] = \
        get_participant_name(ProjectParticipant.objects.filter(project=project).filter(participant_type=10).first())

    # добавление приложения
    add_application(work, context,
                    ProjectParticipant.objects.filter(project=project).filter(participant_type=4).first())

    doc.render(context)
    file_stream = io.BytesIO()
    doc.save(file_stream)
    file_stream.seek(0)

    act_name = "акт_"
    if len(work.name_hidden_works) > 20:
        act_name += work.name_hidden_works[0:20] + ".docx"
    else:
        act_name += work.name_hidden_works + ".docx"

    return file_stream, act_name


# добавление актов
def add_application(work, context, project_participant):
    table = []
    acts = LegalActModel.objects.filter(work=work)
    materials = MaterialModel.objects.filter(work=work)
    act_person = ""
    if project_participant:
        if project_participant.participant:
            if project_participant.participant.legal_name:
                act_person = project_participant.participant.legal_name

    cur_page = 4
    if len(acts) > 1:
        context['has_application'] = True
        context['new_page'] = '\f'
        index = 1
        for act in acts:
            table.append({
                'index': index,
                'name': act.name,
                'number': f"{act.document_number} от {work.end_date_work.strftime('%d.%m.%Y')}",
                'person': act_person,
                'count': act.list_count,
                'list_numbers': calculate_the_number_of_pages(int(act.list_count), cur_page)
            })
            cur_page += int(act.list_count)
            index += 1

        for material in materials:
            table.append({
                'index': index,
                'name': material.certificate_name,
                'number': material.certificate_number,
                'person': material.provider,
                'count': material.list_count,
                'list_numbers': calculate_the_number_of_pages(int(material.list_count), cur_page)
            })
            index += 1
            cur_page += int(material.list_count)

        context['table'] = table
        context['submitted_doc'] = "Приложен реестр документов, " \
                                   "подтверждающих соответствие работ предъявляемым к ним требованиям"

    elif len(acts) == 1:
        context['submitted_doc'] = acts[0].name


def get_participant_name(project_participant):
    if project_participant:
        participant = project_participant.participant
        if participant:
            name = ""
            if participant.surname:
                name += participant.surname
            if participant.name:
                name += f" {participant.name[0]}"
            if participant.patronymic:
                name += f" {participant.patronymic[0]}"

            return name

    return ""


def get_performer(project_participant):
    row = ""
    if project_participant:
        participant = project_participant.participant
        if participant:
            attributes = []
            match participant.subject_type:
                case "ЮЛ":
                    if participant.legal_name:
                        attributes.append(participant.legal_name)

                    if participant.ogrn:
                        attributes.append(f"ОГРН: {participant.ogrn}")

                    if participant.inn:
                        attributes.append(f"ИНН: {participant.inn}")

                    if participant.address:
                        attributes.append(f"Адрес: {participant.address}")

                    if participant.phone:
                        attributes.append(f"Телефон: {participant.phone}")

                case "ФЛ":
                    if participant.post:
                        attributes.append(participant.post)

                    if participant.surname:
                        attributes.append(participant.surname)

                    if participant.name:
                        attributes.append(f"{participant.name[0]}.")

                    if participant.patronymic:
                        attributes.append(f"{participant.patronymic[0]}.")

                    if participant.register_of_specialists:
                        attributes.append(participant.register_of_specialists)

                    if participant.details_admin_doc:
                        attributes.append(participant.details_admin_doc)

                    if participant.inn:
                        attributes.append(f"ИНН: {participant.inn}")

                case "ИП":
                    if participant.surname:
                        attributes.append(participant.surname)

                    if participant.name:
                        attributes.append(f"{participant.name[0]}.")

                    if participant.patronymic:
                        attributes.append(f"{participant.patronymic[0]}.")

                    if participant.address:
                        attributes.append(participant.address)

                    if participant.ogrn:
                        attributes.append(f"ОГРН: {participant.ogrn}")

                    if participant.inn:
                        attributes.append(f"ИНН: {participant.inn}")

            if participant.sro_name:
                attributes.extend(f"СРО: {participant.sro_name}")

            if participant.sro_inn:
                attributes.append(f"СРО ИНН: {participant.sro_inn}")

            if participant.sro_ogrn:
                attributes.append(f"СРО ОГРН: {participant.sro_ogrn}")

            attributes = list(filter(None, attributes))
            row = " ".join(attributes)

    return row


def get_representative(representative):
    if representative:
        attributes = [representative.post, representative.surname, representative.name, representative.patronymic,
                      representative.register_of_specialists, representative.details_admin_doc]
        attributes = list(filter(None, attributes))
        return " ".join(attributes)

    return ""


def calculate_the_number_of_pages(list_count, cur_page):
    if list_count > 1:
        return f"{cur_page}-{cur_page + list_count - 1}"
    else:
        return f"{cur_page}"
