from django.shortcuts import redirect, render

from .models import CustomUser
from .forms import RegistrationForm

from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = CustomUser.objects.create_user(
                email=email,
                password=password
            )

            return redirect(to=f'/user/signin/')
    else:
        form = RegistrationForm()
    
    context = {
        "form": form
    }
    return render(request=request, template_name='user/signup.html', context=context)


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            redirect(to='signin')

    return render(request=request, template_name='user/signin.html')


def dashboard(request):
    return render(request=request, template_name='dashboard/dashboard.html')
