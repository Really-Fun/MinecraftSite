from django.test import TestCase
from django.urls import reverse
from minecraft.models import Servers, News


# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from minecraft.models import Servers, News


# Create your tests here.
class NewsTestCase(TestCase):

    def test_home_case(self):
        path = reverse("home")
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)

    def test_new_case_successful(self):
        server = Servers.objects.create(name="Анархия", slug="anarchy", max_online=100)
        new = News.objects.create(
            title="Открытие анархии",
            text="Открытие сервера........................",
            slug="anarchy",
            is_published=True,
            server=server,
        )
        path = reverse("new", kwargs={"server": 1, "new": "anarchy"})
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
