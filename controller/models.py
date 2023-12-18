from django.db import models

# Create your models here.


class Flavor(models.Model):
    title = models.CharField(max_length=50, unique=True)
    ingredient1 = models.CharField(max_length=50, null=True, blank=True)
    ingredient2 = models.CharField(max_length=50, null=True, blank=True)
    ingredient3 = models.CharField(max_length=50, null=True, blank=True)
    ingredient4 = models.CharField(max_length=50, null=True, blank=True)
    ingredient5 = models.CharField(max_length=50, null=True, blank=True)
    amount1 = models.FloatField(null=True, blank=True)
    amount2 = models.FloatField(null=True, blank=True)
    amount3 = models.FloatField(null=True, blank=True)
    amount4 = models.FloatField(null=True, blank=True)
    amount5 = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title


class AppSettings(models.Model):
    STATUS_CHOICES = [
        ("STOPPED", "STOPPED"),
        ("RUNNING", "RUNNING"),
    ]
    systemStatus = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default="STOPPED"
    )

    def __str__(self):
        return self.systemStatus
