from django.contrib import admin
from .models import InstitutionSettings


@admin.register(InstitutionSettings)
class InstitutionSettingsAdmin(admin.ModelAdmin):
    list_display = ("course_name", "cnpj", "ceo_name", "website", "discount_url", "group_students", "created_at")
    search_fields = ("course_name", "ceo_name", "cnpj")
    readonly_fields = ("created_at",)
