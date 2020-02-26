
import clang.cindex as ci
import cpp_parser.types as types

from cpp_parser.class_parser import ClassParser

class Parser:

  def __init__(self):
    self.classes = []
    self.structs = []
    self.functions = []
   
  def parse(self, file_path, flags: str = ''):
    
    arguments = flags.split(';')

    tu = ci.TranslationUnit.from_source(
      file_path,
      args=['-std=c++17'].extend(arguments),
      options=ci.TranslationUnit.PARSE_SKIP_FUNCTION_BODIES # | 
      # 0x400 # CXTranslationUnit_SingleFileParse 
      # https://clang.llvm.org/doxygen/group__CINDEX__TRANSLATION__UNIT.html#ggab1e4965c1ebe8e41d71e90203a723fe9a96401c77684f532f62e848e78c965886
    )

    for cursor in tu.cursor.get_children():
      if cursor.kind == ci.CursorKind.CLASS_DECL:
        self.classes.append(ClassParser().parse(cursor))

    return tu is not None

  def print_objects(self):

    print ('-'* 5, 'Classes')
    for c in self.classes:
      print (c)