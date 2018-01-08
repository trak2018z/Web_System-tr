"""
Definition of views.
"""

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from Account_app.forms import Edit_User_Form, SignUpForm
from Account_app.models import UserProfile


@login_required()
def view_profile(request):
    args = {'user': request.user}
    # return render(request, 'Account_app/account_view.html', args)
    return render(request, 'Account_app/view_form.html', args)


@login_required()
def edit_user(request):
    if request.method == 'POST':
        form = Edit_User_Form(request.POST or None, instance=request.user)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('Account_app:profile')
    else:
        form = Edit_User_Form(instance=request.user)
        args = {'form': form}
        return render(request, 'Account_app/user_form.html', args)


@method_decorator(login_required, name='dispatch')
class UserProfile_view(generic.ListView):
    model = UserProfile
    context_object_name = 'user_profile_list'
    template_name = 'Account_app/account_view.html'

    # model=UserProfile
    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class userCompanyUpdate(generic.UpdateView):
    model = UserProfile
    template_name = 'Account_app/userCompany_form.html'
    fields = ['telefon_firmy', 'nazwa_firmy', 'miasto_firmy', 'ulica_firmy', 'nr_firmy', 'kod_pocztowy_firmy',
              'nip_firmy']

    def get_success_url(self):
        return reverse_lazy('Account_app:profile')


@method_decorator(login_required, name='dispatch')
class userProfileUpdate(generic.UpdateView):
    model = UserProfile
    template_name = 'Account_app/userProfile_form.html'
    fields = ['nr_telefonu', 'ulica', 'nr_domu', 'miasto', 'kod_pocztowy']

    def get_success_url(self):
        return reverse_lazy('Account_app:profile')


@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('Account_app/account_view.html')
        else:
            return redirect('Account_app/change_password.html')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'Account_app/change_password.html', args)


def singup(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Account_app:login')

    else:
        form = SignUpForm()
        # form = UserCreationForm()

    return render(request, 'Account_app/singup.html', {'form': form})
