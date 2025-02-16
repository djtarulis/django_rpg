from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import HeroCreationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Player, PlayerInventory
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404

"""
Register new user
"""
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debug
            user = form.save()
            print(f"User created: {user}")  # Debug
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(f"User authenticated: {user}")  # Debug
                login(request, user)    # Log the user in after signup
                messages.success(request, 'Your account has been created! You can now log in.')
                return redirect('login') # Redirect to login page
            else:
                print("Authentication failed")  # Debug
        else:
            print("Form is invalid") # Debug
    else:
        form = UserCreationForm()
    return render(request, 'player/register.html', {'form': form})

"""
Create new hero
"""
@login_required
def create_hero(request):
    """
    Allow creation of player hero
    """
    if request.method == 'POST':
        form = HeroCreationForm(request.POST)
        if form.is_valid():
            hero = form.save(commit=False)
            hero.owner = request.user
            hero.initialize_stats()  # Initialize stats based on the class
            hero.save()
            return redirect('hero_detail', hero_id=hero.id)
    else:
        form = HeroCreationForm()
    return render(request, 'player/create_hero.html', {'form': form})

"""
Display user inventory
"""
@login_required
def view_inventory(request):
    # Get the Player object linked to the current user
    player = get_object_or_404(Player, user=request.user)    
    inventory = PlayerInventory.objects.filter(user=player)
    
    return render(request, "player/user_inventory.html", {
        'inventory': inventory
    })

def home(request):
    return render(request, 'player/home.html')

class CustomLoginView(LoginView):
    template_name = 'player/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'player/logout.html'