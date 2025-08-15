from . import views
from django.urls import path


urlpatterns = [
    path("projects/",views.index),
    # path("projects/<int:pid>/",views.detail),
    path("projects/<int:pid>/",views.ProjectView.as_view()),
    path("myview/<int:pid>/",views.MyViewParmForReuqest.as_view())
]