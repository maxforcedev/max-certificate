from rest_framework import serializers
from courses.models import Course
from .models import Certificate
from institution.models import InstitutionSettings


class CertificateCreateSerializer(serializers.ModelSerializer):
    course = serializers.SlugRelatedField(slug_field='slug', queryset=Course.objects.all())

    class Meta:
        model = Certificate
        fields = ['full_name', 'email', 'course']

    def validate(self, data):
        email = data['email'].lower()
        course = data['course']
        existing = Certificate.objects.filter(email=email, course=course).first()

        if existing:
            if existing.course.workload == course.workload:
                existing_comps = set(c.description for c in existing.course.competencies.all())
                current_comps = set(c.description for c in course.competencies.all())

                if existing_comps == current_comps:
                    raise serializers.ValidationError("Já existe um certificado emitido com os mesmos dados para este curso.")
        return data


class CertificateReadSerializer(serializers.ModelSerializer):
    course = serializers.CharField(source='course.name')
    workload = serializers.IntegerField(source='course.workload')
    competencies = serializers.SerializerMethodField()

    class Meta:
        model = Certificate
        fields = ['full_name', 'email', 'course', 'workload', 'issued_at', 'id_code', 'competencies']

    def get_competencies(self, obj):
        return [c.description for c in obj.course.competencies.all()]


class CertificateValidationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="full_name")
    course = serializers.CharField(source="course.name")
    hours = serializers.SerializerMethodField()
    issueDate = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    issuer = serializers.SerializerMethodField()
    cnpj = serializers.SerializerMethodField()
    competencies = serializers.SerializerMethodField()
    id = serializers.CharField(source="id_code")

    class Meta:
        model = Certificate
        fields = ["id", "name", "course", "hours", "issueDate", "status", "issuer", "cnpj", "competencies"]

    def get_hours(self, obj):
        return str(obj.course.workload)

    def get_status(self, obj):
        return "valid" if obj.is_valid else "invalid"

    def get_issuer(self, obj):
        settings = InstitutionSettings.objects.first()
        return settings.ceo_name if settings else ""

    def get_cnpj(self, obj):
        settings = InstitutionSettings.objects.first()
        return settings.cnpj if settings else ""

    def get_issueDate(self, obj):
        return obj.issued_at.strftime("%d/%m/%Y")

    def get_competencies(self, obj):
        if obj.course and hasattr(obj.course, "competencies"):
            return [comp.description for comp in obj.course.competencies.all()]
        return []


class CertificateFrontendSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="id_code")
    studentName = serializers.CharField(source="full_name")
    course = serializers.CharField(source="course.name")
    issueDate = serializers.SerializerMethodField()
    hours = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Certificate
        fields = ["id", "studentName", "course", "issueDate", "hours", "status"]

    def get_hours(self, obj):
        return str(obj.course.workload)

    def get_status(self, obj):
        return "active" if obj.is_valid else "expired"

    def get_issueDate(self, obj):
        return obj.issued_at.strftime("%d/%m/%Y")
