from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Studentdetails(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE, default="")
    student_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10)
    percentage = models.IntegerField()
    backlogs = models.IntegerField()


class Placements(models.Model):
    img = models.ImageField(upload_to="img/%y", null=True)
    eng = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    per = models.IntegerField()
    backlog = models.IntegerField()