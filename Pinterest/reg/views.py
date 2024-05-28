from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignUpForm, CustomLoginForm

def handle_form_submission(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('mainpage')
    return form

def register(request):
    if request.method == 'POST':
        form = handle_form_submission(request)
        if isinstance(form, HttpResponse):  # Check if form submission requires a redirect
            return form
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    return render(request, "index.html")

def callback_view(request):
    return redirect('mainpage')

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'

    def get_success_url(self):
        return '/mainpage/'

def mainpage(request):
    return render(request, "mainpage.html")
