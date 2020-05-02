import clang.cindex as ci

from cpp_parser.meta_parser import ParseMeta
import cpp_parser.types as types

class ClassParser:

  def parse(self, cursor: ci.Cursor) -> types.Klass:
  
    base_classes = []
    fields = []
    class_attrs = {}
    for child in cursor.get_children():
      if child.kind == ci.CursorKind.CXX_BASE_SPECIFIER:
        base_classes.append(child.type.spelling)
      elif child.kind == ci.CursorKind.FIELD_DECL:
        member = self.parse_field(child)
        fields.append(member)
      elif child.kind == ci.CursorKind.CXX_METHOD:
        if child.spelling == '__null_meta':
          class_attrs = ParseMeta(child)

    return types.Klass(
      name=cursor.spelling,
      base_classes=base_classes,
      fields=fields,
      attrs=class_attrs)
    

  def parse_field(self, cursor: ci.Cursor) -> types.Field:
    
    name = cursor.displayname
    if not name or len(name) == 0:
      name = cursor.spelling
    meta = ParseMeta(cursor)

    return types.Field(
      name=name, 
      is_const=cursor.type.is_const_qualified(),
      is_static=cursor.is_static_method,
      attrs=meta)

def ParseClass(cursor: ci.Cursor) -> types.Klass:
  return ClassParser().parse(cursor)