from django.test import TestCase

class HomePageTest(TestCase):
    
    def test_home_page_returns_currect_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
