from django.db import models

# Create your models here.
class FileUpload(models.Model):
      data_file = models.FileField(upload_to='documents/%Y/%m/%d')
