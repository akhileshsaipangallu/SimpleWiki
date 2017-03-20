# Django
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render
from django.shortcuts import reverse

# local Django
from .models import Post
from .forms import PostForm
from .models import UserProfile


def error(request):
    return render(request, 'wiki/error.html')


@login_required
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('homePage'))


@login_required
def searchResults(request, searchKey):
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
        empty = False
        searchKey = searchKey
        # userLevel = get_object_or_404(UserProfile, user=request.user).userLevel
        query_set = Post.objects.filter(title__contains=searchKey)
        if not query_set:
            empty = True
        context = {
            'post_obj': query_set,
            'empty': empty,
            'searchKey': searchKey,
            'user': request.user,
            # 'userLevel': userLevel,
        }
        return render(request, 'wiki/searchResults.html', context)


@login_required
def viewPage(request, title):
    editable = False
    viewable = False
    post_obj = get_object_or_404(Post, title=title)
    userLevel = get_object_or_404(UserProfile, user=request.user).userLevel

    if userLevel > post_obj.viewPermissionLevel:
        viewable = True

    if not viewable:
        return HttpResponseRedirect(reverse('error'))
    elif userLevel > post_obj.editPermissionLevel:
        editable = True

    context = {
        'post_obj': post_obj,
        'user': request.user,
        'editable': editable,
    }
    return render(request, 'wiki/viewPage.html', context)


@login_required
def editPage(request, title):
    postObj = get_object_or_404(Post, title=title)
    if request.method == 'POST':
        formObj = PostForm(request.POST, instance=postObj)

        if formObj.is_valid():
            postObj.save()
            return HttpResponseRedirect(
                reverse(
                    'viewPage',
                    kwargs={
                        'title': formObj.cleaned_data['title']
                    }
                )
            )

    else:
        formObj = PostForm(instance=postObj)

    context = {
        'formObj': formObj,
        'postObj': postObj,
    }
    return render(request, 'wiki/editPage.html', context)


@login_required
def createPage(request, title):
    if request.method == 'POST':
        formObj = PostForm(request.POST)

        if formObj.is_valid():
            instance = formObj.save()
            instance.save()
            return HttpResponseRedirect(
                reverse(
                    'viewPage',
                    kwargs={
                        'title': formObj.cleaned_data['title']
                    }
                )
            )

    else:
        formObj = PostForm()
    context = {'formObj': formObj}
    return render(request, 'wiki/createPage.html', context)
