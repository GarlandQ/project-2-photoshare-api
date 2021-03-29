from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from photoshare import utils
from .forms import SignUpForm, ProfileUpdateForm, UserUpdateForm
from .models import Profile


# Create your views here.
@utils.anonymous_required
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            Profile(user=user).save()

            return HttpResponseRedirect(reverse('index'))

        return render(request, 'users/signup.html', {'form': form})

    return render(request, 'users/signup.html', {'form': SignUpForm()})


@utils.anonymous_required
def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return HttpResponseRedirect(reverse('index'))

        return render(request, 'users/login.html', {'form': form})


    return render(request, 'users/login.html', {'form': AuthenticationForm()})


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required
def profile_view(request, username):
    profile = get_object_or_404(Profile, user__username__iexact=username)

    return render(request, 'users/profile.html', {
        'profile': profile,
    })


def edit_profile_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return HttpResponseRedirect(reverse('profile', args=[request.user.username]))

        return render(request, 'users/edit_profile.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })

    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
