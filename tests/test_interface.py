import unittest 
from context import interface

class TestInterface(unittest.TestCase):
    def test_bool_to_string(self):
        result1 = interface.ui.bool_to_string(True)
        result2 = interface.ui.bool_to_string(False)
        self.assertEqual(result1, 'Yes')
        self.assertEqual(result2, 'No')

    def test_bool_to_string_list(self):
        list = [['Test', False, True],[True, True],['Test']]
        expected_list = [['Test', 'No', 'Yes'],['Yes', 'Yes'],['Test']]
        result = interface.ui.bool_to_string_list(list)
        self.assertEqual(result, expected_list)

    def test_convert_to_lists(self):
        list_with_dicts = [{'name': 'Cartman', 'age': 10, 'hometown': 'South Park'}, {'name': 'Walter White', 'age': 40, 'hometown': 'Albuquerque'}]
        expected_list = [['Cartman', 10, 'South Park'], ['Walter White', 40, 'Albuquerque']]
        result = interface.ui.convert_to_lists(list_with_dicts)
        self.assertEqual(result, expected_list)

    def test_dict_to_list(self):
        dictionary = {'key1': 'testing', 'key2': 'testing123'}
        expected_list = ['testing', 'testing123']

        result = interface.ui.dict_to_list(dictionary)
        self.assertEqual(result, expected_list)
