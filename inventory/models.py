from django.db import models

class UserRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    dob = models.DateField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.email
