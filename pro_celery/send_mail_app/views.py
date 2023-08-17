from django.shortcuts import render
from send_mail_app.tasks import send_mail_func
from django.http import HttpResponse
# Create your views here.


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")