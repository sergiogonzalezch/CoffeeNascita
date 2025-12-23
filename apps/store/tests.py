from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import MenuItem


class StoreViewTests(TestCase):
    def test_should_return_200(self):
        url = reverse("menu_list")
        response = self.client.get(url)
        # breakpoint()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["menu_list"].count(), 0)

    def test_should_return_200_with_menu_list(self):
        url = reverse("menu_list")
        MenuItem.objects.create(
            name="Irish Coffee",
            price=9.99,
            in_menu=True,
            category=None,
            have_discount=False,
            discount_price=None,
            description="",
            photo_item=None,
        )
        response = self.client.get(url)
        # breakpoint()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["menu_list"].count(), 1)

    def test_no_logged_user_should_redirect_to_login(self):
        url = reverse("my_order")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # breakpoint()
        self.assertEqual(response.url, '/users/login/?next=/store/my-order/')
    
    def test_logged_user_should_redirect(self):
        url = reverse("my_order")
        user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.client.force_login(user)
        response = self.client.get(url)
        # breakpoint()
        self.assertEqual(response.status_code, 200)