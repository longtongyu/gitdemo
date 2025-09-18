from . import views
from django.urls import path


urlpatterns = [
    # path("projects/<int:pid>/",views.detail),
    path("projects/",views.ProjectView.as_view()),
    path("projects/<int:pk>/",views.ProjectDetailView.as_view())
]