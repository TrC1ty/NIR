from django.db import models


class BCARModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    code_of_rules_number = models.TextField()
    name = models.TextField()

    class Meta:
        db_table = "BCARs"
