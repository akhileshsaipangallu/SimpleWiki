# Django
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse


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
        context = {
            'user': request.user,
            'searchKey': searchKey,
        }
        return render(request, 'wiki/homePage.html', context)
