from rest_framework import serializers
from .models import ModelVersion, ClientSubmission

class ModelVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelVersion
        fields = "__all__"

class ClientSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientSubmission
        fields = "__all__"
