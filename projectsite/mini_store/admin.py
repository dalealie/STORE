from django.contrib import admin
from .models import Category, Product, Customer, Order, Review

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Review)
# Register other models you want to manage via Django admin here
