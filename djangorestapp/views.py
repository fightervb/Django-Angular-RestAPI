from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response
from djangorestapp.models import Project
from rest_framework import status
from djangorestapp.serializers import ProjectsListSerializer, CreateProjectSerializer 

class ProjectView(APIView):

    def get(self, request):
        projects = Project.objects.all()

        data = ProjectsListSerializer(
                    projects,
                    many = True
                ).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        create_project_serializer = CreateProjectSerializer(data = request.data)

        if create_project_serializer.is_valid():
            created_user = create_project_serializer.create_user()
            return Response({"message": "User created successfully"}, status = status.HTTP_200_OK)
        else:
            return Response(create_project_serializer.errors, status.HTTP_400_BAD_REQUEST)