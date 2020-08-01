from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request,'base.html')

def quote_list(request):
    quoteList=quotes.objects.all()
    d={'quoteList':quoteList}
    return render(request,'quotes.html',d)