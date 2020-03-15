import unittest

import cpp_parser as cpp

class TestAttributes(unittest.TestCase):

  def test_construct(self):
    attrs = cpp.Attributes({'key_1': 1})

    self.assertEqual(len(attrs), 1)
    self.assertEqual(attrs['non_exist_key'], None)
    self.assertEqual(attrs['key_1'], 1)