from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request,'search.html')

def quote_list(request):
    quoteList=quotes.objects.all()
    d={'quoteList':quoteList}
    return render(request,'quotes.html',d)

def author_list(request):
    authorList=authors.objects.all()
    d={'authorList':authorList}
    return render(request,'authorList.html',d)