from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(null=False, unique=True, blank=False)
    phone_num = models.CharField(max_length=25)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.email
