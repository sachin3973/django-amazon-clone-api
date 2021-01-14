from users.models import User
from django.db import models


class Address(models.Model):
    address_type = models.CharField(max_length=55, null=True)
    house_number = models.CharField(max_length=255, null=False)
    street = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=55, null=False)
    zip_code = models.CharField(max_length=55, null=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, default=None)

    def __str__(self):
        return self.address_type
