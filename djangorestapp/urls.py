from django.urls import path
from djangorestapp.views import ProjectView

urlpatterns = [
	path('v1/projects/', ProjectView.as_view(), name = "projects"),
]