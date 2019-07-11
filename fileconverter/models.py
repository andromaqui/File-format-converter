from converter.storage_backends import CsvStorage
from django.db import models
from django.utils import timezone
import time
import os,uuid


def path_and_rename(instance, filename):
    filename = str(instance.id) + ".csv"
    return filename


class CSVUpload(models.Model):

    csv_file = models.FileField(upload_to=path_and_rename, storage=CsvStorage())
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return self.csv_file
    
