from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name="Category Name")
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated At")

    def __str__(self):
        return self.name


# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=250, verbose_name="Menu Item Name")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Price")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    have_discount = models.BooleanField(default=False, verbose_name="Have Discount")
    discount_price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Discount Price"
    )
    in_menu = models.BooleanField(default=True, verbose_name="In Menu")
    # One to Many relationship
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name="Category")
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated At")
    photo_item = models.ImageField(upload_to="menu_items/", blank=True, null=True, verbose_name="Photo Item")

    def __str__(self):
        return f"{self.name} - ${self.price}"


class Order(models.Model):
    # Many to Many relationship
    menu_items = models.ManyToManyField(MenuItem, related_name="menu_items", verbose_name="Menu Items")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantity")
    total_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Total Price")
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated At")

    def __str__(self):
        # return f"Order of {self.quantity} x {self.menu_item.name} - Total: ${self.total_price}"
        return f"Order of {self.quantity} - Total: ${self.total_price}"


class DeliveryStatus(models.Model):
    # One to One relationship
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="order", verbose_name="Order")
    status = models.CharField(max_length=100, verbose_name="Status")
    delivered_at = models.DateTimeField(null=True, blank=True, verbose_name="Delivered At")
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated At")
