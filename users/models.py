from django.contrib.auth.models import AbstractUser
from django.db import models
from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Еmail")
    phone = models.CharField(
        max_length=35, verbose_name="Телефон", blank=True, null=True
    )
    city = models.CharField(max_length=35, verbose_name="Город", blank=True, null=True)
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="Аватар", blank=True, null=True
    )
    # token = models.CharField(max_length=100, verbose_name='Токен', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payments(models.Model):
    METHOD_CHOISES = [
        ('CASH', 'Наличные'),
        ('TRAN', 'Перевод')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_of_pay = models.DateField(auto_now=True, verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', blank=True, null=True)
    amount = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    method = models.CharField(max_length=4, choices=METHOD_CHOISES)

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return self.user


class CourseBuying(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс',
    )
    amount = models.PositiveIntegerField(
        verbose_name='Сумма оплаты',
    )
    session_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='ID сессии',
    )
    link = models.URLField(
        max_length=400,
        blank=True,
        null=True,
        verbose_name='Ссылка на оплату',
    )
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )

    class Meta:
        verbose_name = 'Покупка курса'
        verbose_name_plural = 'Покупки курсов'

    def __str__(self):
        return f'Курс: {self.course.name}, пользователь: {self.user.email}, сумма: {self.amount} RUB.'
