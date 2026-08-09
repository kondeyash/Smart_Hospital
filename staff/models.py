from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Unknown Doctor")
    age = models.IntegerField(null=True, blank=True)
    specialization = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    shift = models.CharField(max_length=50)

    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Unknown Staff")
    role = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=10,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other'),
        ],
        null=True,
        blank=True
    )
    age = models.IntegerField(null=True, blank=True)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} - {self.role}"
