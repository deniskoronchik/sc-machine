#pragma once

#include "sc_addr.hpp"
#include "sc_type.hpp"

class ScStorageInterface
{
public:
  virtual ScAddr CreateNode(ScType const & type) = 0;
  virtual ScAddr CreateLink(ScType const & type = ScType::LinkConst) = 0;
  virtual ScAddr CreateEdge(ScType const & type, ScAddr const & addrBeg, ScAddr const & addrEnd) = 0;

  virtual ScType GetElementType(ScAddr const & addr) const = 0;
};
