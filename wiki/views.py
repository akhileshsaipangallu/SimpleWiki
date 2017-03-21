# Django
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render
from django.shortcuts import reverse
from django.contrib.auth.models import User

# local Django
from .forms import ChangePasswordForm
from .forms import CreateUserForm
from .forms import EditPostForm
from .forms import EditUserForm
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
def createUser(request):
    userLevel = get_object_or_404(UserProfile, user=request.user).userLevel
    if userLevel != 5:
        return HttpResponseRedirect(reverse('error'))
    else:
        formObj = CreateUserForm()
        if request.method == 'POST':
            formObj = CreateUserForm(request.POST)
            if formObj.is_valid():
                user = User.objects.create_user(
                    username=formObj.cleaned_data['username'],
                    password=formObj.cleaned_data['password1'],
                    email=formObj.cleaned_data['email']
                )
                user.save()
                userProfileObj = UserProfile.objects.create(
                    user=user,
                    username=formObj.cleaned_data['username'],
                    email=formObj.cleaned_data['email'],
                    fullName=formObj.cleaned_data['fullName'],
                    userLevel=formObj.cleaned_data['userLevel'],
                    lastUpdatedBy=request.user,
                )
                userProfileObj.save()
                return HttpResponseRedirect(reverse('homePage'))
        context = {
            'formObj': formObj,
        }
        return render(request, 'wiki/createUser.html', context)


@login_required
def selectUser(request):
    userLevel = get_object_or_404(UserProfile, user=request.user).userLevel
    if userLevel != 5:
        return HttpResponseRedirect(reverse('error'))
    else:
        userList = UserProfile.objects.all()
        context = {
            'userList': userList,
        }
        return render(request, 'wiki/selectUser.html', context)


@login_required
def editUser(request, username):
    userLevel = get_object_or_404(UserProfile, user=request.user).userLevel
    if userLevel != 5:
        return HttpResponseRedirect(reverse('error'))
    else:
        userObj = get_object_or_404(UserProfile, username=username)

        if request.method == 'POST':
            formObj = EditUserForm(request.POST, instance=userObj)

            if formObj.is_valid():
                userObj.lastUpdatedBy = request.user
                userObj.save()
                return HttpResponseRedirect(reverse('selectUser'))
        else:
            formObj = EditUserForm(
                initial={
                    'fullName': userObj.fullName,
                    'email': userObj.email,
                    'userLevel': userObj.userLevel,
                }
            )

        context = {
            'formObj': formObj,
            'userObj': userObj,
        }
        return render(request, 'wiki/editUser.html', context)


@login_required
def changePassword(request, username):
    userLevel = get_object_or_404(UserProfile, user=request.user).userLevel
    if userLevel != 5:
        return HttpResponseRedirect(reverse('error'))
    else:
        userObj = get_object_or_404(UserProfile, username=username).user
        username = get_object_or_404(UserProfile, username=username).username
        form = ChangePasswordForm()

        if request.method == 'POST':
            form = ChangePasswordForm(request.POST)

            if form.is_valid():
                password = form.cleaned_data['password1']
                userObj.set_password(password)
                userObj.save()
                return HttpResponseRedirect(reverse('selectUser'))

        context = {
            'form': form,
        }
        return render(request, 'wiki/changePassword.html', context)


@login_required
def deleteUser(request, username):
    userLevel = get_object_or_404(UserProfile, user=request.user).userLevel
    if userLevel != 5:
        return HttpResponseRedirect(reverse('error'))
    else:
        userObj = get_object_or_404(UserProfile, username=username).user
        userObj.delete()
        return HttpResponseRedirect(reverse('selectUser'))


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
        query_set = Post.objects.filter(title__contains=searchKey)
        if not query_set:
            empty = True
        context = {
            'post_obj': query_set,
            'empty': empty,
            'searchKey': searchKey,
            'user': request.user,
        }
        return render(request, 'wiki/searchResults.html', context)


@login_required
def viewPage(request, title):
    editable = False
    viewable = False
    post_obj = get_object_or_404(Post, title=title)
    userLevel = get_object_or_404(UserProfile, user=request.user).userLevel

    if userLevel >= post_obj.viewPermissionLevel:
        viewable = True

    if not viewable:
        return HttpResponseRedirect(reverse('error'))
    elif userLevel >= post_obj.editPermissionLevel:
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
        formObj = EditPostForm(request.POST, instance=postObj)

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
        formObj = EditPostForm(instance=postObj)

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
        formObj = PostForm(
            initial={
                'title': title,
            }
        )
    context = {'formObj': formObj}
    return render(request, 'wiki/createPage.html', context)
