from django.db import models
from app.models.participant import ParticipantModel
from django.forms.models import model_to_dict


class ProjectModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    builder = models.ForeignKey(ParticipantModel)
    person_the_construction = models.ForeignKey(ParticipantModel)
    person_prepares_doc = models.ForeignKey(ParticipantModel)
    representative_builder = models.ForeignKey(ParticipantModel)
    representative_person_the_construction = models.ForeignKey(ParticipantModel)
    specialist_organization_construction = models.ForeignKey(ParticipantModel)
    representative_person_preparing_project_doc = models.ForeignKey(ParticipantModel)
    representative_person_performed_examined = models.ForeignKey(ParticipantModel)
    other_persons_participated_examination = models.ForeignKey(ParticipantModel)
    name_project = models.TextField()
    name_project_documentation = models.TextField()
    building_address = models.TextField()
    date_act = models.DateField()
    number_document = models.DateField()

    class Meta:
        db_table = "project_model"
