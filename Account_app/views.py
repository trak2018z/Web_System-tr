"""
Definition of views.
"""

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from Account_app.forms import Edit_Profile_Form, SignUpForm, UserProfile_Form
from Account_app.models import UserProfile


# działaja
def view_profile(request):
    args = {'user': request.user}
    # return render(request, 'Account_app/account_view.html', args)
    return render(request, 'Account_app/view_form.html', args)


@method_decorator(login_required, name='dispatch')
class UserProfile_view(generic.ListView):
    model = UserProfile
    context_object_name = 'user_profile_list'
    template_name = 'Account_app/account_view.html'

    # model=UserProfile
    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)


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
            # user.save()

            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)

            return redirect('Account_app:login')

    else:
        form = SignUpForm()
        # form = UserCreationForm()

    return render(request, 'Account_app/singup.html', {'form': form})


# do poprawy
def edit_profile(request):
    if request.method == 'POST':
        form = Edit_Profile_Form(request.POST, isinstance=request.user)

        if form.is_valid():
            form.save()
            return redirect('Account_app/account_view.html')
    else:
        form = Edit_Profile_Form(instance=request.user)
        args = {'form': form}
        return render(request, 'Account_app/account_view.html', args)


class userCompanyUpdate(generic.UpdateView):
    model = UserProfile
    form_class = UserProfile_Form
    success_url = reverse_lazy('Account_app:profile')
    template_name = 'Adres_app/adres_form.html'
    fields = ['company', 'company_city', 'company_street', 'company_nr', 'company_post_code', 'company_nip']


class userProfileUpdate(generic.UpdateView):
    model = UserProfile
    form_class = UserProfile_Form
    fields = ['phone', 'street', 'nr', 'city', 'post_code']
    success_url = reverse_lazy('Account_app:profile')
    template_name = 'Account_app/user_form.html'


@method_decorator(login_required, name='dispatch')
class UserUpdate(generic.UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'Account_app/user_form.html'

    def get_success_url(self):
        return reverse_lazy('Account_app:profile')

    def get_object(self):
        return self.request.user
