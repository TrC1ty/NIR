from django.db import models
from app.models.ParticipantModel import ParticipantModel
from django.forms.models import model_to_dict


class ProjectModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    builder = models.ForeignKey(ParticipantModel, on_delete=models.SET_NULL)
    person_the_construction = models.ForeignKey(ParticipantModel, on_delete=models.SET_NULL)
    person_prepares_doc = models.ForeignKey(ParticipantModel, on_delete=models.SET_NULL)
    representative_builder = models.ForeignKey(ParticipantModel, on_delete=models.SET_NULL)
    representative_person_the_construction = models.ForeignKey(ParticipantModel, on_delete=models.SET_NULL)
    specialist_organization_construction = models.ForeignKey(ParticipantModel, on_delete=models.SET_NULL)
    representative_person_preparing_project_doc = models.ForeignKey(ParticipantModel, on_delete=models.SET_NULL)
    representative_person_performed_examined = models.ForeignKey(ParticipantModel, on_delete=models.SET_NULL)
    other_persons_participated_examination = models.ForeignKey(ParticipantModel, on_delete=models.SET_NULL)
    name_project = models.TextField()
    name_project_documentation = models.TextField()
    building_address = models.TextField()
    date_act = models.DateField()
    number_document = models.DateField()

    class Meta:
        db_table = "Projects"
