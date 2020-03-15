import unittest

import cpp_parser as cpp

class TestBaseObject(unittest.TestCase):
  
  def test_namespace(self):
    obj = cpp.BaseObject('MyClass')
    self.assertEqual(obj.get_namespace_str(), '')

    obj = cpp.BaseObject('MyClass', namespaces=['sc', 'scp'])
    self.assertEqual(obj.get_namespace_str(), 'sc::scp')

  def test_full_name(self):
    obj = cpp.BaseObject('MyClass')
    self.assertEqual(obj.get_fullname(), 'MyClass')

    obj = cpp.BaseObject('MyClass', namespaces=['sc', 'scp'])
    self.assertEqual(obj.get_fullname(), 'sc::scp::MyClass')

  def test_attrs(self):
    obj = cpp.BaseObject('MyClass', attrs={
      'attr1': 'value1'
    })

    self.assertEqual(obj.attrs['attr1'], 'value1')
