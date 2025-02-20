from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name='home'),
   path('add-expense/', views.add_expense, name='add_expense'),    
    path('dashboard/', views.dashboard, name='dashboard'),  # Ensure this is present
    path('visualize-expenses/', views.visualize_expenses, name='visualize_expenses'),  # Visualize expenses (if you are using that view)
]
