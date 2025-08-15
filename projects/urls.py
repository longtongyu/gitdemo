from . import views
from django.urls import path


urlpatterns = [
    path("projects/",views.index),
    path("include/",views.index),
    path("projects/<int:ids>/",views.detail)
]