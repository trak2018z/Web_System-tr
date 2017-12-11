"""
Definition of views.
"""
from datetime import timezone

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpRequest
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.views import generic
from django.views.generic import TemplateView

from Account_magnament_app.forms import Edit_Profile_Form, SignUpForm, UserProfile_Form
from Account_magnament_app.models import UserProfile


def singup(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # user.save()

            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('login')

    else:
        form = SignUpForm()
        # form = UserCreationForm()

    return render(request, 'Account_magnament_app/singup.html', {'form': form})


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'Account_magnament_app/view_profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = Edit_Profile_Form(request.POST, isinstance=request.user)

        if form.is_valid():
            form.save()
            return redirect('Account_magnament_app/view_profile.html')
    else:
        form = Edit_Profile_Form(instance=request.user)
        args = {'form': form}
        return render(request, 'Account_magnament_app/view_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('Account_magnament_app/view_profile.html')
        else:
            return redirect('Account_magnament_app/change_password.html')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'Account_magnament_app/change_password.html', args)

class view_UserProfile(generic.DetailView):
    template_name = 'Account_magnament_app/Userprofileedit.html'
    model = UserProfile

    slug_field = 'username'
    # override the context user object from user to user_profile, use {{ user_profile }} instead of {{ user }} in template
    context_object_name = "user_profile"

    #def get_context_data(self, **kwargs):
     #   context=super(UserProfile,self).get_context_data(**kwargs)
      #  context['some_data']=UserProfile(self.object)
       # return context
