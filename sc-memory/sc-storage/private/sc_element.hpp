#pragma once

#include <array>
#include <cstdint>


struct ScElement
{
  using TypeValue = uint16_t;
  using AddrValue = uint64_t;

  struct EdgeData
  {
    AddrValue m_source;
    AddrValue m_target;
    AddrValue m_nextOut; // AddrValue of next output edge in a list
    AddrValue m_nextIn;  // AddrValue of next input edge in a list
    AddrValue m_prevOut; // AddrValue of pevious output edge in a list
    AddrValue m_prevIn;  // AddrValue of previous input edge in a list
  };

  struct LinkData
  {
    std::array<uint8_t, 48> m_data;
  };

  TypeValue m_type;

  AddrValue m_outEdges;
  AddrValue m_inEdges;

  union
  {
    EdgeData m_edge;
    LinkData m_link;
  };
};
