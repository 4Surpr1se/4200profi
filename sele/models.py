from django.db import models

# Create your models here.


class Submission(models.Model):
    title = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    work_cutting = models.BooleanField()
    work_griding = models.BooleanField()
    work_filling = models.BooleanField() # todo SmallIntegerField OR BooleanField in MYSQL
    comments = models.TextField()
    responsible = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    submitted_at = models.TimeField(auto_now=True)
    status = models.BooleanField(default=False)
