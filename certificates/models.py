import uuid
from django.db import models
from unidecode import unidecode
from django.utils.timezone import now
from courses.models import Course
from django.utils import timezone
from datetime import timedelta


class Certificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    id_code = models.CharField(max_length=40, unique=True)
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='certificates')
    issued_at = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)
    pdf_file = models.FileField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id_code:
            date_str = now().strftime("%Y%m%d")
            course_name = unidecode(self.course.name)
            certificate_code = course_name[:4].upper().replace(" ", "")[:3]

            for i in range(1, 10000):
                id_code = f"{certificate_code}-{date_str}-{i:04d}"
                if not Certificate.objects.filter(id_code=id_code).exists():
                    self.id_code = id_code
                    break

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} – {self.course.name}"


class CertificateAccessCode(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=10)

    def __str__(self):
        return f"{self.email} – {self.code} – criado em {self.created_at.strftime('%H:%M')}"
