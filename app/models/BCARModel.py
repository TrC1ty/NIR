from django.db import models


class BCARModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    name = models.TextField()

    class Meta:
        db_table = "BCARs"
