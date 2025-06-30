from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "client",
        "project",
        "type",
        "status",
        "priority",
        "due_date",
        "updated_at",
    )
    list_filter = (
        "status",
        "priority",
        "type",
        "client",
        "project",
    )
    search_fields = ("title", "description", "client", "project")
    ordering = ("-updated_at",)
