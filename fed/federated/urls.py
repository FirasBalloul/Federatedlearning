from django.urls import path
from .views import home, dashboard, submit_results

urlpatterns = [
    path("", home, name="home"),  # Home page
    path("dashboard/", dashboard, name="dashboard"),  # Dashboard page
    path("submit/", submit_results, name="submit_results"),  # Submission endpoint
]
