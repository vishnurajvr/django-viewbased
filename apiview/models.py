from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    mail = models.CharField(max_length=50)

    def __str__(self):
        return self.name
