import json

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render, redirect
from django.utils.encoding import escape_uri_path

from ..models.MaterialModel import MaterialModel
from ..forms.MaterialForm import Material


class MaterialView(View):
    @staticmethod
    def view_certificate(request: HttpRequest, material_id):
        material = MaterialModel.objects.get(id=material_id)

        response = HttpResponse(material.file_data)
        response['Content-Type'] = material.file_type
        response['Content-Disposition'] = "attachment; filename=" + escape_uri_path(material.file_name)

        return response

    @staticmethod
    def edit_material(request: HttpRequest, material_id, prev_page):
        material = MaterialModel.objects.get(id=material_id)

        if request.method == "POST":
            material_form = Material(request.POST)
            if material_form.is_valid():
                material.name = material_form.cleaned_data.get("name", "")
                material.count = material_form.cleaned_data.get("count", "")
                material.units_of_measurement = material_form.cleaned_data.get("units_of_measurement", "")
                material.provider = material_form.cleaned_data.get("provider", "")
                material.certificate_name = material_form.cleaned_data.get("certificate_name", "")
                material.certificate_number = material_form.cleaned_data.get("certificate_number", "")
                material.date_start = material_form.cleaned_data.get("date_start")
                material.date_end = material_form.cleaned_data.get("date_end")
                material.list_count = material_form.cleaned_data.get("list_count", "")

                material.save()
        else:
            material_form = Material(instance=material)

        if prev_page == 0:
            project_id = material.work.projectSection.project_id
            back_btn_name = "К проекту"
            back_btn = f"/projects/{project_id}"
            post_url = f"/materials/{material_id}/0"
        else:
            work_id = material.work_id
            back_btn_name = "К работе"
            back_btn = f"/works/{work_id}"
            post_url = f"/materials/{material_id}/1"

        data = {
            'back_btn': back_btn,
            'back_btn_name': back_btn_name,
            'form': material_form,
            'material': material,
            'post_url': post_url,
            'prev_page': prev_page
        }

        return render(request, 'materials/Edit.html', data)

    @staticmethod
    def delete_material(request: HttpRequest, material_id, prev_page):
        material = MaterialModel.objects.get(id=material_id)
        project_id = material.work.projectSection.project_id
        work_id = material.work_id
        material.delete()

        if prev_page == 0:
            return HttpResponseRedirect(f'/projects/{project_id}')
        else:
            return HttpResponseRedirect(f'/works/{work_id}')
