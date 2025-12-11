from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name="Category Name")
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="Created At"
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True, verbose_name="Updated At"
    )

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=250, verbose_name="Menu Item Name")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Price")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    have_discount = models.BooleanField(default=False, verbose_name="Have Discount")
    discount_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Discount Price",
    )
    in_menu = models.BooleanField(default=True, verbose_name="In Menu")
    # One to Many relationship
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, verbose_name="Category"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="Created At"
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True, verbose_name="Updated At"
    )
    photo_item = models.ImageField(
        upload_to="store/menu_item/", blank=True, null=True, verbose_name="Photo Item"
    )

    def __str__(self):
        return f"{self.name} - ${self.price}"


class Order(models.Model):
    # Many to One relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    # status = models.CharField(max_length=100, null=True, verbose_name="Status")
    is_completed = models.BooleanField(default=False, verbose_name="Is Completed")
    delivered_at = models.DateTimeField(
        null=True, blank=True, verbose_name="Delivered At"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="Created At"
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True, verbose_name="Updated At"
    )


class OrderMenuItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Order")
    menu_item = models.ForeignKey(
        MenuItem, on_delete=models.PROTECT, verbose_name="Menu Item"
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantity")
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="Created At"
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True, verbose_name="Updated At"
    )

    @property
    def total_price(self):
        price = (
            self.menu_item.discount_price
            if self.menu_item.have_discount
            else self.menu_item.price
        )
        return price * self.quantity

    def __str__(self):
        return f"Order of {self.quantity} - Total: ${self.total_price}"
