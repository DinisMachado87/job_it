from . import views
from django.urls import path

urlpatterns = [
    path('', views.JobListView.as_view(), name='home'),
]
