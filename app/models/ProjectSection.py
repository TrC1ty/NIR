from django.db import models
from .ProjectModel import ProjectModel
from .WorkModel import WorkModel


class ProjectSection(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    work = models.ForeignKey(WorkModel, on_delete=models.CASCADE)
    section_name = models.TextField()

    class Meta:
        db_table = "ProjectSection"
