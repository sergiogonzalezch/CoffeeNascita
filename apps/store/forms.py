from django import forms
from .models import MenuItem

class MenuItemForm(forms.Form):
    name = forms.CharField(label='Menu Item Name', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea, required=False)
    price = forms.DecimalField(label='Price', max_digits=5, decimal_places=2)
    have_discount = forms.BooleanField(label='Have Discount', required=False)
    discount_price = forms.DecimalField(label='Discount Price', max_digits=5, decimal_places=2, required=False)
    in_menu = forms.BooleanField(label='In Menu', required=False)
    category = forms.CharField(label='Category', max_length=100, required=False)
    photo_item = forms.ImageField(label='Photo Item', required=False)

    def save(self):
        # Logic to save the form data to the database or perform other actions
        MenuItem.objects.create(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            price=self.cleaned_data['price'],
            have_discount=self.cleaned_data['have_discount'],
            discount_price=self.cleaned_data['discount_price'],
            in_menu=self.cleaned_data['in_menu'],
            category=self.cleaned_data['category'],
            photo_item=self.cleaned_data['photo_item'],
        )