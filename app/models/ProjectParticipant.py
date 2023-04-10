from django.db import models
from .ProjectModel import ProjectModel
from .ParticipantModel import ParticipantModel


class ProjectParticipant(models.Model):
    ParticipantType = (
        (1, 'Застройщик'),
        (2, 'Лицо, осуществляющее строительство'),
        (3, 'Лицо, осуществляющее подготовку проектной документации'),
        (4, 'Лицо, выполнившее работы'),
        (5, 'Представитель застройщика'),
        (6, 'Представитель лица, осуществляющего строительство'),
        (7, 'Представитель лица, осуществляющего строительство, по вопросам строительного контроля'),
        (8, 'Представитель лица, осуществляющего подготовку проектной документации'),
        (9, 'Представитель лица, выполнившего работы, подлежащие освидетельствованию'),
        (10, 'Иные представители лиц, участвующих в освидетельствовании'),
    )
    id = models.BigAutoField(auto_created=True, primary_key=True)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    participant = models.ForeignKey(ParticipantModel, on_delete=models.CASCADE)
    participant_type = models.CharField(
        max_length=2,
        choices=ParticipantType,
    )

    class Meta:
        db_table = "ProjectParticipant"

    @staticmethod
    def get_all_participants(project):
        participants = ProjectParticipant.objects.filter(project=project).order_by('participant_type')
        data = {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None,
            10: None,
        }

        for participant in participants:
            data[participant.participant_type] = participant

        participant_data = {'Застройщик': data[1], 'Лицо, осуществляющее строительство': data[2],
                            'Лицо, осуществляющее подготовку проектной документации': data[3],
                            'Лицо, выполнившее работы': data[4], 'Представитель застройщика': data[5],
                            'Представитель лица, осуществляющего строительство': data[6],
                            'Представитель лица, осуществляющего строительство, по вопросам строительного контроля':
                                data[7],
                            'Представитель лица, осуществляющего подготовку проектной документации': data[8],
                            'Представитель лица, выполнившего работы, подлежащие освидетельствованию': data[9],
                            'Иные представители лиц, участвующих в освидетельствовании': data[10]}

        return participant_data
