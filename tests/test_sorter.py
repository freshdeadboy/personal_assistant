# tests/test_sorter.py
import unittest
from personal_assistant.sorter import Sorter

class TestSorter(unittest.TestCase):
    def setUp(self):
        self.sorter = Sorter()

    def test_sort_list_ascending(self):
        data_to_sort = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_data = self.sorter.sort_list(data_to_sort)
        self.assertEqual(sorted_data, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_sort_list_descending(self):
        data_to_sort = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_data_reverse = self.sorter.sort_list(data_to_sort, reverse=True)
        self.assertEqual(sorted_data_reverse, [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1])

if __name__ == '__main__':
    unittest.main()
