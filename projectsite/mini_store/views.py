from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product, Customer, Order, Review

def home(request):
    # Your logic for the home view
    return render(request, 'home.html') 

# Example view for rendering a page with all categories
def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'all_categories.html', {'categories': categories})

# Example view for rendering product details
def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    reviews = Review.objects.filter(product=product)
    return render(request, 'product_detail.html', {'product': product, 'reviews': reviews})

# Example view for creating an order
def create_order(request, customer_id):
    if request.method == 'POST':
        customer = Customer.objects.get(id=customer_id)
        products = request.POST.getlist('products')  # Assuming products are submitted as a list of IDs
        date = request.POST.get('date')
        total_amount = request.POST.get('total_amount')

        # Create a new order
        order = Order.objects.create(
            customer=customer,
            date=date,
            total_amount=total_amount
        )

        # Adding selected products to the order
        for product_id in products:
            product = Product.objects.get(id=product_id)
            order.products.add(product)

        return HttpResponse('Order created successfully!')

    # Handle GET requests (display form to create an order)
    customer = Customer.objects.get(id=customer_id)
    products = Product.objects.all()  # Retrieve all products to display in the form
    return render(request, 'create_order.html', {'customer': customer, 'products': products})
