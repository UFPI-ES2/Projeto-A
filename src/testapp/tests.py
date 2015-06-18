from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

class testappViewTest(TestCase):

    def test_dashboard_status_code(self):
        client = Client()
        client.login(username='user', password='user')
        response = client.get(reverse('testapp:index'))
        self.assertEqual(response.status_code, 200)

class testappTemplateTest(TestCase):
    
    def test_template_used(self):
        client = Client()
        response = client.get(reverse('testapp:index'))
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'dashboard_base.html')
        self.assertTemplateUsed(response, 'footer.html')
        self.assertTemplateUsed(response, 'home.html')