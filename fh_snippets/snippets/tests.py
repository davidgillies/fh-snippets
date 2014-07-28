from django.test import TestCase
from snippets.models import Snippet

# Create your tests here.
class SnippetModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_snippet = Snippet()
        first_snippet.snippet = 'first snippet'
        first_snippet.source_title = 'The Book of Me'
        first_snippet.author = 'David Gillies'
        first_snippet.source_type = 'Book'
        first_snippet.notes = 'bla'
        first_snippet.save()

        second_snippet = Snippet()
        second_snippet.snippet = 'second snippet'
        second_snippet.source_title = 'The Book of Her'
        second_snippet.author = 'Mrs Gillies'
        second_snippet.source_type = 'Book'
        second_snippet.notes = 'bla'
        second_snippet.save()

        saved_snippets = Snippet.objects.all()
        self.assertEqual(saved_snippets.count(), 2)

        first_saved_snippet = saved_snippets[0]
        second_saved_snippet = saved_snippets[1]
        self.assertEqual(first_saved_snippet.author, 'David Gillies')
        self.assertEqual(second_saved_snippet.author, 'Mrs Gillies')

