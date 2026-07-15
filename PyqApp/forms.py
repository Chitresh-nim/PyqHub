from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields =[
            'username',
            'email',
            'password1',
            'password2',
        ]
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("an account with this email already exists.")
        return email

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    