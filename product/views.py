
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def htmlview(request):
    return render(request,'index.htm')