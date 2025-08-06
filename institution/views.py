from rest_framework.views import APIView
from rest_framework.response import Response
from .models import InstitutionSettings
from .serializers import InstitutionSerializer


class InstitutionSettingsView(APIView):
    def get(self, request):
        instance = InstitutionSettings.objects.first()
        if not instance:
            return Response({"detail": "Nenhum registro encontrado."}, status=404)
        serializer = InstitutionSerializer(instance)
        return Response(serializer.data)
