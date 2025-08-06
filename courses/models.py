import uuid
from django.db import models


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    workload = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CourseCompetency(models.Model):
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name="competencies")
    description = models.TextField()

    def __str__(self):
        return f"{self.course.name} – {self.description[:50]}"
