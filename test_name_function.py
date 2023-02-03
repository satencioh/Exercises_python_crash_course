import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """prueba para name_function.py"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('Luisa','Hernandez')
        self.assertEqual(formatted_name, 'Luisa Hernandez')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('Luisa','Hernandez', 'paola')
        self.assertEqual(formatted_name, 'Luisa Paola Hernandez')

if __name__ == '__main__':
    unittest.main()