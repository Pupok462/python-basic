from django.contrib import admin
from .models import Devices, DevicesType


@admin.register(Devices)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'model', 'price', 'type')
    list_display_links = ('id', 'company')


admin.site.register(DevicesType)



