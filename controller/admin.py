from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Flavor)
class FlavorAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "ingredient1",
        "ingredient2",
        "ingredient3",
        "ingredient4",
        "ingredient5",
        "amount1",
        "amount2",
        "amount3",
        "amount4",
        "amount5",
    ]


@admin.register(AppSettings)
class AppSettingsAdmin(admin.ModelAdmin):
    list_display = ["systemStatus"]


@admin.register(DeviceSettings)
class DeviceSettingsAdmin(admin.ModelAdmin):
    list_display = ["com", "baudrate", "timeout"]


@admin.register(Actuator)
class ActuatorAdmin(admin.ModelAdmin):
    list_display = [
        "condiment1",
        "condiment2",
        "condiment3",
        "condiment4",
        "condiment5",
        "grinder1",
        "grinder2",
        "grinder3",
        "grinder4",
        "mixer",
    ]
