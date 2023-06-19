import unittest
from sorted_frozen_set import SortedFrozenSet


class TestConstruction(unittest.TestCase):

    def test_construction_empty(self):
        s = SortedFrozenSet([])

    def test_construction_non_empty_list(self):
        s = SortedFrozenSet([7,8,9,3])

    def test_construction_from_an_iterator(self):
        items = [7,8,9,3]
        iterator = iter(items)
        s = SortedFrozenSet(iterator)


if __name__ == '__main__':
    unittest.main()