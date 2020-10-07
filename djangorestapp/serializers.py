
from rest_framework import serializers
from djangorestapp.models import Project

class ProjectsListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ["id","name"]

class CreateProjectSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 10)

    def create_user(self):
        data = self.validated_data
        return Project.objects.create(name = data["name"])