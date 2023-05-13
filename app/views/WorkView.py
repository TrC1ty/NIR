import datetime
import io
import os
import zipfile
from pathlib import Path

from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.encoding import escape_uri_path
from django.views import View
from docxtpl import DocxTemplate

from app.models.BCARModel import BCARModel
from app.models.ProjectModel import ProjectModel
from app.models.WorkModel import WorkModel
from app.models.ProjectSection import ProjectSection
from app.models.MaterialModel import MaterialModel
from app.models.LegalActModel import LegalActModel
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
                work.permitted_works = form.cleaned_data["permitted_works"]
                work.additional_information = form.cleaned_data["additional_information"]
                work.number_instances = form.cleaned_data["number_instances"]

                work.save()

        form = Work(instance=work)
        material_form = MaterialForm()
        bcar_form = BCARForm()
        legal_act_form = LegalActForm()
        data = {
            'work': work,
            'form': form,
            'material_form': material_form,
            'materials': materials,
            'bcar_form': bcar_form,
            'bcars': bcars,
            'legal_acts': legal_acts,
            'legal_act_form': legal_act_form,
        }

        return render(request, 'works/View.html', data)

    @staticmethod
    def edit(request: HttpRequest, value) -> HttpResponse:
        work = WorkModel.objects.get(id=value)

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
                work.permitted_works = form.cleaned_data["permitted_works"]
                work.additional_information = form.cleaned_data["additional_information"]
                work.number_instances = form.cleaned_data["number_instances"]

                work.save()

                return render(request, 'works/View.html', {'work': work})

        form = Work(instance=work)

        return render(request, 'works/View.html', {'work': work,
                                                   'form': form})

    @staticmethod
    def delete(request: HttpRequest, value) -> HttpResponse:
        work = WorkModel.objects.get(id=value)
        work.delete()
        works = WorkModel.objects.all()

        return render(request, 'works/index.html', {'works': works})

    @staticmethod
    def create_doc(request: HttpRequest, value) -> HttpResponse:
        filepath, filename = create_documentation(value)
        file = open(filepath, 'rb')
        content = file.read()

        response = HttpResponse(
            content,
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
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
            filepath, filename = create_documentation(works[i].id)
            file = open(filepath, 'rb')
            content = file.read()

            my_zip.writestr(filename, content)
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
    project = work.project

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
        'builder': get_performer(project.builder),
        'person_the_construction': get_performer(project.person_the_construction),
        'person_prepares_doc': get_performer(project.person_prepares_doc),
        'person_performing_work': get_performer(project.person_performed_work),
        'number': work.id,
        'name_project': project.name_project,
        'date_day': datetime.date.today().day,
        'date_month': months[str(datetime.date.today().month)],
        'date_year': datetime.date.today().year,
        'representative_builder': get_performer(project.representative_builder),
        'representative_person_the_construction': get_performer(project.representative_person_the_construction),
        'specialist_organization_construction': get_performer(project.specialist_organization_construction),
        'representative_person_preparing_project_doc': get_performer(
            project.representative_person_preparing_project_doc),
        'representative_person_performed_examined': get_performer(
            project.representative_person_performed_examined),
        'other_persons_participated_examination': get_performer(project.other_persons_participated_examination)
    }

    # добавление названия субъекта, которое осуществляло строительство
    if project.person_performed_work:
        context['person_the_construction_name'] = project.person_performed_work.legal_name

    # добавление названия работ
    context['name_hidden_works'] = work.name_hidden_works

    # добавление проектной документации, по которой проведены работы
    context['number_project_doc'] = work.number_project_doc
    context['number_working_doc'] = work.number_working_doc
    context['other_details_project_drawing'] = work.other_details_project_drawing
    context['other_details_working_drawing'] = work.other_details_working_drawing
    context['name_project_doc'] = work.name_project_doc
    context['name_working_doc'] = work.name_working_doc
    context['information_persons_prepare_doc'] = work.information_persons_prepare_doc

    # добавление материалов
    row = ""
    for material in work.materials.all():
        row += f"{material.name}, {material.certificate}, срок действия c {material.date_start} по " \
               f"{material.date_end}, "

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
    for bcar in work.bcars.all():
        row += f"{bcar.name}, "

    # [:-2] Для удаления лишней запятой и пробела
    context['bcars'] = row[:-2]

    # добавление разрешенных работ
    context['permitted_works'] = work.permitted_works

    # добавление дополнительных сведений
    context['additional_information'] = work.additional_information

    # добавление количества экземпляров
    context['number_instances'] = work.number_instances

    # добавление инициалов представителя застройщика
    context['representative_builder_name'] = get_participant_name(project.representative_builder)

    # добавление инициалов представителя лица, осуществляющего строительство
    context['representative_person_the_construction_name'] = \
        get_participant_name(project.representative_person_the_construction)

    # добавление инициалов специалиста по организации строительства
    context['specialist_organization_construction_name'] = \
        get_participant_name(project.specialist_organization_construction)

    # добавление инициалов представителя лица, осуществляющего подготовку проектной документации
    context['representative_person_preparing_project_doc_name'] = \
        get_participant_name(project.representative_person_preparing_project_doc)

    # добавление инициалов представителя лица, выполнившего работы, подлежащие освидетельствованию
    context['representative_person_performed_examined_name'] = \
        get_participant_name(project.representative_person_performed_examined)

    # добавление инициалов представителей иных лиц
    context['other_persons_participated_examination_name'] = \
        get_participant_name(project.other_persons_participated_examination)

    # добавление приложения
    add_application(work, context, project.builder)

    doc.render(context)
    path = os.path.join(base_path, 'documentation/new_act.docx')
    doc.save(path)

    act_name = "акт_"
    if len(work.name_hidden_works) > 20:
        act_name += work.name_hidden_works[0:20] + ".docx"
    else:
        act_name += work.name_hidden_works + ".docx"

    return path, act_name


# добавление актов
def add_application(work, context, builder):
    table = []
    acts = work.acts.all()
    act_person = ""
    if builder:
        act_person = builder.legal_name

    if len(acts) > 1:
        context['has_application'] = True
        context['new_page'] = '\f'
        last_i = 0
        for i in range(len(acts)):
            table.append({
                'index': i + 1,
                'name': acts[i].name,
                'number': f"от {work.end_date_work.strftime('%d.%m.%Y')}",
                'person': act_person,
                'count': 1,
            })
            last_i = i

        materials = work.materials.all()
        for material in materials:
            last_i += 1
            table.append({
                'index': last_i + 1,
                'name': "Сертификат соответствия",
                'number': material.certificate.replace("Сертификат соответствия", "").strip(),
                'person': material.provider.legal_name,
                'count': material.list_count,
            })

        context['table'] = table
        context['submitted_doc'] = "Приложен реестр документов, " \
                                   "подтверждающих соответствие работ предъявляемым к ним требованиям"

    elif len(acts) == 1:
        context['submitted_doc'] = acts[0].name


def get_participant_name(participant):
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


def get_performer(participant):
    row = ""
    if participant:
        attributes = []
        match participant.subject_type:
            case "ЮЛ":
                attributes = [participant.legal_name, participant.ogrn, participant.inn, participant.address,
                              participant.phone]
            case "ФЛ":
                attributes = [participant.surname, participant.name, participant.patronymic, participant.passport_data,
                              participant.address, participant.phone]
            case "ИП":
                attributes = [participant.surname, participant.name, participant.patronymic, participant.address,
                              participant.ogrn, participant.inn]

        attributes.extend([participant.sro_name, participant.sro_inn, participant.sro_ogrn])
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
