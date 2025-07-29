import traceback

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PredictiveMaintenance
from .serializers import PredictiveMaintenanceSerializer


# class PredictiveMaintenanceCreateView(generics.CreateAPIView):
#     queryset = PredictiveMaintenance.objects.all()
#     serializer_class = PredictiveMaintenanceSerializer


class PredictiveMaintenanceCreateView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            print("Received data:", request.data)
            serializer = PredictiveMaintenanceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            traceback.print_exc()
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)