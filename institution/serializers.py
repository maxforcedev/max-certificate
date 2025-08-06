from rest_framework import serializers
from .models import InstitutionSettings


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutionSettings
        fields = ['course_name', 'cnpj', 'ceo_name', 'website', 'discount_url', 'group_students']
