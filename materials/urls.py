from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import (LessonViewSet, LessonCreateAPIView,
                             LessonDestroyAPIView,
                             # LessonListAPIView,
                             LessonRetrieveAPIView, LessonUpdateAPIView, CourseListAPIView, CourseRetrieveAPIView,
                             CourseCreateAPIView, CourseDestroyAPIView, CourseUpdateAPIView, SubscribeCreateAPIView)

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'', LessonViewSet)

urlpatterns = [
                  path('courses/', CourseListAPIView.as_view(), name='courses_list'),
                  path('courses/<int:pk>/', CourseRetrieveAPIView.as_view(), name='courses_retrieve'),
                  path('courses/create/', CourseCreateAPIView.as_view(), name='courses_create'),
                  path('courses/delete/<int:pk>/', CourseDestroyAPIView.as_view(), name='courses_delete'),
                  path('courses/update/<int:pk>/', CourseUpdateAPIView.as_view(), name='courses_update'),
                  path('subscribe/', SubscribeCreateAPIView.as_view(), name='subscribe'),
              ] + router.urls
