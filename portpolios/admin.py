from django.contrib import admin
from . import models


@admin.register(models.PortpoliosModel)
class PortpoliosAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "url",
    )

    filter_horizontal = ("participants",)
