from django.shortcuts import render
import json
import time
# Create your views here.

from django.http import JsonResponse
from django.db import connection


def indexrender(request):
    return render(request, "./vue-resources/dist/index.html")
