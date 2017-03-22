# Django
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse

# local Django
from wiki.models import UserProfile


def homePage(request):
    try:
        searchKey = request.GET['search']
        return HttpResponseRedirect(
            reverse(
                'searchResults',
                kwargs={
                    'searchKey': searchKey
                }
            )
        )

    except Exception:
        searchKey = None
        userLevel = None
        if request.user.is_authenticated:
            userLevel = UserProfile.objects.get(user=request.user).userLevel
        context = {
            'userLevel': userLevel,
            'searchKey': searchKey,
        }
        return render(request, 'wiki/homePage.html', context)
