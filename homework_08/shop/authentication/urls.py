from django.urls import path
from .views import UserCreationView, UserProfileView, LoginView, LogoutView

app_name = 'authentication'

urlpatterns = [
    path('register/', UserCreationView.as_view(), name='register'),
    path('<int:pk>/profile/', UserProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]