from django.core.exceptions import ValidationError
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

    def clean_name(self):
        name_project = self.name_project
        print(name_project)
        if name_project != "1":
            raise ValidationError("Не 1")

        return name_project

    def change_participant(self, participant, column):
        match column:
            case "builder":
                self.builder = participant
            case "person_the_construction":
                self.person_the_construction = participant
            case "person_prepares_doc":
                self.person_prepares_doc = participant
            case "representative_builder":
                self.representative_builder = participant
            case "representative_person_the_construction":
                self.representative_person_the_construction = participant
            case "specialist_organization_construction":
                self.specialist_organization_construction = participant
            case "representative_person_preparing_project_doc":
                self.representative_person_preparing_project_doc = participant
            case "representative_person_performed_examined":
                self.representative_person_performed_examined = participant
            case "other_persons_participated_examination":
                self.other_persons_participated_examination = participant

        self.save()
