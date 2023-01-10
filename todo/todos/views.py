from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from todos.models import Userprofile
from .EmailBackend import EmailBackend
from .forms import *



def login_page(request):
    # check if user is already logged in
    if request.user.is_authenticated: return redirect(reverse("home"))
    
    # else redirect guest to login page
    return render(request, 'todos/login.html')

def doLogin(request, **kwargs):
    # On login data submittion
    if request.method != 'POST':
        return HttpResponse("<h4>Denied</h4>")
    else:
        # Get the user via authenticaticated email
        user = EmailBackend.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        
        # if user exists 
        if user != None: 
            # then login user
            login(request, user)
            
            # redirect user to home
            return redirect(reverse('home'))
        
        # else if user does not exits return error
        else: 
            messages.error(request, "Invalid details")
            return redirect("/")

def home(request):
    form = TodoForm()
    user = get_object_or_404(Userprofile, user=request.user)
    todos = Todo.objects.filter(user = user)
    context={
        'form': form,
        'todos': todos
    }
    
    if request.method == 'POST':
        if form.is_valid():
            try:
                obj = form.save(commit=False)
                obj.user = get_object_or_404(Userprofile, user=request.user)
                obj.save()
                messages.success(request, "Todo Saved Successfully")
                return redirect(reverse('home'))
            except Exception:
                messages.error(request, "Could not Submit!")
        else:
            messages.error(request, "Form has errors!")
    return render(request, 'todos/home.html', context)