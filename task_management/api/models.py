from django.db import models
from django.utils import timezone
from rest_framework.serializers import ValidationError

class User(models.Model):
    name = models.CharField(max_length=255)    
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Completed", "Completed"),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    due_date = models.DateTimeField()

    def clean(self):
        if self.due_date <= timezone.now():
            raise ValidationError('Due date must be in future')
    
    def __str__(self):
        return self.title
    