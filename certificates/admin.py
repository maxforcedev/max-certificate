from django.contrib import admin
from .models import Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "course", "id_code", "issued_at", "is_valid"]
    list_editable = ["is_valid"]
    search_fields = ["full_name", "email", "id_code"]
    list_filter = ["course", "is_valid", "issued_at"]
    readonly_fields = ["id_code", "created_at", "updated_at"]

    fieldsets = (
        (None, {
            "fields": ("full_name", "email", "course", "id_code", "is_valid")
        }),
        ("Datas", {
            "fields": ("created_at", "updated_at"),
        }),
    )
