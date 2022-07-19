from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.cache import cache_control



# Create your views here.



def index(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password =password  )

        if user is not None:
            auth.login(request , user)
            return redirect('/home')    
        else:
            messages.info(request, 'invalid username or password')
            return redirect("/")
    else:
        return render(request,'index.html')


def register(request):

    if request.method == 'POST':

        email = request.POST['email']
        username = request.POST['username']
        password= request.POST['password']


        user = User.objects.create_user(username = username , password = password , email = email)
        user.save()
        print('user created')
        return redirect('/custom')

    return render(request,'register.html')
 
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@login_required
def custom(request):
    return render(request, 'custom.html')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@login_required
def home(request):
    return render(request, 'home.html')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def logout(request):
    auth.logout(request)
    return redirect('/')
