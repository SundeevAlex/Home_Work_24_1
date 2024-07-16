from django.db import models
from users.models import User

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    """
    Модель курса.
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    name = models.CharField(max_length=120, verbose_name="Название куса")
    image = models.ImageField(
        upload_to="materials/course/image", **NULLABLE, verbose_name="Изображение"
    )
    description = models.TextField(**NULLABLE, verbose_name="Описание курса")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """
    Модель урока.
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    name = models.CharField(max_length=150, verbose_name="Урок")
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Курс",
        related_name="lesson",
    )
    description = models.TextField(**NULLABLE, verbose_name="Описание урока")
    image = models.ImageField(
        upload_to="materials/lesson/image", **NULLABLE, verbose_name="Изображение"
    )
    link_to_video = models.CharField(
        max_length=150, **NULLABLE, verbose_name="Ссылка на видео"
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
