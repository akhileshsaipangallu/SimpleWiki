# standard library
import re

# Django
from django import forms
from django.contrib.auth.models import User

# local Django
from .models import Post
from .models import UserProfile


def string_validation(data, field_name):
    for char in data:
        if not char.isalpha():
            raise forms.ValidationError(
                "Enter a valid %s name" % field_name
            )


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'viewPermissionLevel', 'editPermissionLevel']

    def clean_title(self):
        title = self.cleaned_data['title']
        if Post.objects.filter(title__iexact=title):
            raise forms.ValidationError("'%s' has already been taken" % title)
        return title

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].widget.attrs['class'] = 'form-control'
            self.fields[key].widget.attrs['placeholder'] = \
                self.fields[key].label
            self.fields[key].widget.attrs['id'] = self.fields[key].label


class EditPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'viewPermissionLevel', 'editPermissionLevel']

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if Post.objects.filter(title__iexact=title).exclude():
    #         raise forms.ValidationError("'%s' has already been taken" % title)
    #     return title

    def __init__(self, *args, **kwargs):
        super(EditPostForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].widget.attrs['class'] = 'form-control'
            self.fields[key].widget.attrs['placeholder'] = \
                self.fields[key].label
            self.fields[key].widget.attrs['id'] = self.fields[key].label


class EditUserForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['fullName', 'email', 'userLevel']

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].widget.attrs['class'] = 'form-control'
            self.fields[key].widget.attrs['placeholder'] = \
                self.fields[key].label
            self.fields[key].widget.attrs['id'] = self.fields[key].label


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
        data = self.cleaned_data['password2']
        data_password = self.cleaned_data['password1']
        if data != data_password:
            raise forms.ValidationError("Password mismatch")
        return data


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
        choices=[(x, x) for x in range(0, 5)],
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
        data = self.cleaned_data['username']
        if User.objects.filter(username=data):
            raise forms.ValidationError(
                "Username '%s' has already been taken" % data
            )
        return data

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
        data = self.cleaned_data['password2']
        data_password = self.cleaned_data['password1']
        if data != data_password:
            raise forms.ValidationError("Password mismatch")
        return data
