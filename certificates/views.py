import random
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from . import models, serializers


class CertificateCreateView(CreateAPIView):
    queryset = models.Certificate.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.CertificateCreateSerializer
        return serializers.CertificateReadSerializer

    def perform_create(self, serializer):
        self.instance = serializer.save()

    def get_serializer_context(self):
        return {"request": self.request}

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        read_serializer = serializers.CertificateReadSerializer(self.instance, context=self.get_serializer_context())
        return Response(read_serializer.data)


@api_view(["GET"])
def validate_certificate(request):
    certificate_id = request.GET.get("id", "").upper()
    try:
        cert = models.Certificate.objects.get(id_code=certificate_id)
    except models.Certificate.DoesNotExist:
        return Response({"detail": "not_found"}, status=404)

    serializer = serializers.CertificateValidationSerializer(cert)
    return Response(serializer.data)


@api_view(["POST"])
def request_certificate_code(request):
    email = request.data.get("email")
    if not email:
        return Response({"detail": "Email obrigatório"}, status=400)

    if not models.Certificate.objects.filter(email=email, is_valid=True).exists():
        return Response({"detail": "Nenhum certificado válido encontrado para este e-mail."}, status=404)

    code = str(random.randint(100000, 999999))
    models.CertificateAccessCode.objects.filter(email=email).delete()
    models.CertificateAccessCode.objects.create(email=email, code=code)

    send_mail(
        subject="Seu código de acesso aos certificados",
        message=f"Seu código de verificação é: {code}",
        from_email="noreply@maxforcedev.com",
        recipient_list=[email],
    )

    return Response({"detail": "Código enviado com sucesso"})


@api_view(["POST"])
def my_certificates(request):
    email = request.data.get("email")
    code = request.data.get("code")

    try:
        access = models.CertificateAccessCode.objects.get(email=email, code=code)
        if access.is_expired():
            return Response({"detail": "Código expirado"}, status=400)

        certificates = models.Certificate.objects.filter(email=email)
        serializer = serializers.CertificateFrontendSerializer(certificates, many=True)
        return Response(serializer.data)

    except models.CertificateAccessCode.DoesNotExist:
        return Response({"detail": "Código inválido"}, status=400)
