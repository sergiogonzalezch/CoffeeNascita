from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from .forms import MenuItemForm, CategoryForm
from django.urls import reverse_lazy

# Importing fake data for testing purposes
# from store.util.test_scripts.fake_data import menu_list
from apps.store.util.test_scripts.fake_data import menu_list


# Create your views here.
def index(request):
    return render(request, "./index.html")


# Old function-based view
# def menu_list(request):
#     menu_list = [{"name": "Espresso"}, {"name": "Cappuccino"}, {"name": "Latte"}]
#     context = {
#         "menu_list": menu_list
#     }
#     return render(request, './menu_list.html', context)


# New class-based view
class MenuItemListView(TemplateView):
    template_name = "menu_list.html"

    def get_context_data(self):
        # menu_list = [{"name": "Espresso"}, {"name": "Cappuccino"}, {"name": "Latte"}]
        return {"menu_list": menu_list}


class CategoryFormView(FormView):
    template_name = "add_edit_category.html"
    form_class = CategoryForm
    success_url = reverse_lazy("add_category")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class MenuItemsFormView(FormView):
    template_name = "add_edit_menu_item.html"
    form_class = MenuItemForm
    success_url = reverse_lazy("add_menu_item")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# Detail view
def detail(request, *args, **kwargs):
    print(f"ARGS: {args}")
    print(f"KWARGS: {kwargs}")
    return HttpResponse(f"Detail view for item {kwargs.get('item_id')}")
