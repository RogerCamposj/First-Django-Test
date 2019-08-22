from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse(' ESSA É A HOME IRMÃO')
    # return render(request, 'notify/index.html')