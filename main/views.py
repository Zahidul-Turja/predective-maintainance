from rest_framework import generics
from .models import PredictiveMaintenance
from .serializers import PredictiveMaintenanceSerializer


class PredictiveMaintenanceCreateView(generics.CreateAPIView):
    queryset = PredictiveMaintenance.objects.all()
    serializer_class = PredictiveMaintenanceSerializer
