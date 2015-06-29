from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

class authViewTest(TestCase):

    def test_login_status_code(self):
        client = Client()
        response = client.get(reverse('auth:index'))
        self.assertEqual(response.status_code, 200)

    def test_logout_status_code(self):
        client = Client()
        response = client.get(reverse('auth:logout'))
        self.assertEqual(response.status_code, 200)

class authTemplateTest(TestCase):
    
    def test_template_use(self):
        client = Client()
        response = client.get(reverse('auth:index'))
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'login.html')


class login_usuario_form(TestCase):
    
    def test_usuario_form_error(self):
        data = {'user': 'admin', 'pass': '1234'}
        client = Client()
        path = reverse('auth:index')
        response = client.post(path, data)
        self.assertFormError(response, 'form', 'user', 'Este campo é obrigatório')
        self.assertFormError(response, 'form', 'pass', 'Este campo é obrigatório')
        
        