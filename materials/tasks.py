from celery import shared_task


@shared_task
def hi(pk):
    print("HELLO1")
