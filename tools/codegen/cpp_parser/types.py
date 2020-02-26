import typing

from enum import Enum

class BaseObject:
  def __init__(self, name: str='', namespaces=[], attrs={}):
    self._name = name
    self._namspaces = namespaces
    self._attrs = attrs

  def get_namespace_str(self) -> str:
    return '::'.join(self._namspaces)

  def get_fullname(self) -> str:
    if len(self._namspaces) > 0:
      return self.get_namespace_str() + '::' + self._name

    return self._name

  @property
  def name(self) -> str:
    return self._name

  @property
  def attrs(self) -> dict:
    return self._attrs

  def __str__(self):
    return 'name: {}, attrs: {}'.format(self.get_fullname(), self.attrs)

  
class Klass(BaseObject):

  def __init__(self, **kwargs):
    BaseObject.__init__(self, **kwargs)


class Struct(BaseObject):

  def __init__(self, **kwargs):
    BaseObject.__init__(self, **kwargs)


ClassStruct = typing.Tuple[Klass, Struct]

class Function(BaseObject):

  def __init__(self, 
    is_static=False, is_const=False, 
    parent=None, **kwargs):

    BaseObject.__init__(self, **kwargs)

    if parent:
      assert isinstance(parent, Klass) or isinstance(parent, Struct)

    self._parent = parent
    self._is_static = is_static
    self._is_const = is_const    

  def get_fullname(self) -> str:
    if self._parent:
      return self._parent.get_fullname() + '::' + self._name
    
    return BaseObject.get_fullname(self)

  @property
  def is_method(self):
    return self._parent is not None

  @property
  def parent(self) -> ClassStruct:
    return self._parent

  @property
  def is_static(self) -> bool:
    return self._is_static

  @property
  def is_const(self) -> bool:
    return self._is_const

  def __str__(self):
    return '{}, parent: {}, is_method: {}, is_static: {}, is_const: {}'.format(
      BaseObject.__str__(self),
      self.parent.get_fullname() if self.parent else 'None',
      self.is_method,
      self.is_static,
      self.is_const
    )
