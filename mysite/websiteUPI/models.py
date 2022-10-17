from django.db import models

# Create your models here.
class upiModel(models.Model):
    
    file = models.FileField(upload_to='upload/', null=True,)
    description = models.TextField()