from rest_framework.test import APITestCase
from users.models import User
from materials.models import Course, Lesson, Subscribe
from django.urls import reverse
from rest_framework import status


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.course = Course.objects.create(name="Math", description="Good")
        self.lesson = Lesson.objects.create(name="Lesson1", description="test", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson-detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), self.lesson.name
        )

    def test_lesson_create(self):
        url = reverse("materials:courses_create")
        data = {
            "name": "test1"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        # self.assertEqual(
        #     Lesson.objects.filter(name="Lesson1").count(), 1
        # )
        self.assertEqual(
            Lesson.objects.all().count(), 1
        )

    def test_lesson_update(self):
        url = reverse("materials:lesson-detail", args=(self.lesson.pk,))
        data = {
            "name": "test1"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), "test1"
        )

    def test_lesson_delete(self):
        url = reverse("materials:courses_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse("materials:courses_list")
        response = self.client.get(url)
        data = response.json()
        # print(data)
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "name": self.lesson.name,
                    "image": None,
                    "description": self.lesson.description,
                    "owner": self.user.pk
                }
            ]
        }
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )


class SubscribeTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.course = Course.objects.create(name="test", description="test", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscribe(self):
        url = reverse("materials:subscribe")
        data = {"course": self.course.pk}
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {"message": "Подписка успешно добавлена."})

    def test_unsubscribe(self):
        url = reverse("materials:subscribe")
        data = {"course": self.course.pk}
        Subscribe.objects.create(course=self.course, user=self.user)
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {'message': 'Подписка успешно удалена.'})
