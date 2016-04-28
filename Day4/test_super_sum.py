""" Test suite for super_sum  """
from unittest import TestCase
from super_sum import super_sum


class TestSuperSum(TestCase):
    """  Test Case for super_sum function """

    def test_empty_input(self):
        # self.assertEqual("Please Enter Numbers", super_sum())
        self.assertEqual(0, super_sum())

    def test_sum_of_integers(self):
        """  Test sum of integers """
        # super_sum(1,2,3) ==> 6
        """ Argument number one should be equal to argument number two"""
        self.assertEqual(super_sum(1, 2, 3), 6)

    def test_sum_of_items_in_one_list(self):
        """  Test sum of items in a single list """
        self.assertEqual(super_sum([10, 20, 30]), 60)

    def test_sum_of_list_of_tuple(self):
        self.assertEqual(super_sum([2], [3], [4]), 9)
