from django.urls import path
from .views import phone_index, tablet_index, laptop_index

app_name = 'devices'

urlpatterns = [
    path('phone/', phone_index, name='phone_list'),
    path('laptop/', laptop_index, name='laptop_list'),
    path('tablet/', tablet_index, name='tablet_list'),

]
