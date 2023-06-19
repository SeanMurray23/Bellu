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
    
    def test_construction_no_args(self):
        s = SortedFrozenSet()


class TestContainerProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedFrozenSet([6,7,3,9])
    
    def test_positive_contained(self):
        self.assertTrue(6 in self.s)

    def test_negative_contained(self):
        self.assertFalse(2 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(5 not in self.s)
    
    def test_negative_not_contained(self):
        self.assertFalse(9 not in self.s)



if __name__ == '__main__':
    unittest.main()