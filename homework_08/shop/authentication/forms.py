from django.contrib.auth.forms import UserCreationForm as CreationForm
from .models import UserModel


class UserCreationForm(CreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "email", "password1", "password2")


