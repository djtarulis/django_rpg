from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # Login and Logout views
    path('login/', views.CustomLoginView.as_view(template_name='player/login.html'), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    # path('login/', DebugLoginView.as_view(), name='login'),

    # Home
    path('', views.home, name='home'),  # Home page
    # Signup view
    path('register/', views.register, name='register'),

    # Player paths
    path("create_hero/", views.create_hero, name="create_hero"),
    path("user_inventory/", views.view_inventory, name="user_inventory"),

]