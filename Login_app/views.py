"""
Definition of views.
"""

from django.contrib.auth import login, authenticate
from django.http import HttpRequest
from django.shortcuts import render, redirect

from Login_app.forms import SignUpForm

def singup(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()


            # user.refresh_from_db()
            # user.profile.birth_date = form.cleaned_data.get('birth_date')
            # user.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')

    else:
        form = SignUpForm()

    return render(
        request, 'Login_app/singup.html', {'form': form})

    # @login_required
    # @transaction.atomic
    # def update_profile(request):
    #    if request.method == 'POST':
    #        user_form = UserForm(request.POST, instance=request.user)
    #        profile_form = ProfileForm(request.POST, instance=request.user.profile)
    #        if user_form.is_valid() and profile_form.is_valid():
    #            user_form.save()
    #            profile_form.save()
    #            messages.success(request, _('Your profile was successfully updated!'))
    #            return redirect('settings:profile')
    #        else:
    #            messages.error(request, _('Please correct the error below.'))
    #    else:
    #        user_form = UserForm(instance=request.user)
    #        profile_form = ProfileForm(instance=request.user.profile)
    #    return render(request, 'profiles/profile.html', {
    #        'user_form': user_form,
    #        'profile_form': profile_form
    #    })

    # return render(request, 'signup.html', {'form': form})
