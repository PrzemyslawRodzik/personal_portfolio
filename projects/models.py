from django.utils import timezone
from django.db import models


# Create your models here.


class Project(models.Model):
    class Meta:
        db_table = 'project'

    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    #image = models.ImageField(upload_to='img/')
    image = models.FilePathField(path='img/')
    publication_date = models.DateTimeField(default=timezone.now)



