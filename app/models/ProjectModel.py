from django.core.exceptions import ValidationError
from django.db import models
from app.models.ParticipantModel import ParticipantModel
from django.forms.models import model_to_dict


class ProjectModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    name_project = models.TextField()
    name_project_documentation = models.TextField()
    building_address = models.TextField()
    date = models.DateTimeField()
    project_code = models.TextField()

    class Meta:
        db_table = "Projects"

    def get_attributes(self):
        attributes = {
            "Наименование проектной документации": self.name_project_documentation,
            "Адрес объекта строительства": self.building_address,
            "Шифр проекта": self.project_code,
            "Дата": self.date
        }

        return attributes
