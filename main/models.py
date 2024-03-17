from django.db import models
from django.utils import timezone

from users.models import CustomUser as User


class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.calories} calories"
