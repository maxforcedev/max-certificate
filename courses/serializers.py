from rest_framework import serializers
from .models import Course


class CourseReadSerializer(serializers.ModelSerializer):
    competencies = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'name', 'slug', 'workload', 'description', 'is_active', 'competencies']

    def get_competencies(self, obj):
        return [c.description for c in obj.competencies.all()]


class CourseSelectSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    hours = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['value', 'label', 'hours']

    def get_value(self, obj):
        return obj.slug

    def get_label(self, obj):
        return obj.name

    def get_hours(self, obj):
        return str(obj.workload)
