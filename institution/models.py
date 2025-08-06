from django.db import models


class InstitutionSettings(models.Model):
    course_name = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18)
    ceo_name = models.CharField(max_length=150)
    website = models.URLField(blank=True, null=True)
    logo_img = models.ImageField(blank=True, null=True)
    discount_url = models.URLField(blank=True, null=True)
    group_students = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
