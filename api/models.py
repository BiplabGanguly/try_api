from django.db import models
import uuid

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_title = models.CharField(max_length=255)
    project_description = models.TextField()

    def __str__(self):
        return self.project_title


class Apidata(models.Model):
    HTTP_METHOD_CHOICES = [
        ('POST', 'POST'),
        ('GET', 'GET'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE'),
        ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_uuid = models.ForeignKey(Project, on_delete=models.CASCADE)
    api_method = models.CharField(max_length=10, choices=HTTP_METHOD_CHOICES)
    api_data = models.CharField(max_length=255)
    api_description = models.TextField()

    def __str__(self) -> str:
        return self.project_uuid.project_title