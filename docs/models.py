from django.db import models

class ImplementationDoc(models.Model):
    DOC_TEMPLATES = [
        ("LWC", "Lightning Web Component"),
        ("APEX", "Apex Class/Trigger"),
        ("FLOW", "Flow"),
        ("CONFIG", "Configuración"),
        ("PERMISSION", "Permission Set"),
        ("METADATA", "Metadata"),
        ("OTHER", "Otro"),
    ]

    title = models.CharField(max_length=255)
    task = models.ForeignKey("tasks.Task", on_delete=models.CASCADE, related_name="docs", null=True, blank=True)
    template_type = models.CharField(max_length=50, choices=DOC_TEMPLATES)
    content = models.TextField()  # Markdown o texto enriquecido
    version = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} v{self.version}"
