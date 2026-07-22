from django.urls import path
from .views import (
    JobListView,
    JobDetailView,
    JobCreateView,
    JobUpdateView,
    JobDeleteView,
    MyJobsListView,
    apply_to_job,
    MyApplicationsListView,
)

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('job/new/', JobCreateView.as_view(), name='job_create'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('job/<int:pk>/edit/', JobUpdateView.as_view(), name='job_update'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
    path('job/<int:pk>/apply/', apply_to_job, name='apply_to_job'),
    path('my-jobs/', MyJobsListView.as_view(), name='my_jobs'),
    path('my-applications/', MyApplicationsListView.as_view(), name='my_applications'),
]
