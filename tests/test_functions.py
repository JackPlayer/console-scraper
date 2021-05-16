import unittest 
from context import parsers

class TestFunctions(unittest.TestCase):
    def test_bestbuy_format_price(self):
        result1 = parsers.bestbuy.format_price('$599')
        result2 = parsers.bestbuy.format_price('$5999')
        result3 = parsers.bestbuy.format_price('$10')
        self.assertEqual(result1, '$5.99')
        self.assertEqual(result2, '$59.99')
        self.assertEqual(result3, '$.10')