import unittest
import os

import cpp_parser as cpp

from cpp_parser.tools import clang_init

def get_test_path():
  return os.path.dirname(os.path.abspath(__file__))

def get_test_file_path(file_name):
  return os.path.join(get_test_path(), 'test_sources', file_name)

def get_sc_memory_path():
  return os.path.normpath(os.path.join(get_test_path(), '..', '..', '..', 'sc-memory'))

def get_common_parse_flags():
  return [
    '-D__SC_REFLECTION_PARSER__',
    '-I{}'.format(get_sc_memory_path())
  ]

# Initialize clang library
clang_init()

class TestParser(unittest.TestCase):
  

  def test_invalid_file(self):
    parser = cpp.Parser()

    res = parser.parse('unknown file path', flags=[], is_debug=False)

    self.assertFalse(res)


  def test_attrs_parse(self):
    parser = cpp.Parser()

    flags = get_common_parse_flags()
    res = parser.parse(get_test_file_path('meta.hpp'), flags=flags, is_debug=True)
   
    self.assertTrue(res)

    self.assertEqual(len(parser.classes), 1)

    cl = parser.classes[0]
    self.assertEqual(cl.name, 'MyClass')
    self.assertEqual(len(cl.base_classes), 1)
    self.assertEqual(cl.base_classes[0], 'ScObject')
    self.assertEqual(cl.gen_body_line, 11)

    self.assertEqual(cl.attrs['Attr_No_Value'], True)
    self.assertEqual(cl.attrs['Attr_Str'], '\"str_value\"')
    self.assertEqual(cl.attrs._user_attrs_count(), 2)

    self.assertEqual(len(cl.fields), 3)
    field = cl.fields[0]
    self.assertEqual(field.name, 'm_member')
    self.assertEqual(field.attrs._user_attrs_count(), 2)
    self.assertEqual(field.attrs['Attr_With_Value'], 'value_1')
    self.assertEqual(field.attrs['Attr_No_Value'], True)    
    self.assertFalse(field.is_static)

    keynode = cl.fields[1]
    self.assertEqual(keynode.name, 'm_keynode')
    self.assertEqual(keynode.attrs._user_attrs_count(), 2)
    self.assertEqual(keynode.attrs['ForceCreate'], 'ScType::NodeConst')
    self.assertEqual(keynode.attrs['Keynode'], '\"keynode\"')
    
    self.assertTrue(keynode.is_keynode)
    self.assertEqual(keynode.keynode_idtf, 'keynode')
    self.assertEqual(keynode.keynode_type, 'ScType::NodeConst')

    template = cl.fields[2]
    self.assertEqual(template.name, 'm_template')
    self.assertEqual(template.attrs._user_attrs_count(), 1)
    self.assertTrue(template.is_template)
    self.assertEqual(template.template_value, 'template_idtf')
    
    
