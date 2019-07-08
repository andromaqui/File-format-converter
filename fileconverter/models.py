from converter.storage_backends import CsvStorage
from django.db import models
from django.utils import timezone
import time


class CSVUpload(models.Model):

    csv_file = models.FileField(storage=CsvStorage())
    
    def __str__(self):
        return self.csv_file
    
