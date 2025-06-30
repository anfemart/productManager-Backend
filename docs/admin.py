from django.contrib import admin
from .models import ImplementationDoc

@admin.register(ImplementationDoc)
class ImplementationDocAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "template_type",
        "task",
        "version",
        "updated_at",
    )
    list_filter = ("template_type",)
    search_fields = ("title", "content")
    ordering = ("-updated_at",)
