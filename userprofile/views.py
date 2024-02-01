from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from userprofile.models import Userprofile

from store.forms import ProductForm
from store.models import Product, Category


# Create your views here.
def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)

    return render(request, 'userprofile/vendor_detail.html', {
        'user': user
    })


@login_required
def my_store(request):
    return render(request, 'userprofile/my_store.html')


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            product = form.save(commit=False)
            product.user = request.user  # Assuming Product model has a 'user' field
            product.save()
            return redirect('success_page')  # Redirect to a success page or any other desired page
    else:
        form = ProductForm()

    return render(request, 'userprofile/add_product.html', {'form': form})


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
