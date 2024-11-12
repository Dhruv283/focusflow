from django.db import models
from django.contrib.auth.models import User

# from django.utils import timezone
# current_datetime = timezone.now()
# today = current_datetime.date()

# Create your models here.
MODEL_CHOICES=[
    ('Not Completed','Not Completed'),('Completed','Completed'),
]
class Task(models.Model):
    Username=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField()
    taskname=models.TextField(max_length=100)
    taskpriority=models.CharField(max_length=25)
    status=models.CharField(choices=MODEL_CHOICES,default='Not Completed')