from django.db import models

# Create your models here.
class logDetails(models.Model):
    msg_type = models.CharField(max_length=200)
    msg_content = models.CharField(max_length=200)
    msg_date = models.DateTimeField('date published')
