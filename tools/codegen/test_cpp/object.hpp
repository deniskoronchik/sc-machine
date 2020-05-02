#include <sc-memory/sc_object.hpp>

#include "object.generated.hpp"

class Object : public ScObject
{
  SC_CLASS()
  SC_GENERATED_BODY()

private:
  SC_PROPERTY(Keynode("test_keynode"), ForceCreate)
  ScAddr m_keynode;
};