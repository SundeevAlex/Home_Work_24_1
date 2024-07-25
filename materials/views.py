from rest_framework import generics, viewsets

from materials.models import Course, Lesson, Subscribe
from materials.serializers import CourseSerializer, LessonSerializer, LessonDetailSerializer, SubscribeSerializer
# , CourseDetailSerializer
from users.permissions import IsModers, IsOwner
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from materials.paginations import CustomPagination


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return LessonDetailSerializer
        return LessonSerializer

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (~IsModers,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModers | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (~IsModers | IsOwner,)
        return super().get_permissions()


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomPagination

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return CourseDetailSerializer
    #     return CourseSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~IsModers, IsAuthenticated,)


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModers | IsOwner,)


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModers | IsOwner,)


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner | ~IsModers,)


class CourseCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, ~IsModers, IsOwner]

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()


class CourseListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsModers | IsOwner]
    pagination_class = CustomPagination


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsModers | IsOwner]


class CourseUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsModers | IsOwner]


class CourseDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class SubscribeCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Subscribe.objects.all()

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course")
        course = get_object_or_404(Course, pk=course_id)
        subs_item = Subscribe.objects.filter(user=user, course=course)

        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка успешно удалена.'
        else:
            Subscribe.objects.create(user=user, course=course, sign_of_subscription=True)
            message = 'Подписка успешно добавлена.'
        return Response({"message": message})
