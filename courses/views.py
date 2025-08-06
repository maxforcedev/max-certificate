from rest_framework.generics import ListAPIView
from .serializers import CourseReadSerializer, CourseSelectSerializer
from .models import Course


class CourseListView(ListAPIView):
    serializer_class = CourseReadSerializer
    queryset = Course.objects.filter(is_active=True)


class CourseSelectListView(ListAPIView):
    serializer_class = CourseSelectSerializer
    queryset = Course.objects.filter(is_active=True)
    ordering = ['-name']
