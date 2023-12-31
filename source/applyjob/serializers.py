from .models import Job
from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    model = Job
    fields = '__all__'
    