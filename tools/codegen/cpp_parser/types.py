import typing

from enum import Enum


class BaseObject:
  def __init__(self, name: str='', namespaces=[], attrs={}, parent=None):
    self._name = name
    self._namspaces = namespaces
    self._attrs = attrs
    self._parent = parent

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

  @property
  def parent(self):
    return self._parent

  @parent.setter
  def parent(self, value):
    self._parent = value

  def __str__(self):
    return '{} - name: {}, parent: {}, attrs: {}'.format(
      self.__class__.__name__,
      self.get_fullname(),
      self.parent.get_fullname() if self.parent else 'None',
      self.attrs
      )

class Field(BaseObject):

  def __init__(self, is_const: bool = False, **kwargs):
    BaseObject.__init__(self, **kwargs)

    self._is_const = is_const

  @property
  def is_const(self) -> bool:
    return self._is_const

  def __str__(self) -> str:
    base_str = BaseObject.__str__(self)
    return '{}, is_const: {}'.format(base_str, self.is_const)
  
class Klass(BaseObject):

  def __init__(self, **kwargs):
    BaseObject.__init__(self, **kwargs)

    self._base_classes = []
    self._fields = []
  
  @property
  def base_classes(self) -> [str]:
    return self._base_classes

  @base_classes.setter
  def base_classes(self, classes: [str]):
    self._base_classes = classes

  @property
  def fields(self) -> [Field]:
    return self._fields

  @fields.setter
  def fields(self, value: [Field]):
    self._fields = value


  def __str__(self) -> str:
    base_str = BaseObject.__str__(self)
    fields_str = 'fields: '
    for f in self.fields:
      fields_str += '\n  {}'.format(str(f))
    
    return '{}, base: {}\n{}'.format(
      base_str,
      self._base_classes,
      fields_str
      )

class Struct(Klass):

  def __init__(self, **kwargs):
    Klass.__init__(self, **kwargs)



class Function(BaseObject):

  def __init__(self, is_static=False, is_const=False, **kwargs):

    BaseObject.__init__(self, **kwargs)

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
  def is_static(self) -> bool:
    return self._is_static

  @property
  def is_const(self) -> bool:
    return self._is_const

  def __str__(self):
    return '{}, is_method: {}, is_static: {}, is_const: {}'.format(
      BaseObject.__str__(self),
      self.is_method,
      self.is_static,
      self.is_const
    )
