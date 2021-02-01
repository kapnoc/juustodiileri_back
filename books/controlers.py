from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.utils.translation import gettext as _


# @login_required(login_url='/users/login/')
def ocr_controler(request):
    context = {
        'title': _('OCR'),
    }
    return render(request, 'books/ocr.html', context)
