from django.db import models

# Create your models here.

class UserDataModel(models.Model):
    user_id = models.CharField(max_length = 150, null= True)
    name = models.CharField(max_length = 150, null= True)
    roll_no = models.CharField(max_length = 150, null= True)
    marks = models.CharField(max_length = 150, null= True)