from django.urls import path
from .views import index, detail, MenuItemListView, MenuItemsFormView, CategoryFormView

urlpatterns = [
    path("", index, name="index"),
    # path('menu-list/', views.menu_list, name='menu_list'),
    path("menu-list/", MenuItemListView.as_view(), name="menu_list"),
    path("details/<int:item_id>/", detail, name="detail"),
    path("add-category/", CategoryFormView.as_view(), name="add_category"),
    path("add-menu-item/", MenuItemsFormView.as_view(), name="add_menu_item"),
]
