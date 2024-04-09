from django.http import HttpResponse

from django.shortcuts import render, redirect
from .forms import SignUpForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


# Create your views here.
def home(request):
    return render(request, "index.html")


def callback_view(request):
    return HttpResponse("Yay! You logged in!")
