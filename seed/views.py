# from django.shortcuts import render,redirect

# def index(request):
#     return render(request , 'seed/index.html')


# def login(request):
#     return render(request , 'seed/login.html')

# def error_404(request):
#     return render(request , 'seed/error_404.html')

# def explore(request):
#     return render(request, 'seed/explore.html')

# def testimonials(request):
#     return render(request, 'seed/testimonials.html')

# def signup(request):
#     return render(request, 'seed/signup.html')

# def forget_password(request):
#     return render(request, 'seed/forgot_password.html')

# def contacts(request):
#     return render(request, 'seed/contacts.html')

# def view_details(request):
#     return render(request, 'seed/view_details.html')

# def showcart(request):
#     return render(request , 'seed/showcart.html')

# def checkout(request):
#     return render(request , 'seed/checkout.html')


# ///////////////////////////////////////////////////////////////////////////////////


from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import login as auth_login , logout as auth_logout , authenticate
from django.contrib.auth.decorators import login_required 
from django.contrib import messages 
from .models import Seed, Testimonial , User , Contacts, Cart , CartItem , Order , OrderItem 
from .forms import UserRegistrationForm , ContactForm 

def index(request):
    seeds = Seed.objects.all()[:4] #will take 4 objects at the index page 
    testimonial = Testimonial.objects.all()[:3] #will take 3 testimonials 
    return render(request , 'seed/index.html',{
        'seeds' : seeds,
        'testimonial' : testimonial,
    })



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username , password=password)
        if user not in None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'seed/login.html')

def error_404(request):
    return render(request, 'seed/error_404.html')

def explore(request):
    seeds = Seed.objects.all()
    return render(request, 'seed/explore.html' , {'seeds' : seeds})


def testimonials(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')
    return render(request, 'seed/testimonials.html', {'testimonials' : testimonials})


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'seed/signup.html' , {'form' : form})


def forget_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)

            #added password reset logic here 
            messages.success(request, 'Password reset link has been sent to email ')
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, 'No user found with this email address ')
    return render(request, 'seed/forgot_password.html')


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent ')
            return redirect('contacts')
    else:
        form = ContactForm()

    return render(request, 'seed/contacts.html', {'form':form})


def view_details(request, seed_id):
    seed = get_object_or_404(Seed, id=seed_id)
    return render(request, 'seed/view_details.html', {'seed': seed})


@login_required
def showcart(request):
    cart , created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'seed/showcart.html',{'cart':cart})

@login_required
def add_to_cart(request, seed_id):
    seed = get_object_or_404(Seed, id=seed_id)
    cart , created = Cart.objects.get_or_create(user=request.user)
    cart_item , created = CartItem.objects.get_or_create(cart=cart , seed=seed)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('showcart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id = item_id , cart__user = request.user)
    cart_item.delete()

    return redirect('showcart')


@login_required
def checkout(request):
    cart = get_object_or_404(Cart , user=request.user)
    if request.method == 'POST':

        #create order form cart 
        order = Order.objects.create(
            user = request.user,
            total_amount = cart.get_total(),
            shipping_address = request.POST.get('shipping_address')
        )

        #create order item from cart item 
        for cart_item in cart.items.all():
            OrderItem.objects.create(
                order = order ,
                seed = cart_item.seed,
                quantity = cart_item.quantity,
                price = cart_item.seed.price
            )

        #clearing the cart 
        cart.items.all().delete()
        messages.success(request, 'Order placed successfully ')
        return redirect('index')
    return render(request, 'seed/checkout.html', {'cart':cart})


