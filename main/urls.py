from django.urls import path
from .views import PredictiveMaintenanceCreateView

urlpatterns = [
    path(
        "submit/",
        PredictiveMaintenanceCreateView.as_view(),
        name="submit-device-data",
    ),
]
