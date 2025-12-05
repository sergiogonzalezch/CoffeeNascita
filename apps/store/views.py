from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Importing fake data for testing purposes
from store.util.test_scripts.fake_data import menu_list


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


# Detail view
def detail(request, *args, **kwargs):
    print(f"ARGS: {args}")
    print(f"KWARGS: {kwargs}")
    return HttpResponse(f"Detail view for item {kwargs.get('item_id')}")
