from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def login_view(request):
    return render_to_response('login.html')

def auth_view(request, onsuccess='/', onfail='/error'):
    user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect(onsuccess)
    else:
        return redirect(onfail)

def error_view(request):
    return render_to_response('error.html')

@login_required(login_url='/login/')
def index_view(request):
    # initialize
    return render_to_response("index.html")