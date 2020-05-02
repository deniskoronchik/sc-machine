import typing


import clang.cindex as ci
import cpp_parser.types as types

from cpp_parser.class_parser import ParseClass

class Parser:

  def __init__(self):
    self.classes = []
    self.structs = []
    self.functions = []
   
  def parse(self, file_path, flags: [str] = [], is_debug: bool = False):

    args = ['-std=c++17']
    args.extend(flags)

    try:
      tu = ci.TranslationUnit.from_source(
        file_path,
        args=args,
        options=ci.TranslationUnit.PARSE_SKIP_FUNCTION_BODIES # | 
        # 0x400 # CXTranslationUnit_SingleFileParse 
        # https://clang.llvm.org/doxygen/group__CINDEX__TRANSLATION__UNIT.html#ggab1e4965c1ebe8e41d71e90203a723fe9a96401c77684f532f62e848e78c965886
      )
    except ci.TranslationUnitLoadError:
      if is_debug:
        print ("Can't open source file: {}".format(file_path))
      
      return False

    for cursor in tu.cursor.get_children():
      # skip everything from included files
      if str(cursor.location.file) != file_path:
        continue

      if cursor.kind == ci.CursorKind.CLASS_DECL:
        self.classes.append(ParseClass(cursor=cursor))

    if is_debug and len(tu.diagnostics) > 0:
      print ('\n', '-' * 10, '\nParse errors:')
      for msg in tu.diagnostics:
        print (msg)

    return tu is not None

  def print_objects(self):

    print ('-'* 5, 'Classes')
    for c in self.classes:
      print (c)