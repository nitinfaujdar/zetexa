from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assigned_user', 'status', 'due_date']

    def validate_due_date(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError("Due Date is in future")
        return value