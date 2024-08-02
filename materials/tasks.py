from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from materials.models import Course, Subscribe
from users.models import User
import datetime
import pytz


@shared_task
def hi(pk):
    print("HELLO1")


@shared_task
def send_notification(pk):
    course = Course.objects.get(pk=pk)
    subscription = Subscribe.objects.filter(course_id=pk, sign_of_subscription=True)
    users_id_list = []
    if subscription:
        for el in subscription:
            users_id_list.append(el.user_id)
        if users_id_list:
            user_email = []
            for item in users_id_list:
                email = User.objects.get(pk=item).email
                user_email.append(email)
            send_mail(
                subject=f"Внимание, обновление!",
                message=f"В курсе '{course.title}' произошли изменения.",
                from_email=EMAIL_HOST_USER,
                recipient_list=user_email,
            )


@shared_task
def checking_login():
    # today = datetime.datetime.now().date()
    # print(today)
    users = User.objects.filter(is_active=True)
    if users.exists():
        for user in users:
            if datetime.datetime.now(pytz.timezone('Asia/Novosibirsk')) - user.last_login > datetime.timedelta(weeks=4):
                user.is_active = False
                user.save()
