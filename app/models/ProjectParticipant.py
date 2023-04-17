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
        projectParticipants = ProjectParticipant.objects.filter(project=project).order_by('participant_type')
        data = {
            1: [None],
            2: [None],
            3: [None],
            4: [None],
            5: [None],
            6: [None],
            7: [None],
            8: [None],
            9: [None],
            10: [None],
        }

        for projectParticipant in projectParticipants:
            participant = ParticipantModel.objects.get(id=projectParticipant.participant_id)
            data[int(projectParticipant.participant_type)] = [participant]

        data[1].append('Застройщик')
        data[2].append('Лицо, осуществляющее строительство')
        data[3].append('Лицо, осуществляющее подготовку проектной документации')
        data[4].append('Лицо, выполнившее работы')
        data[5].append('Представитель застройщика')
        data[6].append('Представитель лица, осуществляющего строительство')
        data[7].append('Представитель лица, осуществляющего строительство, по вопросам строительного контроля')
        data[8].append('Представитель лица, осуществляющего подготовку проектной документации')
        data[9].append('Представитель лица, выполнившего работы, подлежащие освидетельствованию')
        data[10].append('Иные представители лиц, участвующих в освидетельствовании')

        return data
