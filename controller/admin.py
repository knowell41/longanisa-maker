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
