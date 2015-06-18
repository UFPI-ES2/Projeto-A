from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

class ocrSysViewTest(TestCase):

    def test_draft_status_code(self):
        client = Client()
        client.login(username='user', password='user')
        response = client.get(reverse('ocrSys:draft'))
        self.assertEqual(response.status_code, 200)

    def test_scan_document_status_code(self):
        client = Client()
        client.login(username='user', password='user')
        response = client.get(reverse('ocrSys:scan_document'))
        self.assertEqual(response.status_code, 200)

class ocrSysTemplateTest(TestCase):
    
    def test_template_used(self):
        client = Client()
        client.login(username='user', password='user')
        response = client.get(reverse('ocrSys:draft'))
        self.assertTemplateUsed(response, 'drafthtml')
        response = client.get(reverse('ocrSys:scan_document'))
        self.assertTemplateUsed(response, 'scan_document.html')