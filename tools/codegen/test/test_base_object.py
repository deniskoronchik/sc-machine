import unittest

import cpp_parser as cpp

class TestBaseObject(unittest.TestCase):
  
  def test_namespace(self):
    obj = cpp.BaseObject('MyClass', [])
    self.assertEqual(obj.get_namespace_str(), '')

    obj = cpp.BaseObject('MyClass', ['sc', 'scp'])
    self.assertEqual(obj.get_namespace_str(), 'sc::scp')

  def test_full_name(self):
    obj = cpp.BaseObject('MyClass', [])
    self.assertEqual(obj.get_fullname(), 'MyClass')

    obj = cpp.BaseObject('MyClass', ['sc', 'scp'])
    self.assertEqual(obj.get_fullname(), 'sc::scp::MyClass')
