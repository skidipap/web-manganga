from django.test import TestCase
from django.test import SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_mangareader_page_status_code(self):
        response = self.client.get('/mangareader/')
        self.assertEqual(response.status_code, 200)

