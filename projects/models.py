from django.db import models
import uuid


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    demo_link = models.CharField(max_length=2000, blank=True, null=True)
    source_link = models.CharField(max_length=2000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)  # Unique identifier for each project , we use editable=False to prevent it from being changed after creation

    def __str__(self):
        return self.title # String representation of the model, returns the title of the project

    class Meta:
        ordering = ['-created_at']  # Order by creation date, newest first
