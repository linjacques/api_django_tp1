from django.db import models

class ResourceLog(models.Model):
    user = models.CharField(max_length=100)
    # nom du fichier, dossier, table, etc.
    resource = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} accessed {self.resource} at {self.timestamp}"
