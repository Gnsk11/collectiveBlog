from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='This field is required')

    class Meta:
        model = User
        fields = ('username', 'email', 'gender', 'date_of_birth', 'password1', 'password2',)
        help_texts = {
            'date_of_birth': "YYYY-MM-DD"
        }
