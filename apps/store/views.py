from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import FormView, DetailView
from .forms import MenuItemForm, CategoryForm
from django.urls import reverse_lazy
from .models import MenuItem, Order

# Importing fake data for testing purposes
# from .util.test_scripts.fake_data import menu_list


# Create your views here.
def index(request):
    return render(request, "./index.html")


# Old function-based view
# def menu_list(request):
#     menu_list = [{"name": "Espresso"}, {"name": "Cappuccino"}, {"name": "Latte"}]
#     context = {
#         "menu_list": menu_list
#     }
#     return render(request, './store/menu_list.html', context)


# New class-based view
class MenuItemListView(TemplateView):
    template_name = "store/menu_list.html"

    def get_context_data(self):
        queryset = MenuItem.objects.all()
        menu_list = queryset
        return {"menu_list": menu_list}


class CategoryFormView(FormView):
    template_name = "forms/add_edit_category.html"
    form_class = CategoryForm
    success_url = reverse_lazy("add_category")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class MenuItemsFormView(FormView):
    template_name = "forms/add_edit_menu_item.html"
    form_class = MenuItemForm
    # success_url = reverse_lazy("add_menu_item")
    success_url = reverse_lazy("menu_list")


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class MyOrderView(DetailView):
    model = Order
    template_name = "store/my_order.html"
    context_object_name = "order"
    def get_object(self, queryset=None):
        return Order.objects.filter(is_completed=True).first()
    

# Detail view
def detail(request, *args, **kwargs):
    print(f"ARGS: {args}")
    print(f"KWARGS: {kwargs}")
    return HttpResponse(f"Detail view for item {kwargs.get('item_id')}")
