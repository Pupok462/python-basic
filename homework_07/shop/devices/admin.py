from django.contrib import admin

from devices.models import Laptop, Phone, Tablet


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'model', 'price')
    list_display_links = ('id', 'company')


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'model', 'price')
    list_display_links = ('id', 'company')


@admin.register(Tablet)
class TabletAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'model', 'price')
    list_display_links = ('id', 'company')
