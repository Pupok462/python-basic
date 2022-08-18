from django.contrib.auth.forms import UserCreationForm as CreationForm
from django.contrib.auth.forms import ValidationError
from .models import UserModel, UserProfile
from django.contrib.auth.forms import AuthenticationForm


class UserCreationForm(CreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "email", "password1", "password2")

    # def bad_username(self):
    #     username = self.cleaned_data.get('Meta.model.username')
    #     queryset = UserModel.objects.values_list('username', flat=True)
    #     qs = []
    #     for q in queryset:
    #         qs.append(q)
    #     if username in qs:
    #         raise ValidationError('Username is not unique')
    #     return username


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ("username", "password")

