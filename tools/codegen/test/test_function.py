import unittest

import cpp_parser as cpp

class TestFunction(unittest.TestCase):

  def test_params(self):
    func = cpp.Function(name='myFunc', is_static=False, is_const=False)
    self.assertEqual(func.get_fullname(), 'myFunc')
    self.assertEqual(func.is_const, False)
    self.assertEqual(func.is_static, False)
    self.assertEqual(func.is_method, False)

    obj = cpp.Klass(name='MyClass', namespaces=['sc', 'scp'])
    func = cpp.Function(name='myFunc', is_static=True, is_const=True, parent=obj)
    self.assertEqual(func.get_fullname(), 'sc::scp::MyClass::myFunc')
    self.assertEqual(func.is_const, True)
    self.assertEqual(func.is_static, True)
    self.assertEqual(func.is_method, True)
