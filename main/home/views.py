from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile,Items


# Create your views here.
def homepage(request):
    queryset = Items.objects.all()
    return render(request, 'home.html', context={'items':queryset, 'page':'Home'})

@login_required
def profile(request):
    userprof = Profile.objects.get(user=request.user)
    queryset = Items.objects.filter(seller=userprof)
    context = {
        'items': queryset,
        'user': request.user,
        'profile':userprof,
        'page': 'Profile'
    }
    return render(request, 'profile.html', context)

@login_required
def additem(request):
    if request.method == 'POST':
        data =  request.POST
        item_name = data.get('item_name')
        item_cost = data.get('item_cost')
        item_img = request.FILES.get('item_img')
        userprof = Profile.objects.get(user=request.user)
        new_item = Items(seller=userprof, item_name=item_name, item_cost=item_cost, item_img=item_img)
        new_item.save()
        print("inside additem")  
        return redirect('/profile')
    return redirect('/profile')

@login_required
def deleteitem(request, id):
    item = Items.objects.get(id=id)
    if item.seller.user == request.user:
        item.delete()
        print("inside delete")
    return redirect('/profile')

def loginpage(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        print(username + " " + password)
        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid username")
            print("here")
            return redirect('/login/')
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, "Invalid Password")
            print("here")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/home/')        #actual redirect
    return render(request, 'login.html', context={'page':'Login'})

def signuppage(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        username = data.get('username')
        password = data.get('password')
        phone = data.get('phone')
        profile_img = request.FILES.get('profile_img')
        
        user = User.objects.filter(username = username)
        if user.exists():
                messages.error(request, "User already exists")
                return redirect('/signup/')
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        profile = Profile(
            user=user,
            name = name,
            phone = phone,
            profile_img = profile_img
        )
        profile.save()
        messages.success(request, "Account created Successfully")
        return redirect('/login/')

    return render(request, 'signup.html', context={'page':'Sign Up'})

def logoutpage(request):
    logout(request)
    return redirect('/login/')
    
