from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

from .models import UserProfile, Comment


class UserEditForm(UserChangeForm):
    password = None

    class Meta:
        fields = ("username", "first_name", "last_name", "email",)
        model = get_user_model()
        widgets = {'password': forms.HiddenInput()}


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic', 'bio', 'location', 'occupation', 'linkedin', 'github', 'instagram', 'quote')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'email', 'comment')