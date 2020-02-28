import clang.cindex as ci
import cpp_parser.types as types

class ClassParser:

  def parse(self, cursor: ci.Cursor) -> types.Klass:

    result = types.Klass(name=cursor.spelling)

    base_classes = []
    fields = []
    for child in cursor.get_children():
      if child.kind == ci.CursorKind.CXX_BASE_SPECIFIER:
        base_classes.append(cursor.canonical.displayname)
      elif child.kind == ci.CursorKind.FIELD_DECL:
        member = self.parse_field(child)
        member.parent = result
        fields.append(member)

    result.base_classes = base_classes
    result.fields = fields

    return result

  def parse_field(self, cursor: ci.Cursor) -> types.Field:
    
    name = cursor.displayname
    if not name or len(name) == 0:
      name = cursor.spelling

    return types.Field(name=name, is_const=cursor.type.is_const_qualified())