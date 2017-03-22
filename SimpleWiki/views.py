# Django
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse

# local Django
from wiki.models import UserProfile


def homePage(request):
    if request.method == 'POST':
        searchKey = request.POST['search']
        return HttpResponseRedirect(
            reverse(
                'searchResults',
                kwargs={
                    'searchKey': searchKey
                }
            )
        )

    else:
        searchKey = None
        userLevel = None
        if request.user.is_authenticated:
            userLevel = UserProfile.objects.get(user=request.user).userLevel
        context = {
            'userLevel': userLevel,
            'searchKey': searchKey,
        }
        return render(request, 'wiki/homePage.html', context)
