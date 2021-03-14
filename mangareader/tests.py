from django.test import TestCase

from .models import MangaList

# Create your tests here.
class MangaListModelTest(TestCase):
    def setUp(self):
        MangaList.objects.create(title='just a test')

    def test_title_content(self):
        name = MangaList.objects.get(id=1)
        expected_object_name = f'{name.title}'
        self.assertEqual(expected_object_name, 'just a test')
