from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.text import slugify

from store.models import Product
from userprofile.models import Userprofile

from store.forms import ProductForm


# Create your views here.
def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)
    products = user.products.filter(status=Product.ACTIVE)

    return render(request, 'userprofile/vendor_detail.html', {
        'user': user,
        'products': products,
    })


@login_required
def my_store(request):
    products = request.user.products.exclude(status=Product.DELETED)
    return render(request, 'userprofile/my_store.html', {'products': products})


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        # Save the form data to the database
        if form.is_valid():
            title = request.POST.get('title')
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()

            messages.success(request, "The product has been added successfully!")
            return redirect('my_store')  # Redirect to the success page which is my store
    else:
        form = ProductForm()
    return render(request, 'userprofile/add_product.html', {
        'title': 'Add Product',
        'form': form
    })


@login_required
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()

            messages.success(request, "The product has been edited successfully!.")

            return redirect('my_store')
    else:
        form = ProductForm(instance=product)

    return render(request, 'userprofile/add_product.html', {
        'title': 'Edit product',
        'product': product,
        'form': form
    })


@login_required
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETED
    product.save()

    messages.success(request, "The product has been deleted successfully!")

    return redirect('my_store')


@login_required
def profile(request):
    return render(request, 'userprofile/profile.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            userprofile = Userprofile.objects.create(user=user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'userprofile/signup.html', {'form': form})
