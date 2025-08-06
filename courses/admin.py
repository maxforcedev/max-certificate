from django.contrib import admin
from .models import Course, CourseCompetency


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'workload', 'description', 'is_active']


class CourseCompetencyAdmin(admin.ModelAdmin):
    list_display = ['course']


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseCompetency, CourseCompetencyAdmin)
