import base64

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core.files.base import ContentFile
from django.utils.crypto import get_random_string
from django import forms

from .models import User


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        new_user = User.objects.create_user(username, email, password)
        return JsonResponse({
            'success': True,
        })


def login_controler(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({
                'success': True,
            })
        return JsonResponse({
            'success': False,
        })


@login_required(login_url='/users/login/')
def test(request):
    return JsonResponse({
        'success': True,
    })


@login_required(login_url='/users/login/')
def profile(request):
    return JsonResponse({
        'success': True,
        'username': request.user.username,
    })


class AvatarUploadForm(forms.Form):
    image = forms.ImageField()


@login_required(login_url='/users/login/')
def avatar(request):
    if request.method == 'POST':
        form = AvatarUploadForm(request.POST, request.FILES)
        if form.is_valid():
            request.user.avatar = form.cleaned_data['image']
            request.user.save()
            return JsonResponse({
                'success': True,
            })
        return JsonResponse({
            'success': False,
        })
    elif request.method == 'GET':
        avatar = request.user.avatar
        return HttpResponseRedirect(avatar.url)
