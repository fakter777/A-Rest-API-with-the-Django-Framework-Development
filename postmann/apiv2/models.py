from django.db import models
import uuid
# Create your models here.
class UsersAPI(models.Model):
    name = models.CharField(unique=False, max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(unique=False, max_length=50)



    def __str__(self):
        return self.email





