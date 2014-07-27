from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from biogs.views import index

class BiogsIndexTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/biogs/')
        self.assertEqual(found.func, index)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        
        response = index(request)
        
        expected_html = render_to_string('biog_home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_index_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['new_biog_first_name'] = 'Bert'
        request.POST['new_biog_surname'] = 'Konterman'
        request.POST['new_biog_birth_year'] = '1976'
        
        response = index(request)
        
        self.assertIn('Konterman', response.content.decode())

