from django.utils import timezone
from django.db import models


# Create your models here.


class Project(models.Model):
    class Meta:
        db_table = 'project'

    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='img/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



