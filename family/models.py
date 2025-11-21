from django.db import models
import uuid
from django.contrib.auth.models import User

class Family(models.Model):
    familyId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="families")
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FamilyLog(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name="logs")
    date = models.DateTimeField()
    start_hour = models.CharField(max_length=10, blank=True, null=True)
    end_hour = models.CharField(max_length=10, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    signature = models.CharField(blank=True, null=True)

    def __str__(self):
        return f"{self.family.name} - {self.date}"
