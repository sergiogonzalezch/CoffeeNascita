from apps.store.models import MenuItem, Category, Order, DeliveryStatus

# Persistence in memory (RAM)

# 1. Create Category instances

cold_drink = Category(name="Cold Drink")
cold_drink.save()

hot_drink = Category(name="Hot Drink")
hot_drink.save()

# 2. Create MenuItem instances

coffee_cappuccino = MenuItem(
    name="Cappuccino",
    price=4.50,
    description="A classic Italian coffee drink made with espresso, steamed milk, and a thick layer of milk foam.",
    have_discount=True,
    discount_price=3.99,
    in_menu=True,
    category=cold_drink,
)
print(coffee_cappuccino)
coffee_cappuccino.save()

# coffee_cappuccino.name

coffee_cappuccino.name = "Moka Cappuccino"
coffee_cappuccino.save()
print(coffee_cappuccino)

coffee_irish = MenuItem(
    name="Irish Coffee",
    price=5.00,
    description="A warm cocktail consisting of hot coffee, Irish whiskey, sugar, and topped with cream.",
    have_discount=False,
    in_menu=True,
    category=hot_drink,
)
coffee_irish.save()
print(coffee_irish)

# Optional: Deleting an instance

coffee_irish.delete()

MenuItem.objects.filter(id=5).delete()

# Optional: Get instance from database
MenuItem.objects.first()
MenuItem.objects.all()

cappuccino_db = MenuItem.objects.get(name="Moka Cappuccino")
coffee_irish_db = MenuItem.objects.get(name="Irish Coffee")
menu_items_list = [cappuccino_db, coffee_irish_db]
print(menu_items_list)

# 3. Create Order instance and associate MenuItems
order_one = Order(quantity=2, total_price=9.00)
order_one.save()
# menu_items_list = [coffee_irish]
order_one.menu_items.set(menu_items_list)

print(order_one)

# Optional: Get order from database
order_one_db = Order.objects.get(id=1)
print(order_one_db)

# 4. Create DeliveryStatus instance
delivery_status_good = DeliveryStatus(
    order=order_one_db,
    status="Delivered",
)
delivery_status_good.save()

# From database

MenuItem.objects.count()
MenuItem.objects.first()
MenuItem.objects.last()

Category.objects.create(name="Milkshake")

MenuItem.objects.all()
MenuItem.objects.all().filter(have_discount=True)

MenuItem.objects.filter(have_discount=False).delete()
MenuItem.objects.order_by("price")
