from . import views
from django.urls import path

urlpatterns = [
    path('', views.JobListView.as_view(), name='home'),
    path('add_job/', views.AddJobView.as_view(), name='add_job'),
    path('edit_job/<slug:slug>/', views.EditJobView.as_view(), name='edit_job'),
    path('delete_job/<slug:slug>/',
         views.DeleteJobView.as_view(), name='delete_job'),
    path('edit_dream_job/', views.EditDreamJobView.as_view(), name='edit_dream_job'),
    path('instructions/', views.InstructionsView.as_view(), name='instructions'),
]
