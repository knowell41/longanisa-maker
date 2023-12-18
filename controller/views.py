from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ListFlavors(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FlavorSerializer
    queryset = Flavor.objects.all()


class RetrieveFlavor(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FlavorSerializer
    queryset = Flavor.objects.all()


class DeleteFlavor(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FlavorSerializer
    queryset = Flavor.objects.all()


class UpdateFlavor(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FlavorSerializer
    queryset = Flavor.objects.all()
    http_method_names = ["patch"]


class AppStatus(APIView):
    def get(self, request, *args, **kwargs):
        try:
            app_status = AppSettings.objects.get(id=1)
            return Response(app_status.systemStatus, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": f"{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
