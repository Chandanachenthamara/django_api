# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib import messages
# from .forms import UserRegistrationForm
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.contrib.auth.forms import AuthenticationForm
# from django.shortcuts import render

# def home_view(request):
#     return render(request, 'user/home.html')

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             # Redirect to a success page or any other desired page
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
    
#     context = {'form': form}
#     return render(request, 'user/login.html', context)
# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your account has been created. You can log in now!')
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()

#     context = {'form': form}
#     return render(request, 'user/register.html', context)
# # def user_profile_view(request):
# #     profiles = UserProfile.objects.all()
# #     return render(request, 'user/user_profiles.html', {'profiles': profiles})


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

def home_view(request):
    return render(request, 'user/home.html')

def login_view(request):
    if request.method == 'POST':
        # Check the user type and authenticate accordingly
        if request.POST.get('user_type') == 'user1':
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'], backend='user.backends.User1Backend')
        elif request.POST.get('user_type') == 'user2':
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'], backend='user.backends.User2Backend')
        else:
            user = None

        if user is not None:
            login(request, user)
            # Redirect to a success page or any other desired page
            return redirect('home')
        else:
            # Invalid credentials, show error message
            messages.error(request, 'Invalid username or password.')
    
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'user/login.html', context)

def register(request):
    if request.method == 'POST':
        # Check the user type and use the corresponding registration form
        if request.POST.get('user_type') == 'user1':
            form = UserRegistrationForm(request.POST)
        elif request.POST.get('user_type') == 'user2':
            form = User2RegistrationForm(request.POST)
        else:
            form = None
        
        if form is not None and form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'user/register.html', context)
