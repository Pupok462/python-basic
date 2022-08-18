from django.urls import path
from .views import DevicesListView, DevicesTypeListView, DevicesDetailView, DeviceDeleteView, DeviceCreateView


app_name = 'devices'

urlpatterns = [
    path('', DevicesListView.as_view(), name='devices-list'),
    path('<int:pk>/', DevicesDetailView.as_view(), name='details'),
    path('create/', DeviceCreateView.as_view(), name='create'),
    path('<str:type_name>/', DevicesTypeListView.as_view(), name='type-list'),
    path('<int:pk>/delete/', DeviceDeleteView.as_view(), name='delete')
]



