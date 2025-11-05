from django.db import models


class Family(models.Model):
    familyId = models.CharField(max_length=100, unique=True)
    userId = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FamilyLog(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name="logs")
    date = models.DateField()
    start_hour = models.CharField(max_length=10, blank=True, null=True)
    end_hour = models.CharField(max_length=10, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    signature = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.family.name} - {self.date}"
