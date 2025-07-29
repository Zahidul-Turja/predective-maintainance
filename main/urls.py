from django.urls import path
from main.views import *

urlpatterns = [
    path(
        "submit/",
        PredictiveMaintenanceCreateView.as_view(),
        name="submit-device-data",
    ),
    path(
        "insights/", PredictiveMaintenanceCreateView.as_view(), name="device-insights"
    ),
]
