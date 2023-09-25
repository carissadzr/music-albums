from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404

@login_required(login_url='/login')

# Create your views here.
def show_main(request):
    products = Product.objects.filter(user = request.user)
    jumlah_item = len(products)

    context = {
        'name': request.user.username,
        'class': 'PBP D', # Kelas PBP kamu
        'products': products,
        'jumlah_item': jumlah_item,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    print(data)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def product_list(request):
    jumlah_item = Product.objects.count()
    return render(request, 'main.html', {'jumlah_item': jumlah_item})

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def update_product_amount(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        amount = request.POST.get('amount')

        try:
            product = Product.objects.get(pk=product_id)
            if amount == 'add':
                product.amount += 1
            elif amount == 'reduce':
                if product.amount > 0:
                    product.amount -= 1
            product.save()
        except Product.DoesNotExist:
            raise Http404

    return redirect('main:show_main')

@login_required(login_url='/login')
def delete_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')

        try:
            product = Product.objects.get(pk=product_id, user=request.user)
            product.delete()
        except Product.DoesNotExist:
            pass  # Produk tidak ditemukan atau sudah dihapus

    return redirect('main:show_main')
