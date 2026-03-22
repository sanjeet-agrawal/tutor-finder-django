from django.shortcuts import render, redirect
from .forms import SignupForm, ProfileForm
from tutors.models import Tutor
from .models import Profile
from django.contrib.auth.decorators import login_required

def signup(request):

    if request.method == 'POST':

        form = SignupForm(request.POST)

        if form.is_valid():

            user = form.save()

            role = form.cleaned_data['role']

            Profile.objects.create(user=user, role=role)

            # if tutor, create tutor profile automatically
            if role == 'tutor':
                Tutor.objects.create(
                    user=user,
                    subject="Not set",
                    experience=0,
                    location="Not set",
                    hourly_rate=0,
                    bio="Update your profile"
                )

            return redirect('/login/')

    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    tutor = None
    try:
        tutor = Tutor.objects.get(user=request.user)
    except Tutor.DoesNotExist:
        pass

    context = {
        'profile': profile,
        'tutor': tutor
    }

    return render(request, 'accounts/profile.html', context)

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/edit_profile.html', {'form': form})