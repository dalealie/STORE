from django.db import models

# BaseModel to inherit created_at and updated_at fields
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Category model (one-to-many relationship)
class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Product model (one-to-many relationship with Category)
class Product(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Customer model
class Customer(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

# Order model (one-to-many relationship with Customer and many-to-many relationship with Product)
class Order(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.name}"

# Review model (many-to-one relationship with Product)
class Review(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.product.name}"

# Other models with different fields can be similarly created following the structure of BaseModel and incorporating the required fields.
