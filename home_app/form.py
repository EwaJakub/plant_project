from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Class Form for creating new User object
class AddUserForm(UserCreationForm):

    # Class Meta for creating a form
    class Meta:
        model = User
        fields = (
            "username", "first_name", "last_name", "email", "password1", "password2"
        )

    def __init__(self, *args, **kwargs):  # inheritance
        super().__init__(*args, **kwargs)

        for field_name in ("username", "password1", "password2"):
            self.fields[field_name].help_text = None    # hides default hints to fill each field

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get("username")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        user = User.objects.filter(username=username).first()
        if user:
            self.add_error("username", "Użytkowik o podanym loginie już istnieje.")

        if password1 != password2:
            self.add_error("password2", "Hasła w obu polach muszą być jednakowe.")

        return cleaned_data


# Class Form for login User
class LoginForm(AuthenticationForm):

    class Meta:
        model = User


# Class Form for creating UserProfile objects
class UserProfileForm(forms.Form):
    first_name = forms.CharField(label='Imię:', max_length=200)
    last_name = forms.CharField(label='Nazwisko:', max_length=200)
    phone = forms.CharField(label='Telefon:', max_length=12, required=False)
    email = forms.CharField(label='email', max_length=200)
    picture = forms.ImageField(label='zdjęcie', required=False)  # pip install pillow -- YT user model


# Class Form for UserProfile editing
class EditUserProfileForm(forms.Form):
    first_name = forms.CharField(label='Imię:', max_length=200)
    last_name = forms.CharField(label='Nazwisko:', max_length=200)
    phone = forms.CharField(label='Telefon:', max_length=12, required=False)
    email = forms.CharField(label='email', max_length=200)
    picture = forms.ImageField(label='zdjęcie', required=False)


# Class Form for Password changing
class ResetPasswordForm(forms.Form):
    password1 = forms.CharField(label='Hasło', max_length=255, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło', max_length=255, widget=forms.PasswordInput)

    # Checking data added to form
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            self.add_error("password2", "Hasła nie pasują.")
        return cleaned_data