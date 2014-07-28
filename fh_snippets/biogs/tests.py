from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from biogs.views import index
from biogs.models import Biog
import time

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

class BiogModelTest(TestCase):
    
    def test_saving_and_retrieving_items(self):
        first_biog = Biog()
        first_biog.first_name = 'David'
        first_biog.surname = 'Gillies'
        first_biog.birth_year = '1548'
        first_biog.notes = 'bla'
        first_biog.save()

        second_biog = Biog()
        second_biog.first_name = 'Mrs'
        second_biog.surname = 'Gillies'
        second_biog.birth_year = '1936'
        second_biog.notes = 'bla'
        second_biog.save()

        saved_biogs = Biog.objects.all()
        self.assertEqual(saved_biogs.count(), 2)

        first_saved_biog = saved_biogs[0]
        second_saved_biog = saved_biogs[1]
        
        self.assertEqual(first_saved_biog.first_name, 'David')
        self.assertEqual(second_saved_biog.first_name, 'Mrs')
