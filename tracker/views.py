import os
import matplotlib.pyplot as plt
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Expense, Category
from django.conf import settings

# Home page (Redirects based on authentication status)
def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to dashboard if logged in
    else:
        return render(request, 'tracker/home.html')

# Register View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=user, password=raw_password)
            login(request, user)
            return redirect('home')  # Redirect to dashboard after registration
    else:
        form = UserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})

# Login View
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'tracker/login.html')

# Logout View
def user_logout(request):
    logout(request)
    return redirect('login')

# Dashboard View (Shows all expenses of the logged-in user)
@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user)  # Only get the logged-in user's expenses
    return render(request, 'tracker/visualize_expenses.html', {'expenses': expenses})


@login_required
def add_expense(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        category_id = request.POST['category']
        amount = request.POST['amount']
        date_added = request.POST['date_added']  # New field

        # Manually creating an Expense object
        category = Category.objects.get(id=category_id)
        expense = Expense(user=request.user, category=category, amount=amount, date_added=date_added)
        expense.save()

        return redirect('dashboard')  

    return render(request, 'tracker/add_expense.html', {'categories': categories})
import os
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
from django.shortcuts import render
from .models import Expense, Category

@login_required
def visualize_expenses(request):
    categories = Category.objects.all()
    expenses = Expense.objects.filter(user=request.user)

    # Calculate total expenses per category
    category_expenses = {category.name: 0 for category in categories}
    for expense in expenses:
        category_expenses[expense.category.name] += float(expense.amount)

    # Generate file paths for the charts
    static_dir = os.path.join('static', 'tracker')
    pie_chart_path = os.path.join(static_dir, 'pie_chart.png')
    bar_chart_path = os.path.join(static_dir, 'bar_chart.png')

    # Convert paths to string
    pie_chart_path_str = str(pie_chart_path)
    bar_chart_path_str = str(bar_chart_path)

    # Ensure the static directory exists
    os.makedirs(static_dir, exist_ok=True)

    # Pie chart generation
    fig, ax = plt.subplots()
    ax.pie(category_expenses.values(), labels=category_expenses.keys(), autopct='%1.1f%%')
    fig.savefig(pie_chart_path_str)
    plt.close(fig)

    # Bar graph generation
    fig, ax = plt.subplots()
    ax.bar(category_expenses.keys(), category_expenses.values())
    fig.savefig(bar_chart_path_str)
    plt.close(fig)

    # Pass the relative paths to the template
    return render(request, 'tracker/visualize_expenses.html', {
        'pie_chart_path': '/' + pie_chart_path_str,
        'bar_chart_path': '/' + bar_chart_path_str
    })
