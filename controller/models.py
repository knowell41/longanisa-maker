from django.db import models

# Create your models here.


class DeviceSettingsManager(models.Manager):
    def get_or_create_singleton(self):
        obj, created = self.get_or_create(pk=1)
        return obj


class Actuator(models.Model):
    condiment1 = models.CharField(max_length=2)
    condiment2 = models.CharField(max_length=2)
    condiment3 = models.CharField(max_length=2)
    condiment4 = models.CharField(max_length=2)
    condiment5 = models.CharField(max_length=2)
    grinder1 = models.CharField(max_length=2)
    grinder2 = models.CharField(max_length=2)
    grinder3 = models.CharField(max_length=2)
    grinder4 = models.CharField(max_length=2)
    mixer = models.CharField(max_length=2)


class DeviceSettings(models.Model):
    com = models.CharField(max_length=20)
    baudrate = models.IntegerField()
    timeout = models.FloatField(default=1)

    objects = DeviceSettingsManager()

    def __str__(self):
        return self.com

    class Meta:
        verbose_name = "Device Settings"


class Flavor(models.Model):
    title = models.CharField(max_length=50, primary_key=True)
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
