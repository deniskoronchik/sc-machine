import unittest

import cpp_parser as cpp

class TestField(unittest.TestCase):

  def test_construct(self):
    field = cpp.Field(name='myField', is_const=False)
    self.assertEqual(field.name, 'myField')
    self.assertEqual(field.is_const, False)

    field = cpp.Field(name='myField', is_const=True)
    self.assertEqual(field.is_const, True)
    