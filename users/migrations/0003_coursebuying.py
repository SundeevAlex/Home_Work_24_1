# Generated by Django 5.0.7 on 2024-07-29 07:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0006_subscribe"),
        ("users", "0002_payments"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseBuying",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.PositiveIntegerField(verbose_name="Сумма оплаты")),
                (
                    "session_id",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="ID сессии"
                    ),
                ),
                (
                    "link",
                    models.URLField(
                        blank=True,
                        max_length=400,
                        null=True,
                        verbose_name="Ссылка на оплату",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.course",
                        verbose_name="Курс",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Покупка курса",
                "verbose_name_plural": "Покупки курсов",
            },
        ),
    ]
