from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    have_discount = models.BooleanField(default=False)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    in_menu = models.BooleanField(default=True)
    # One to Many relationship
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name} - ${self.price}"

class Order(models.Model):
    # Many to Many relationship
    menu_items = models.ManyToManyField(MenuItem, related_name='menu_items')
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        # return f"Order of {self.quantity} x {self.menu_item.name} - Total: ${self.total_price}"
        return f"Order of {self.quantity} - Total: ${self.total_price}"


class DeliveryStatus(models.Model):
    # One to One relationship
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='order')
    status = models.CharField(max_length=100)
    delivered_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)