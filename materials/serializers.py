from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson, Subscribe
from materials.validators import YouTubeLinkValidator


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [YouTubeLinkValidator(fields='link_to_video')]


class LessonDetailSerializer(ModelSerializer):
    count_lesson_in_course = SerializerMethodField()
    course = CourseSerializer()

    def get_count_lesson_in_course(self, lesson):
        return Lesson.objects.filter(course=lesson.course).count()

    class Meta:
        model = Lesson
        fields = ('name', 'course', 'description', 'count_lesson_in_course',)


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ("sign_of_subscription",)
