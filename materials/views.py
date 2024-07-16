from rest_framework import viewsets
from materials.serializers import CourseSerializer
from materials.models import Course


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
