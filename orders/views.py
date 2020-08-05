from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from django.db import IntegrityError
from django.core.mail import send_mail


# Create your views here.
from .models import Pizza, Topping, Sub, Pasta, Salad, DinnerPlatter, CustomerOrder, Extra

# Landing Page
def index(request):
    return render(request, 'orders/index.html')

# Register
def register(request):
    # POST from page
    if request.method == "POST":
        # Call the function and pass in the info from the post data
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password2 != password1:
            messages.error(request, "Password does not match or invalid")
            return render(request, 'orders/login.html')
        # Check if username is taken
        try:
            user = User.objects.create_user( request.POST['username'], request.POST['email'], password2)
        except IntegrityError:
            messages.error(request, "Username is taken")
            return render(request, 'orders/login.html')
        # Get user's First and Last name
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.save()
        messages.success(request, "Account created for " + request.POST['username'])
        return redirect('login')
    else:
        # GET request, render the register page
        return render(request, 'orders/register.html')

# Log in page, make sure to not name the view "login" because login() is a django function
def loginPage(request):
    # POST from page
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, password=password, username=username)

        if user is not None :
            login(request, user)
            return redirect('menu')
        else:
            messages.error(request, "Log in failed")
            return redirect('login')
    else:
        # GET request, render the login/register page
        return render(request, 'orders/login.html')

# Log out page
def logoutUser(request):
    logout(request)
    user = None
    return redirect('/')

# Menu
def menu(request):
    # Add to cart database
    if request.method == "POST":
        # POST data
        identifier = request.POST.get('button', None)
        type = request.POST.get('type', None)
        price = request.POST.get('price', None)
        if price == "small_price":
            size = "Small"
        elif price == "large_price":
            size = "Large"
        else:
            return redirect('menu')

        # Get values for PIZZA
        if type == "Regular Pizza" or type == "Sicilian Pizza":
            pizza = Pizza.objects.get(id=identifier)
            # Check with database
            name = pizza.name
            if price == "small_price":
                p = pizza.small_price
            else:
                p = pizza.large_price
            topping1 = ''
            topping2 = ''
            topping3 = ''
            if pizza.topping_count == 1:
                topping1 = Topping.objects.get(id=request.POST.get('topping1', None))
            elif pizza.topping_count == 2:
                topping1 = Topping.objects.get(id=request.POST.get('topping1', None))
                topping2 = Topping.objects.get(id=request.POST.get('topping2', None))
            elif pizza.topping_count == 3:
                topping1 = Topping.objects.get(id=request.POST.get('topping1', None))
                topping2 = Topping.objects.get(id=request.POST.get('topping2', None))
                topping3 = Topping.objects.get(id=request.POST.get('topping3', None))           


        # Add into cart database
        customer = CustomerOrder(customer=request.user, item=type, name=name, size=size, price=p, topping1=topping1, topping2=topping2, topping3=topping3, status="Pending")
        customer.save()
        return redirect('menu')

    else:
        # Get all the menu from the database
        ordersum = CustomerOrder.objects.filter(customer=request.user, status="Pending").aggregate(Sum('price'))['price__sum']
        try:
            ordersum = round(ordersum, 2)
        except TypeError:
            pass
        
        context = {
            "regularpizza": Pizza.objects.filter(menu__menu="Regular Pizza"),
            "sicilianpizza": Pizza.objects.filter(menu__menu="Sicilian Pizza"),
            "toppings": Topping.objects.order_by('topping'),
            "subs": Sub.objects.all(),
            "pastas": Pasta.objects.all(),
            "salads": Salad.objects.all(),
            "dinnerplatters": DinnerPlatter.objects.all(),
            "steakextras": Extra.objects.filter(menu="Steak"),
            "subextras": Extra.objects.filter(menu="Sub"),
            "cart": CustomerOrder.objects.filter(customer=request.user),
            "ordersum": ordersum
        }
        return render(request, 'orders/menu.html', context)

