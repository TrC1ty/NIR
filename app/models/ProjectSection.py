from django.db import models
from .ProjectModel import ProjectModel


class ProjectSection(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    name = models.TextField()

    class Meta:
        db_table = "ProjectSection"
