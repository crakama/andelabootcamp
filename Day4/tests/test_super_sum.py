""" Test suite for super_sum  """

import unittest
from super_sum import super_sum


class TestSuperSum(unittest.TestCase):

    """  Test Case for super_sum function """

    def test_empty_input(self):
        self.assertEqual(super_sum(), "Please Enter Numbers")
