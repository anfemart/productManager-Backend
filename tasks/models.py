from django.db import models

class Task(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Borrador"
        IN_PROGRESS = "IN_PROGRESS", "En progreso"
        REVIEW = "REVIEW", "En revisión"
        BLOCKED = "BLOCKED", "Bloqueada"
        COMPLETED = "COMPLETED", "Completada"

    class Priority(models.TextChoices):
        LOW = "LOW", "Baja"
        MEDIUM = "MEDIUM", "Media"
        HIGH = "HIGH", "Alta"
        CRITICAL = "CRITICAL", "Crítica"

    class ImplementationType(models.TextChoices):
        APEX = "APEX", "Apex"
        LWC = "LWC", "Lightning Web Component"
        FLOW = "FLOW", "Flow"
        CONFIG = "CONFIG", "Declarativo"
        INTEGRATION = "INTEGRATION", "Integración"
        METADATA = "METADATA", "Metadata"
        OTHER = "OTHER", "Otro"

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    client = models.CharField(max_length=255)
    project = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=20, choices=ImplementationType.choices)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.MEDIUM)
    tags = models.JSONField(default=list, blank=True)  # lista de etiquetas
    due_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
