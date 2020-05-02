#include "sc-memory/sc_defines.hpp"
#include "sc-memory/sc_object.hpp"
#include "sc-memory/sc_addr.hpp"

#include <string>

class MyClass : public ScObject
{
  SC_CLASS(Attr_No_Value, Attr_Str("str_value"))
  SC_GENERATED_BODY()

private:
  SC_PROPERTY(Attr_With_Value("value_1"), Attr_No_Value)
  int m_member;
};
