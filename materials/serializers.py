from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


# class CourseDetailSerializer(ModelSerializer):
#     count_lesson_in_course = SerializerMethodField()
#
#     def get_count_lesson_in_course(self, course):
#         return Lesson.objects.filter(course=course).count()
#
#     class Meta:
#         model = Course
#         fields = ('name', 'description', 'image', 'count_lesson_in_course',)


class LessonSerializer(ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Lesson
        fields = "__all__"


class LessonDetailSerializer(ModelSerializer):
    count_lesson_in_course = SerializerMethodField()
    course = CourseSerializer()

    def get_count_lesson_in_course(self, lesson):
        return Lesson.objects.filter(course=lesson.course).count()

    class Meta:
        model = Lesson
        fields = ('name', 'course', 'description', 'count_lesson_in_course',)
