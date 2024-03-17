from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    height = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def calculate_bmi(self):
        """
        Calculate the BMI (Body Mass Index) based on the user's height and weight.
        BMI formula: weight (kg) / (height (m))^2
        """
        if self.height and self.weight:
            height_in_meters = self.height / 100  # Convert height from cm to meters
            bmi = self.weight / (height_in_meters ** 2)
            return round(bmi, 2)
        else:
            return None

    def __str__(self):
        return self.username
