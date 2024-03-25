from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ['full_name', 'username', 'email', 'password1', 'password2', 'user_type']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username or Email', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username or Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            return cleaned_data

class ResolveDisputeForm(forms.Form):
    resolution = forms.CharField(label='Resolution', widget=forms.Textarea)