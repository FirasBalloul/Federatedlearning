from django.db import models

class ModelVersion(models.Model):
    version_number = models.PositiveIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    global_model_path = models.CharField(max_length=255, null=True, blank=True, default="media/global_model.pkl")  # Allow NULL and set a default path

    def __str__(self):
        return f"Model Version {self.version_number}"

class ClientSubmission(models.Model):
    model_version = models.ForeignKey(ModelVersion, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    performance_metric = models.FloatField()
    parameters = models.JSONField()

    def __str__(self):
        return f"Submission for Version {self.model_version.version_number}"
