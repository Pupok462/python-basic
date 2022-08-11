from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from devices.models import Tablet


def index(request: HttpRequest):
    tablets = Tablet.objects.order_by("id").all()
    context = {
        "tablets": tablets
    }
    return render(request, 'tablets/index.html', context=context)
