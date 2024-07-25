from django.db import models

# from users.models import User
from config.settings import AUTH_USER_MODEL


NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    """
    Модель курса.
    """

    name = models.CharField(max_length=120, verbose_name="Название куса")
    image = models.ImageField(
        upload_to="materials/course/image", **NULLABLE, verbose_name="Изображение"
    )
    description = models.TextField(**NULLABLE, verbose_name="Описание курса")
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name="Владелец")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """
    Модель урока.
    """

    name = models.CharField(max_length=150, verbose_name="Урок")
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Курс",
        # related_name="lesson",
    )
    description = models.TextField(**NULLABLE, verbose_name="Описание урока")
    image = models.ImageField(
        upload_to="materials/lesson/image", **NULLABLE, verbose_name="Изображение"
    )
    link_to_video = models.CharField(
        max_length=150, **NULLABLE, verbose_name="Ссылка на видео"
    )
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name="Владелец")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscribe(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='Курс')
    sign_of_subscription = models.BooleanField(default=False, verbose_name='Признак подписки')

    def __str__(self):
        return f'{self.user}: ({self.course})'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
