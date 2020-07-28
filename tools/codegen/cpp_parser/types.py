import typing

from enum import Enum

class Attributes:

  def __init__(self, attrs: dict = {}):
    self._attrs = dict(attrs)

  def __getitem__(self, key):
    try:
      return self._attrs[key]
    except KeyError:
      return None

  def __setitem__(self, key, value):
    self._attrs[key] = value

  def __len__(self):
    return len(self._attrs)

  def __str__(self):
    return str(self._attrs)

  def __contains__(self, item):
    return item in self._attrs

  # unittest support
  def _user_attrs_count(self):
    result = 0
    for k in self._attrs.keys():
      if k.startswith('$'):
        continue
      result += 1
    
    return result

class BaseObject:
  def __init__(self, name: str='', namespaces=[], attrs={}, parent=None):
    self._name = name
    self._namspaces = namespaces
    if isinstance(attrs, dict):
      self._attrs = Attributes(attrs=attrs)
    elif isinstance(attrs, Attributes):
      self._attrs = attrs
    else:
      raise 'attrs parameter should have on of two types: Attributes or dict'

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
  def attrs(self) -> Attributes:
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
      str(self.attrs)
      )

class Field(BaseObject):

  def __init__(self, is_const: bool = False, is_static: bool = False, **kwargs):
    BaseObject.__init__(self, **kwargs)

    self._is_const = is_const
    self._is_static = is_static

  @property
  def is_const(self) -> bool:
    return self._is_const

  @property
  def is_static(self) -> bool:
    return self._is_static

  @property
  def is_keynode(self) -> bool:
    return 'Keynode' in self.attrs

  @property
  def is_template(self) -> bool:
    return 'Template' in self.attrs

  @property
  def keynode_type(self) -> str:
    try:
      return self.attrs['ForceCreate']
    except KeyError:
      pass

    return 'ScType::Node'

  @property
  def keynode_idtf(self) -> str:
    try:
      return self.attrs['Keynode']
    except KeyError:
      pass

    return None

  @property
  def template_value(self) -> str:
    try:
      return self.attrs['Template']
    except KeyError:
      pass

    return None
  
  @property
  def has_force_type(self) -> str:
    return 'ForceCreate' in self.attrs

  def __str__(self) -> str:
    base_str = BaseObject.__str__(self)
    return '{}, is_const: {}, is_static: {}, attrs: {}'.format(base_str, self.is_const, self.is_static, self.attrs)
  
class Klass(BaseObject):

  MetaBody = 'GenBody'

  def __init__(self, base_classes: [str]=[], fields: [Field]=[], **kwargs):
    BaseObject.__init__(self, **kwargs)

    self._base_classes = base_classes
    self._fields = fields
    for f in self._fields:
      f.parent = self
  
  @property
  def base_classes(self) -> [str]:
    return self._base_classes

  @property
  def fields(self) -> [Field]:
    return self._fields

  @property
  def gen_body_line(self) -> int:
    res = self.attrs['$line_number']
    assert res
    return res
    
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
