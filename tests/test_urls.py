import unittest 
from context import parse_urls

class TestUrls(unittest.TestCase):
    def test_parse_proper(self):
        result = parse_urls.parse_file('./test_files/urls.txt')
        self.assertEqual(result, [{'testretailer1': 'www.google.com'}, {'testretailer2': 'www.amazon.ca'}])
  

    def test_parse_malformed(self):
        self.assertRaises(Exception, parse_urls.parse_file, './test_files/malformed_urls.txt')

    def test_parse_empty(self):
        result = parse_urls.parse_file('./test_files/empty.txt')
        self.assertEqual(result, [])
