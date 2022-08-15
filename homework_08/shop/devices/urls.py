from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import DevicesListView, DevicesTypeListView, DevicesDetailView


app_name = 'devices'

urlpatterns = [
    path('', DevicesListView.as_view(), name='devices-list'),
    path('<int:pk>/', DevicesDetailView.as_view(), name='details'),
    path('<str:type_name>/', DevicesTypeListView.as_view(), name='type-list'),
]



