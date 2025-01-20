from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Import User model

# Category model for expense categories
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Expense model for storing expenses
class Expense(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add user field to associate with the logged-in user

    def __str__(self):
        return f"{self.category.name} - {self.amount} - {self.date_added}"
