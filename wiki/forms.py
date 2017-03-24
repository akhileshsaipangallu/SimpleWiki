# standard library
import re

# Django
from django import forms
from django.contrib.auth.models import User

# local Django
from .models import Post
from .models import UserProfile


# form to create a page, can add Title, Content, View Permission Level and
# Edit Permission Level. Title should be unique
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title', 'content', 'viewPermissionLevel', 'editPermissionLevel'
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Title',
                    'id': 'title',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter content here',
                    'id': 'content',
                }
            ),
            'viewPermissionLevel': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'viewPermissionLevel',
                }
            ),
            'editPermissionLevel': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'editPermissionLevel',
                }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if Post.objects.filter(title__iexact=title):
            raise forms.ValidationError("'%s' has already been taken" % title)
        return title


# form to edit a page, can edit Title, Content, View Permission Level and
# Edit Permission Level. Title should be unique
class EditPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title', 'content', 'viewPermissionLevel', 'editPermissionLevel'
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Title',
                    'id': 'title',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter content here',
                    'id': 'content',
                }
            ),
            'viewPermissionLevel': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'viewPermissionLevel',
                }
            ),
            'editPermissionLevel': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'editPermissionLevel',
                }
            ),
        }


# form to edit User details, can edit Full Name, Email and User Level
class EditUserForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['fullName', 'email', 'userLevel']
        widgets = {
            'fullName': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Full Name',
                    'id': 'fullName',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'email',
                    'id': 'email',
                }
            ),
            'userLevel': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'userLevel',
                }
            ),
        }


# form to change User password
class ChangePasswordForm(forms.Form):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'id': 'password1',
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password',
                'id': 'password2',
            }
        )
    )

    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        password1 = self.cleaned_data['password1']
        if password2 != password1:
            raise forms.ValidationError("Password mismatch")
        return password2


# form to create a new User with username, Full Name, Email, User Level
# and Password
class CreateUserForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'id': 'username',
            }
        )
    )
    fullName = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Full Name',
                'id': 'fullname',
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'id': 'email',
            }
        )
    )
    userLevel = forms.ChoiceField(
        choices=[(x, x) for x in range(0, 6)],
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'User Level',
                'id': 'userlevel',
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'id': 'password1',
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password',
                'id': 'password2',
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError(
                "Username '%s' has already been taken" % username
            )
        return username

    def clean_fullName(self):
        fullName = self.cleaned_data['fullName']
        pattern = re.compile(r"^([a-zA-Z\s]{1,})$")
        if not pattern.match(fullName):
            raise forms.ValidationError("Invalid Full Name")
        return fullName

    def clean_email(self):
        email = self.cleaned_data['email']
        pattern = re.compile(r"^([a-zA-Z0-9.-]{1,})\@(\w{1,}\.(\w{1,}))$")
        if not pattern.match(email):
            raise forms.ValidationError("Invalid Email ID")
        return email

    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        password1 = self.cleaned_data['password1']
        if password2 != password1:
            raise forms.ValidationError("Password mismatch")
        return password2
