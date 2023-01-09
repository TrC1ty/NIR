from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..forms.WorkForm import WorkForm, Work
from app.models.WorkModel import WorkModel
from app.models.ProjectModel import ProjectModel
from ..models.MaterialModel import MaterialModel
from docxtpl import DocxTemplate
from pathlib import Path
import os
import datetime


class WorkView(View):
    @staticmethod
    def get(request: HttpRequest, project_id) -> HttpResponse:
        form = WorkForm()

        return render(request, 'works/creation.html', {'form': form, 'project_id': project_id})

    @staticmethod
    def post(request: HttpRequest, project_id) -> HttpResponse:
        form = WorkForm(request.POST)
        if form.is_valid():
            project = ProjectModel.objects.get(id=project_id)

            work = WorkModel.objects.create(
                name_hidden_works=form.cleaned_data["name_hidden_works"],
                number_project_doc=form.cleaned_data["number_project_doc"],
                number_working_doc=form.cleaned_data["number_working_doc"],
                other_details_project_drawing=form.cleaned_data["other_details_project_drawing"],
                other_details_working_drawing=form.cleaned_data["other_details_working_drawing"],
                name_project_doc=form.cleaned_data["name_project_doc"],
                name_working_doc=form.cleaned_data["name_working_doc"],
                information_persons_prepare_doc=form.cleaned_data["information_persons_prepare_doc"],
                submitted_doc=form.cleaned_data["submitted_doc"],
                start_date_work=form.cleaned_data["start_date_work"],
                regulatory_acts=form.cleaned_data["regulatory_acts"],
                permitted_works=form.cleaned_data["permitted_works"],
                additional_information=form.cleaned_data["additional_information"],
                number_instances=form.cleaned_data["number_instances"],
                applications=form.cleaned_data["applications"],
                project=project
            )
            work.save()

            return HttpResponseRedirect(f'/works/{work.id}')

    @staticmethod
    def index(request: HttpRequest) -> HttpResponse:
        works = WorkModel.objects.all().order_by('-id')

        return render(request, 'works/index.html', {'works': works})

    @staticmethod
    def view(request: HttpRequest, value) -> HttpResponse:
        work = WorkModel.objects.get(id=value)

        return render(request, 'works/work.html', {'work': work})

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
                work.submitted_doc = form.cleaned_data["submitted_doc"]
                work.start_date_work = form.cleaned_data["start_date_work"]
                work.regulatory_acts = form.cleaned_data["regulatory_acts"]
                work.permitted_works = form.cleaned_data["permitted_works"]
                work.additional_information = form.cleaned_data["additional_information"]
                work.number_instances = form.cleaned_data["number_instances"]
                work.applications = form.cleaned_data["applications"]
                work.save()

                return render(request, 'works/work.html', {'work': work})

        form = Work(instance=work)

        return render(request, 'works/edit.html', {'work': work,
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
        response['Content-Disposition'] = "attachment; filename=%s" % filename

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
    context = {
        'name_project_documentation': project.name_project_documentation,
        'building_address': project.building_address,
    }

    # добавление застройщика
    row = ""
    if project.builder:
        match project.builder.SubjectType:
            case "ЮЛ":
                row = f"{project.builder.legal_name} {project.builder.ogrn} {project.builder.inn} " \
                      f"{project.builder.address} {project.builder.phone} "
            case "ФЛ":
                row = f"{project.builder.surname} {project.builder.name} {project.builder.patronymic} " \
                      f"{project.builder.passport_data} {project.builder.address} {project.builder.phone} "
            case "ИП":
                row = f"{project.builder.surname} {project.builder.name} {project.builder.patronymic} " \
                      f"{project.builder.address} {project.builder.ogrn} {project.builder.inn} "

    if project.builder_so:
        row += f"{project.builder_so.legal_name} {project.builder_so.ogrn} {project.builder_so.inn}"

    context['builder'] = row

    # добавление лица, осуществляющего строительство
    row = ""
    if project.person_the_construction:
        match project.person_the_construction.SubjectType:
            case "ЮЛ":
                row = f"{project.person_the_construction.legal_name} {project.person_the_construction.ogrn} " \
                      f"{project.person_the_construction.inn} {project.person_the_construction.address} " \
                      f"{project.person_the_construction.phone} "
            case "ИП":
                row = f"{project.person_the_construction.surname} {project.person_the_construction.name} " \
                      f"{project.person_the_construction.patronymic} {project.person_the_construction.address} " \
                      f"{project.person_the_construction.ogrn} {project.person_the_construction.inn} "

    if project.person_the_construction_so:
        row += f"{project.person_the_construction_so.legal_name} {project.person_the_construction_so.ogrn} " \
               f"{project.person_the_construction_so.inn}"

    context['person_the_construction'] = row

    # добавление лица, осуществляющего подготовку проектной документации
    row = ""
    if project.person_prepares_doc:
        match project.person_prepares_doc.SubjectType:
            case "ЮЛ":
                row = f"{project.person_prepares_doc.legal_name} {project.person_prepares_doc.ogrn} " \
                      f"{project.person_prepares_doc.inn} {project.person_prepares_doc.address} " \
                      f"{project.person_prepares_doc.phone} "
            case "ИП":
                row = f"{project.person_prepares_doc.surname} {project.person_prepares_doc.name} " \
                      f"{project.person_prepares_doc.patronymic} {project.person_prepares_doc.address} " \
                      f"{project.person_prepares_doc.ogrn} {project.person_prepares_doc.inn} "

    if project.person_prepares_doc_so:
        row += f"{project.person_prepares_doc_so.legal_name} {project.person_prepares_doc_so.ogrn} " \
               f"{project.person_prepares_doc_so.inn}"

    context['person_prepares_doc'] = row

    # добавление даты, названия и номера работы
    context['number'] = work.id
    context['name_project'] = project.name_project
    context['date_day'] = datetime.date.today().day
    context['date_month'] = months[str(datetime.date.today().month)]
    context['date_year'] = datetime.date.today().year

    # добавление представителя застройщика
    if project.representative_builder:
        row = ""
        row += f"{project.representative_builder.post} {project.representative_builder.surname} " \
               f"{project.representative_builder.name} {project.representative_builder.patronymic} " \
               f"{project.representative_builder.register_of_specialists} " \
               f"{project.representative_builder.details_admin_doc}"

        context['representative_builder'] = row

    # добавление представителя лица, осуществляющего строительство
    if project.representative_person_the_construction:
        row = ""
        row += f"{project.representative_person_the_construction.post} " \
               f"{project.representative_person_the_construction.surname} " \
               f"{project.representative_person_the_construction.name} " \
               f"{project.representative_person_the_construction.patronymic} " \
               f"{project.representative_person_the_construction.details_admin_doc}"

        context['representative_person_the_construction'] = row

    # добавление специалиста по организации строительства
    if project.specialist_organization_construction:
        row = ""
        row += f"{project.specialist_organization_construction.post} " \
               f"{project.specialist_organization_construction.surname} " \
               f"{project.specialist_organization_construction.name} " \
               f"{project.specialist_organization_construction.patronymic} " \
               f"{project.specialist_organization_construction.register_of_specialists} " \
               f"{project.specialist_organization_construction.details_admin_doc}"

        context['specialist_organization_construction'] = row

    # добавление представителя лица, осуществляющего подготовку проектной документации
    if project.representative_person_preparing_project_doc:
        row = ""
        row += f"{project.representative_person_preparing_project_doc.post} " \
               f"{project.representative_person_preparing_project_doc.surname} " \
               f"{project.representative_person_preparing_project_doc.name} " \
               f"{project.representative_person_preparing_project_doc.patronymic} " \
               f"{project.representative_person_preparing_project_doc.details_admin_doc}"

        context['representative_person_preparing_project_doc'] = row

    # добавление представителя лица, выполнившего работы, подлежащие освидетельствованию
    if project.representative_person_performed_examined:
        row = ""
        row += f"{project.representative_person_performed_examined.post} " \
               f"{project.representative_person_performed_examined.surname} " \
               f"{project.representative_person_performed_examined.name} " \
               f"{project.representative_person_performed_examined.patronymic} " \
               f"{project.representative_person_performed_examined.details_admin_doc}"

        context['representative_person_performed_examined'] = row

    # добавление иных представителей лиц, участвующих в освидетельствовании
    if project.other_persons_participated_examination:
        row = ""
        row += f"{project.other_persons_participated_examination.post} " \
               f"{project.other_persons_participated_examination.surname} " \
               f"{project.other_persons_participated_examination.name} " \
               f"{project.other_persons_participated_examination.patronymic} " \
               f"{project.other_persons_participated_examination.details_admin_doc}"

        context['other_persons_participated_examination'] = row

    # добавление названия субъекта, которое осуществляло строительство
    context['person_the_construction_name'] = project.builder.legal_name

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

    # добавление предъявленных документов
    context['submitted_doc'] = work.submitted_doc

    # добавление начала работ
    context['start_date_work_day'] = work.start_date_work.day
    context['start_date_work_month'] = months[str(work.start_date_work.month)]
    context['start_date_work_year'] = work.start_date_work.year

    # добавление разрешенных работ
    context['permitted_works'] = work.permitted_works

    # добавление дополнительных сведений
    context['additional_information'] = work.additional_information

    # добавление количества экземпляров
    context['number_instances'] = work.number_instances

    # добавление приложения
    context['applications'] = work.applications

    # добавление инициалов представителя застройщика
    if project.representative_builder:
        if project.representative_builder.patronymic == "":
            context['representative_builder_name'] = f"{project.representative_builder.surname} " \
                                                     f"{project.representative_builder.name[0]}."
        else:
            context['representative_builder_name'] = f"{project.representative_builder.surname} " \
                                                     f"{project.representative_builder.name[0]}." \
                                                     f"{project.representative_builder.patronymic[0]}."

    # добавление инициалов представителя лица, осуществляющего строительство
    if project.representative_person_the_construction:
        if project.representative_person_the_construction.patronymic == "":
            context['representative_person_the_construction_name'] = f"{project.representative_person_the_construction.surname} " \
                                                                     f"{project.representative_person_the_construction.name[0]}."
        else:
            context[
                'representative_person_the_construction_name'] = f"{project.representative_person_the_construction.surname} " \
                                                                 f"{project.representative_person_the_construction.name[0]}."\
                                                                 f"{project.representative_builder.patronymic[0]}."


    # добавление инициалов специалиста по организации строительства
    if project.specialist_organization_construction:
        if project.specialist_organization_construction.patronymic == "":
            context['specialist_organization_construction_name'] = f"{project.specialist_organization_construction.surname} " \
                                                                   f"{project.specialist_organization_construction.name[0]}."
        else:
            context['specialist_organization_construction_name'] = f"{project.specialist_organization_construction.surname} " \
                                                               f"{project.specialist_organization_construction.name[0]}." \
                                                               f"{project.specialist_organization_construction.patronymic[0]}."


    # добавление инициалов представителя лица, осуществляющего подготовку проектной документации
    if project.representative_person_preparing_project_doc:
        if project.representative_person_preparing_project_doc.patronymic == "":
            context['representative_person_preparing_project_doc_name'] = f"{project.representative_person_preparing_project_doc.surname} " \
                                                                          f"{project.representative_person_preparing_project_doc.name[0]}."
        else:
            context['representative_person_preparing_project_doc_name'] = f"{project.representative_person_preparing_project_doc.surname} " \
                                                                      f"{project.representative_person_preparing_project_doc.name[0]}." \
                                                                      f"{project.representative_person_preparing_project_doc.patronymic[0]}."


    # добавление инициалов представителя лица, выполнившего работы, подлежащие освидетельствованию
    if project.representative_person_performed_examined:
        if project.representative_person_performed_examined.patronymic == "":
            context['representative_person_performed_examined_name'] = f"{project.representative_person_performed_examined.surname} " \
                                                                       f"{project.representative_person_performed_examined.name[0]}."
        else:
            context['representative_person_performed_examined_name'] = f"{project.representative_person_performed_examined.surname} " \
                                                                   f"{project.representative_person_performed_examined.name[0]}." \
                                                                   f"{project.representative_person_performed_examined.patronymic[0]}."

    # добавление инициалов представителей иных лиц
    if project.other_persons_participated_examination:
        if project.other_persons_participated_examination.patronymic == "":
            context['other_persons_participated_examination_name'] = f"{project.other_persons_participated_examination.surname} " \
                                                                     f"{project.other_persons_participated_examination.name[0]}."
        else:
            context['other_persons_participated_examination_name'] = f"{project.other_persons_participated_examination.surname} " \
                                                                 f"{project.other_persons_participated_examination.name[0]}." \
                                                                 f"{project.other_persons_participated_examination.patronymic[0]}."

    doc.render(context)
    path = os.path.join(base_path, 'documentation/new_act.docx')
    doc.save(path)

    return path, "new_act.docx"
