from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import connection
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password

def ProductView(request):
    if request.user.is_authenticated:
        return redirect('home')
    qs = Product.objects.all()
    context = {'qs':qs}
    return render(request,"cart/product.html",context)

def View(request,id):
    qs = Product.objects.get(id=id)
    return render(request,'cart/view.html',context={'qs':qs})

@login_required(login_url='/login')
def view_cart(request):
    cart_item = Cart.objects.filter(user=request.user)
    user = request.user
    total_price = sum(item.name.price * item.quantity for item in cart_item)
    return render(request,'cart/cart.html',context={'itm':cart_item,'price':total_price,'us':user})

@login_required(login_url='/login')
def add_to_cart(request,id):
    pro = Product.objects.get(id=id)
    cart_item, created = Cart.objects.get_or_create(name=pro,user=request.user)
    cart_item.quantity +=1
    cart_item.save()
    return redirect('cart')
def delete(request,id):
    qs = Cart.objects.get(id=id)
    qs.delete()
    return redirect('cart')
def inc(request,id):
    qs = Cart.objects.get(id=id)
    qs.quantity +=1
    qs.save()
    return redirect('cart')
def dec(request,id):
    qs = Cart.objects.get(id=id)
    if qs.quantity >=1:
        qs.quantity -=1
        qs.save()
    if qs.quantity ==0:
        qs.delete()
    return redirect('cart')

def Register(request):
    if request.method == "POST":
        Uname = request.POST.get('username')
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        pd = make_password(pwd)
        user = User(username=Uname,first_name=fname,last_name=lname,email=email,password=pd)
        user.save()
        group = Group.objects.get(name='User')
        user.groups.add(group)
    form = Userform()
    return render(request,'cart/register.html',context={'form':form})


def Login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')  
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "cart/login.html")

@login_required
def Home(request):
    qs = Product.objects.all()
    user = request.user
    qt = User.objects.get(username=user)
    context = {'qs':qs,'us':user}
    return render(request,"cart/home.html",context)

def Search(request):
    name = request.POST.get('name')
    qs = Product.objects.filter(name__icontains=str(name)).values()

    query = f"select * from cart_product where name like 'a%';"
    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
    return render(request,'cart/search.html',context={'qs':list(results)})

@login_required
def Logout(request):
    logout(request)
    return redirect('product')

def Addproduct(request):
    form = Productform()
    if request.method == 'POST':
        form = Productform(request.POST)
        if form.is_valid:
            form.save()
    return render(request,'cart/addpro.html',context={'form':form})
def sellerindex(request):
    return render(request,"seller/seller.html")
def sellerregister(request):
    if request.method == "POST":
        Uname = request.POST.get('username')
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        pwd = request.POST.get('password')

        user = User(username=Uname,first_name=fname,last_name=lname,email=email,password=pwd)
        user.save()
        group = Group.objects.get(name='Seller')
        user.groups.add(group)
    return render(request,"seller/sellerregister.html")
def SellerLogin(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')  
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "seller/login.html")