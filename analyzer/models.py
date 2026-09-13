from django.db import models


class CodeSubmission(models.Model):
    title = models.CharField(max_length=200, default="")
    purpose = models.TextField(default="")
    code = models.TextField()
    language = models.CharField(max_length=50, default="python")
    analysis_result = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"{self.language} submission #{self.pk}"
