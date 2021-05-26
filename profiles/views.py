from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import Profile
from .forms import ProfileForm


@login_required
def profile_view(request):
    """
    add customers
    add products
    create positions
    create sales
    see profile details
    """
    profile_obj = Profile.objects.get(user=request.user)
    profile_form = ProfileForm(
        request.POST or None,
        request.FILES or None,
        instance=profile_obj
    )

    if profile_form.is_valid():
        profile_form.save()
        messages.success(request, f'your profile has been updated')

    context = {
        'profile_obj': profile_obj,
        'title': 'Profile',
        'profile_form': profile_form
    }
    return render(request, 'profile/home.html', context)
