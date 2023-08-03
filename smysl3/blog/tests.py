from django.urls import resolve
from django.test import TestCase
from blog.views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Koba Cake</title>', html)
        self.assertIn('<h1>Koba Cake</h1>', html)
        self.assertTrue(html.endswith('</html>'))

#class SmokeTest(TestCase):
#    def test_bad_math(self):
#        self.assertEqual(1 + 1, 3)
