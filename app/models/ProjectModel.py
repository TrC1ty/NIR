from django.db import models
from app.models.ParticipantModel import ParticipantModel
from django.forms.models import model_to_dict


class ProjectModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    builder = models.ForeignKey(ParticipantModel, on_delete=models.SET_NULL, null=True, related_name="builder")
    person_the_construction = models.ForeignKey(ParticipantModel, on_delete=models.SET_NULL, null=True,
                                                related_name="construction")
    person_prepares_doc = models.ForeignKey(ParticipantModel, on_delete=models.SET_NULL, null=True,
                                            related_name="document")
    representative_builder = models.ForeignKey(ParticipantModel, on_delete=models.SET_NULL, null=True,
                                               related_name="part_represent_builder")
    representative_person_the_construction = models.ForeignKey(ParticipantModel, on_delete=models.SET_NULL, null=True,
                                                               related_name="represent_construction")
    specialist_organization_construction = models.ForeignKey(ParticipantModel, on_delete=models.SET_NULL, null=True,
                                                             related_name="organize_construction")
    representative_person_preparing_project_doc = models.ForeignKey(ParticipantModel, on_delete=models.SET_NULL,
                                                                    null=True, related_name="represent_document")
    representative_person_performed_examined = models.ForeignKey(ParticipantModel, on_delete=models.SET_NULL, null=True,
                                                                 related_name="represent_examined")
    other_persons_participated_examination = models.ForeignKey(ParticipantModel, on_delete=models.SET_NULL, null=True,
                                                               related_name="other_examined")
    name_project = models.TextField()
    name_project_documentation = models.TextField()
    building_address = models.TextField()
    date = models.DateTimeField()
    number_document = models.TextField()

    class Meta:
        db_table = "Projects"