# Sub
def sub(request):
    if request.method == "POST":
        # Get post data
        identifier = request.POST.get('button', None)
        type = request.POST.get('type', None)
        size = request.POST.get('price', None)
        
        # Check with database
        sub = Sub.objects.get(id=identifier)

        p = 0

        name = sub.menu
        if size == "Small":
            p = sub.small_price
        else:
            p = sub.large_price

        print(p)
        print(name)
        print(sub.extra_count)
        print(request.POST.get('extra1', None))

        extra1 = ''
        extra2 = ''
        extra3 = ''
        if request.POST.get('extra1', None) is not None:
            if sub.extra_count == 1:
                extra1 = Extra.objects.get(id=request.POST.get('extra1', None))
                total = p + extra1.small_price
            elif sub.extra_count == 2:
                extra1 = Extra.objects.get(id=request.POST.get('extra1', None))
                extra2 = Extra.objects.get(id=request.POST.get('extra2', None))
                total = p + extra1.small_price + extra2.small_price
            elif sub.extra_count == 3:
                extra1 = Extra.objects.get(id=request.POST.get('extra1', None))
                extra2 = Extra.objects.get(id=request.POST.get('extra2', None))
                extra3 = Extra.objects.get(id=request.POST.get('extra3', None))
                total = p + extra1.small_price + extra2.small_price + extra3.small_price
        else:
            total = p
            
        print(total)

        # Add into cart database
        customer = CustomerOrder(customer=request.user, item=type, name=name, size=size, price=total, extra1 = extra1, extra2=extra2, extra3=extra3, status="Pending")
        customer.save()
        return redirect('menu')

# Pasta
def pasta(request):
    if request.method == "POST":
        # Get post data
        identifier = request.POST.get('button', None)
        type = request.POST.get('type', None)
        size = request.POST.get('price', None)
        
        # Check with database
        pasta = Pasta.objects.get(id=identifier)
        if pasta is not None:
            name = pasta.menu
            total = pasta.price
            extra1 = None
            extra2 = None
            extra3 = None

            # Add into cart database
            customer = CustomerOrder(customer=request.user, item=type, name=name, size=size, price=total, extra1 = extra1, extra2=extra2, extra3=extra3, status="Pending")
            customer.save()
            return redirect('menu')
        return redirect('menu')

# Salad
def salad(request):
    if request.method == "POST":
        # Get post data
        identifier = request.POST.get('button', None)
        type = request.POST.get('type', None)
        size = request.POST.get('price', None)
        
        # Check with database
        salad = Salad.objects.get(id=identifier)
        if salad is not None:
            name = salad.menu
            total = salad.price
            extra1 = None
            extra2 = None
            extra3 = None

            # Add into cart database
            customer = CustomerOrder(customer=request.user, item=type, name=name, size=size, price=total, extra1 = extra1, extra2=extra2, extra3=extra3, status="Pending")
            customer.save()
            return redirect('menu')
        return redirect('menu')

# Dinner Platter
def dinnerplatter(request):
    if request.method == "POST":
        # Get post data
        identifier = request.POST.get('button', None)
        type = request.POST.get('type', None)
        size = request.POST.get('price', None)

        # Check with database
        dinnerplatter = DinnerPlatter.objects.get(id=identifier)
        if dinnerplatter is not None:
            if size == "Small":
                total = dinnerplatter.small_price
            else:
                total = dinnerplatter.large_price
            name = dinnerplatter.menu
            extra1 = None
            extra2 = None
            extra3 = None

            # Add into cart database
            customer = CustomerOrder(customer=request.user, item=type, name=name, size=size, price=total, extra1 = extra1, extra2=extra2, extra3=extra3, status="Pending")
            customer.save()
            return redirect('menu')
        return redirect('menu')

# Shopping Cart
def shoppingcart(request):
    if request.method == "POST":
        # Delete item from shopping cart
        item_id = request.POST.get('item_id', None)
       
        # Delete
        CustomerOrder.objects.filter(customer=request.user, id=item_id).delete()

        return redirect('shoppingcart')
    
    else:
        # Get all the menu from the database
        ordersum = CustomerOrder.objects.filter(customer=request.user, status="Pending").aggregate(Sum('price'))['price__sum']
        try:
            ordersum = round(ordersum, 2)
        except TypeError:
            pass

        context = {
            "cart": CustomerOrder.objects.filter(customer=request.user),
            "ordersum": ordersum
        }
        return render(request, 'orders/cart.html', context)   

# Payment
def payment_cart(request):
    if request.method == "POST":
        # Update status of customer's orders
        CustomerOrder.objects.filter(customer=request.user).update(status="Approved")

        # Send an email to the customer
        send_mail(
            "Pinocchio's Pizza & Subs", # Subject
            "Hi, " + request.user.first_name + ". We've received your orders. Please wait patiently as we process your orders.", # Message
            "pinocchio@business.com",
            [request.user.email], # To Email
        )

        messages.success(request, "Payment Successful! Please check this page or your email for updates.")
        return redirect('shoppingcart')