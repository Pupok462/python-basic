from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from devices.models import Phone


def index(request: HttpRequest):
    phones = Phone.objects.order_by("id").all()
    context = {
        "phones": phones
    }
    return render(request, 'phones/index.html', context=context)