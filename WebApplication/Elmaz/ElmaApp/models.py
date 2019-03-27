from django.db import models

# Create your models here.
class Messages(models.Model):
    name = models.CharField(max_length=20,null=True)
    email = models.EmailField(max_length=20,null=True)
    subject = models.CharField(max_length=20, default='')
    message = models.TextField(null=True)

    def __str__(self):
        return self.name

