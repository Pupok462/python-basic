from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import DeviceCreateForm
from .models import Devices, DevicesType
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse


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


class DeviceDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Devices
    success_url = reverse_lazy("devices:devices-list")
    permission_required = (
        "devices.delete_devices",
        "devices.delete_laptop",
        "devices.delete_phone",
        "devices.delete_tablet",
    )


class DeviceCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Devices
    form_class = DeviceCreateForm
    permission_required = (
        "devices.add_devices",
        "devices.add_laptop",
        "devices.add_phone",
        "devices.add_tablet",
    )

    def get_success_url(self):
        return reverse("devices:details", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)
