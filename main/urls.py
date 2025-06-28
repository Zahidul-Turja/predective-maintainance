from django.urls import path
from .views import submit_device_data

urlpatterns = [
    path("submit/", submit_device_data, name="submit-device-data"),
]
