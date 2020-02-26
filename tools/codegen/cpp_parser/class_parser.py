import clang.cindex as ci
import cpp_parser.types as types

class ClassParser:

  def parse(self, cursor: ci.Cursor) -> types.Klass:

    result = types.Klass(name=cursor.displayname)

    return result