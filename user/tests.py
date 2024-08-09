from http import HTTPStatus
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy


class RegisterTestCase(TestCase):

    def setUp(self) -> None:
        pass

    def test_successful_get_htmlform(self):
        path = reverse("register")
        response = self.client.get(path=path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "user/register.html")

    def test_successful_registration(self):
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password1": "password123qwe",
            "password2": "password123qwe",
        }
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertIsNotNone(get_user_model().objects.get(username="newuser"))

    def test_unsuccessful_registration(self):
        data = {
            "username": "",
            "email": "newuser@example.com",
            "password1": "password123",
            "password2": "password1234",
        }
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Введенные пароли не совпадают.")

    def tearDown(self) -> None:
        pass
