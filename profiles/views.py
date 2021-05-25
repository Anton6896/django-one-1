from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from profiles.models import Profile


@login_required
def profile_view(request):
    """
    add customers
    add products
    create positions
    create sales
    see profile details
    """

    context = {
        'profile': Profile.objects.get(user=request.user),
        'title': 'Profile'
    }
    return render(request, 'profile/home.html', context)
