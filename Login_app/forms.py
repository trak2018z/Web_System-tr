"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Password'}))

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2',)
        # class SignUpForm(UserCreationForm):
        #    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
        #    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
        #    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
        #    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

        #    class Meta:
        #        model = User
        #        fields = ('username', 'first_name', 'last_name','birth_date', 'email', 'password1', 'password2', )
        # class UserForm(forms.ModelForm):
        #    class Meta:
        #        model = User
        #        fields = ('first_name', 'last_name', 'email')

        # class ProfileForm(forms.ModelForm):
        #    class Meta:
        #        model = Profile
        #        fields = ('url', 'location', 'company')
