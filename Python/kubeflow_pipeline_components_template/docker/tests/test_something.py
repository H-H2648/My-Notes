import unittest
from unittest.mock import patch # for temporarily creating output value with some predetermined attributes without looking up things online
class TestSomething(unittest.TestCase):

    # test some function

    self.assertEqual(
        output_of_some_function,
        expected_output,
    )