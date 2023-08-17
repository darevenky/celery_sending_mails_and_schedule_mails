from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from pro_celery import settings

@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    for a in users:
        subject = 'celery mail'
        message = 'sending mails through the celery'
        to_email = a.email

        send_mail(
            subject = subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=False,
        )
    return 'done'