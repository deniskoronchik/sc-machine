import clang.cindex as ci
import cpp_parser.types as types
import re

class MetaParser:

  def parse(self, cursor: ci.Cursor) -> types.Attributes:
    result = types.Attributes()

    # Add system attributes. All system attributes starts with '$'
    result['$line_number'] = cursor.location.line
    reg_expr = re.compile(r"(\s*(?P<attr>[a-zA-Z0-9_]+)(\(\"(?P<value>[^\"]*)\"\))?)([,]|$)")
    for child in cursor.get_children():
      if child.kind == ci.CursorKind.ANNOTATE_ATTR:
        # parse properties
        matches = reg_expr.finditer(child.displayname)
        for _, match in enumerate(matches):
          a = match.group('attr')
          v = match.group('value')
          result[a] = v if v is not None else True

    return result

def ParseMeta(cursor: ci.Cursor) -> types.Attributes:
  p = MetaParser()
  return p.parse(cursor)