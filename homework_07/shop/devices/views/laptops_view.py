from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from devices.models import Laptop


def index(request: HttpRequest):
    laptops = Laptop.objects.order_by("id").all()
    context = {
        "laptops": laptops
    }
    return render(request, 'laptops/index.html', context=context)
