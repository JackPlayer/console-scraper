import unittest 
import urls 

class TestUrls(unittest.TestCase):
    def test_parse_proper(self):
        result = urls.parse_file('./test_files/urls.txt')
        self.assertEqual(result, [{'testretailer1': 'www.google.com'}, {'testretailer2': 'www.amazon.ca'}])
  

    def test_parse_malformed(self):
        self.assertRaises(Exception, urls.parse_file, './test_files/malformed_urls.txt')

    def test_parse_empty(self):
        result = urls.parse_file('./test_files/empty.txt')
        self.assertEqual(result, [])
