from django.db import models


class PdfModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    file_type = models.TextField()
    file_data = models.BinaryField()

    class Meta:
        db_table = "Pdfs"
