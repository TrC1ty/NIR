from django.db import models
from .ProjectModel import ProjectModel
from .WorkModel import WorkModel


class ProjectSection(models.Model):
    ParticipantType = (
        (1, 'Застройщик'),
        (2, 'Лицо, осуществляющее строительство'),
        (3, 'Лицо, осуществляющее подготовку проектной документации'),
        (4, 'Лицо, выполнившее работы, подлежащие освидетельствованию'),
        (5, 'Представитель застройщика'),
        (6, 'Представитель лица, осуществляющего строительство'),
        (7, 'Представитель лица, осуществляющего строительство, по вопросам строительного контроля'),
        (8, 'Представитель лица, осуществляющего подготовку проектной документации'),
        (9, 'Представитель лица, выполнившего работы, подлежащие освидетельствованию'),
        (10, 'Иные представители лиц, участвующих в освидетельствовании'),
    )
    id = models.BigAutoField(auto_created=True, primary_key=True)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    work = models.ForeignKey(WorkModel, on_delete=models.CASCADE)
    section_name = models.CharField(
        max_length=2,
        choices=ParticipantType,
    )

    class Meta:
        db_table = "ProjectSection"
