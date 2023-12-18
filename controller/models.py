from django.db import models

# Create your models here.


class Flavor(models.Model):
    title = models.CharField(max_length=50, unique=True)
    ingredient1 = models.CharField(max_length=50, unique=True)
    ingredient2 = models.CharField(max_length=50, unique=True)
    ingredient3 = models.CharField(max_length=50, unique=True)
    ingredient4 = models.CharField(max_length=50, unique=True)
    ingredient5 = models.CharField(max_length=50, unique=True)
    amount1 = models.IntegerField()
    amount2 = models.IntegerField()
    amount3 = models.IntegerField()
    amount4 = models.IntegerField()
    amount5 = models.IntegerField()

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