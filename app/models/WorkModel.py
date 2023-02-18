from django.db import models
from .BCARModel import BCARModel
from .ProjectModel import ProjectModel
from .MaterialModel import MaterialModel
from .LegalActModel import LegalActModel


class WorkModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    name_hidden_works = models.TextField()
    number_project_doc = models.TextField()
    number_working_doc = models.TextField()
    other_details_project_drawing = models.TextField()
    other_details_working_drawing = models.TextField()
    name_project_doc = models.TextField()
    name_working_doc = models.TextField()
    # todo: нужно ли разделить то поле на проектную и рабочую документацию
    information_persons_prepare_doc = models.TextField()
    submitted_doc = models.TextField()
    start_date_work = models.DateField()
    end_date_work = models.DateField(null=True)
    permitted_works = models.TextField()
    additional_information = models.TextField()
    number_instances = models.IntegerField(null=True)
    materials = models.ManyToManyField(MaterialModel)
    bcars = models.ManyToManyField(BCARModel)
    acts = models.ManyToManyField(LegalActModel)

    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "Works"
