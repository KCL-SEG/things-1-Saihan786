"""simple view"""

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    response = HttpResponse("<title>Things</title>")
    response.setdefault("h1", "Things")
    return response