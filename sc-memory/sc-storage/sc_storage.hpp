#pragma once

#include "sc_storage_api.hpp"

#include "sc-memory/sc_storage_interface.hpp"

class SC_STORAGE_API ScStorage final : public ScStorageInterface
{
public:
  ScAddr CreateNode(ScType const & type) override;
  ScAddr CreateLink(ScType const & type = ScType::LinkConst) override;
  ScAddr CreateEdge(ScType const & type, ScAddr const & source, ScAddr const & target) override;

  ScType GetElementType(ScAddr const & addr) const override;
};
