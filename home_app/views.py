from django.views.generic import View
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.mixins import (
    PermissionRequiredMixin,
    LoginRequiredMixin
)
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import (
    login_required,
)

from plant_app.models import ANIMAL_INFLUENCE, AIR_PURIFYING, Category
from .models import UserProfile
from .form import AddUserForm, LoginForm, UserProfileForm, EditUserProfileForm, ResetPasswordForm


# Class for passing the context chosen data to HomeView app
class HomeView(View):

    def get(self, request):
        categories = Category.objects.all()
        influence = ANIMAL_INFLUENCE
        purifying = AIR_PURIFYING
        ctx = {'categories': categories,
               'influence': influence,
               'purifying': purifying
               }
        return render(request, 'home.html', ctx)


# Class for creating a view to AddUserForm, which allow to create User model, if it doesn't already exsists
class AddUserView(View):
    template_name = "home_app/add_user.html"

    def get(self, request):
        return render(request, self.template_name, {"form": AddUserForm})

    def post(self, request):
        form = AddUserForm(request.POST)
        logged_user = request.user.username
        if logged_user:
            messages.success(request, "Posiadasz już konto!")
            return render(request, self.template_name, {"form": form})
        elif form.is_valid():
            form.save()
            messages.success(request, "Użytkownik zarejestrowany pomyślnie! Zaloguj się, żeby korzystać z serwisu.")
            return redirect("login")
        else:
            messages.success(request, "Problem z rejestracją użytkownika. Spróbuj ponownie")
            return render(request, self.template_name, {"form": form})


# Class for creating a view for User login, which allow to create User model, if it doesn't already exsists
class LoginView(View):
    template_name = "home_app/login.html"

    def get(self, request):
        return render(request, self.template_name, {"form": LoginForm})

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)  # authentication
        if user:  # user.is_authenticated
            login(request, user)  # login

            next_url = request.GET.get("next")
            if next_url:
                return redirect(next_url)  # redirects to next page after login
            return redirect('/')
        else:
            messages.error(request, "Coś poszło nie tak. Spróbuj ponownie.")
            return render(request, self.template_name, {"form": LoginForm})


# Log out funtion for logged users
@login_required  # requirement for user, that he needs to be logged in
def log_out(request):
    logout(request)
    return redirect("home-view")


# Class View for creating a UserProfile for each user on the basis of UserProfileForm, and adding permissions
class CreateProfileView(LoginRequiredMixin, View):
    template_name = "home_app/userprofile_form.html"
    permission_required = "home_app.add_userprofile", "admin.change_user"

    def get(self, request):
        logged_user = request.user.username
        user = User.objects.get(username=logged_user)
        form = UserProfileForm(initial={'first_name': user.first_name,
                                        'last_name': user.last_name,
                                        'email': user.email
                                        })
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES)  # request.FILES allows to save images by Form
        if form.is_valid():
            logged_user = request.user.username
            user = User.objects.get(username=logged_user)
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone = form.cleaned_data["phone"]
            email = form.cleaned_data["email"]
            picture = form.cleaned_data["picture"]
            if phone.isdigit():   # checking if phone number is a digit
                new_userprofile = UserProfile.objects.create(
                    user=user,
                    phone=phone,
                    picture=picture,
                )
                new_userprofile.user = user
                new_userprofile.save()
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.save()
                change_userprofile = Permission.objects.get(codename='change_userprofile')
                change_user = Permission.objects.get(codename='change_user')
                view_user = Permission.objects.get(codename='view_user')
                view_userprofile = Permission.objects.get(codename='view_userprofile')
                user.user_permissions.add(change_userprofile)  # automatically added permissions to User with Userprofile
                user.user_permissions.add(view_user)
                user.user_permissions.add(view_userprofile)
                user.user_permissions.add(change_user)
                user.save()
                return redirect('my-profile')
            messages.error(request,
                           "Problem z edycją profilu użytkownika. Spróbuj ponownie. Pamiętaj że numer telefonu musi być liczbą")
        return render(request, self.template_name, {'form': form})


# Class View for editing UserProfile for logged users and users with needed permissions
class EditProfileView(PermissionRequiredMixin, LoginRequiredMixin, View):
    template_name = "home_app/user_profile_edit.html"
    permission_required = "home_app.change_userprofile"


    def get(self, request):
        logged_user = request.user.username
        user = User.objects.get(username=logged_user)
        form = EditUserProfileForm(initial={'first_name': user.first_name,  # set's up initial User data
                                            'last_name': user.last_name,
                                            'phone': user.userprofile.phone,
                                            'email': user.email,
                                            'picture': user.userprofile.picture
                                            })
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EditUserProfileForm(request.POST, request.FILES)
        logged_user = request.user.username
        user = User.objects.get(username=logged_user)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone = form.cleaned_data["phone"]
            email = form.cleaned_data["email"]
            picture = form.cleaned_data["picture"]
            user.userprofile.phone = phone
            if phone.isdigit():  # checking if phone number is a digit
                user.userprofile.save()
            else:
                messages.error(request, "Numer telefonu nie został zmieniony! Numer musi składać się z samych cyfr")
            if picture:
                user.userprofile.picture = picture
                user.userprofile.save()
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            return redirect('my-profile')
        form = EditUserProfileForm(initial={'first_name': user.first_name,
                                            'last_name': user.last_name,
                                            'phone': user.userprofile.phone,
                                            'email': user.email,
                                            'picture': user.userprofile.picture
                                            })
        return render(request, self.template_name, {'form': form})


# Class View for viewing UserProfile on the basis of his objecst data
class UserProfileView(LoginRequiredMixin, View):
    template_name = "home_app/user_profile.html"
    permission_required = "home_app.view_userprofile", "admin.view_user"

    def get(self, request):
        logged_user = request.user.username
        user = User.objects.get(username=logged_user)
        ctx = {
            'user': user
        }
        return render(request, self.template_name, ctx)


# Class View that allows to reset the password added to account for logged users
class ResetPasswordView(LoginRequiredMixin, View):
    template_name = "home_app/reset_password.html"

    # def handle_no_permission(self):
    #     print("Logged this call")
    #     return super().handle_no_permission()

    def get(self, request):
        logged_user = request.user.username
        user = User.objects.get(username=logged_user)
        if not user:
            raise Http404
        return render(request, self.template_name, {"form": ResetPasswordForm})

    def post(self, request):
        form = ResetPasswordForm(request.POST)
        logged_user = request.user.username
        user = User.objects.get(username=logged_user)
        if form.is_valid():
            password = form.cleaned_data["password1"]
            user.set_password(password)
            user.save()

            messages.success(request, "Hasło zmienione")
            return redirect("login")
        else:
            messages.error(request, "Hasła do siebie nie pasują.")
            return render(request, self.template_name, {"form": form})