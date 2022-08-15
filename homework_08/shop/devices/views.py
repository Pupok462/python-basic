from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from .models import Devices, DevicesType
from django.views.generic import ListView, DetailView


class DevicesListView(ListView):
    queryset = Devices.objects.select_related('type')
    template_name = 'devices/index.html'
    context_object_name = "devices"


class DevicesTypeListView(ListView):
    queryset = Devices.objects.select_related("type")
    context_object_name = "devices"

    def get_queryset(self):
        qs = super().get_queryset()
        type: DevicesType = get_object_or_404(
            DevicesType, name=self.kwargs["type_name"]
        )

        return qs.filter(type__name=type.name)


class DevicesDetailView(DetailView):
    queryset = Devices.objects.select_related('type')
    context_object_name = "device"
    template_name = "devices/details.html"
