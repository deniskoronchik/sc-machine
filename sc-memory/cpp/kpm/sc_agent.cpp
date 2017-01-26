/*
* This source file is part of an OSTIS project. For the latest info, see http://ostis.net
* Distributed under the MIT License
* (See accompanying file COPYING.MIT or copy at http://opensource.org/licenses/MIT)
*/

#include "sc_agent.hpp"

#include "../sc_debug.hpp"

bool gInitializeResult = false;
bool gIsInitialized = false;

bool _resolveKeynodeImpl(ScMemoryContext & ctx, char const * str, ScAddr & outAddr)
{
  check_expr(ctx.isValid());

  return ctx.helperResolveSystemIdtf(str, outAddr, true);
}

bool ScAgentInit(bool force /* = false */)
{
  if (force || !gIsInitialized)
  {
    gInitializeResult = ScAgentAction::initGlobal();

    gIsInitialized = true;
  }

  return gInitializeResult;
}


ScAgent::ScAgent(char const * name, sc_uint8 accessLvl)
  : mMemoryCtx(accessLvl, name)
{
}

ScAgent::~ScAgent()
{
}

sc_result ScAgent::run(ScAddr const & listenAddr, ScAddr const & edgeAddr, ScAddr const & otherAddr)
{
  return SC_RESULT_ERROR;
}


// ---------------------------
ScAddr ScAgentAction::msCommandInitiatedAddr;
ScAddr ScAgentAction::msCommandProgressdAddr;
ScAddr ScAgentAction::msCommandFinishedAddr;
ScAddr ScAgentAction::msNrelResult;

ScAddr ScAgentAction::ms_keynodeScResultOk;
ScAddr ScAgentAction::ms_keynodeScResultError;
ScAddr ScAgentAction::ms_keynodeScResultErrorInvalidParams;
ScAddr ScAgentAction::ms_keynodeScResultErrorInvalidType;
ScAddr ScAgentAction::ms_keynodeScResultErrorIO;
ScAddr ScAgentAction::ms_keynodeScResultInvalidState;
ScAddr ScAgentAction::ms_keynodeScResultErrorNotFound;
ScAddr ScAgentAction::ms_keynodeScResultErrorNoWriteRights;
ScAddr ScAgentAction::ms_keynodeScResultErrorNoReadRights;

ScAgentAction::ScAgentAction(ScAddr const & cmdClassAddr, char const * name, sc_uint8 accessLvl)
  : ScAgent(name, accessLvl)
  , mCmdClassAddr(cmdClassAddr)

{
}

ScAgentAction::~ScAgentAction()
{
}

sc_result ScAgentAction::run(ScAddr const & listenAddr, ScAddr const & edgeAddr, ScAddr const & otherAddr)
{
  SC_UNUSED(otherAddr);

  ScAddr const cmdAddr = mMemoryCtx.getEdgeTarget(edgeAddr);
  if (cmdAddr.isValid())
  {
    if (mMemoryCtx.helperCheckArc(mCmdClassAddr, cmdAddr, sc_type_arc_pos_const_perm))
    {
      mMemoryCtx.eraseElement(edgeAddr);
      ScAddr progressAddr = mMemoryCtx.createEdge(sc_type_arc_pos_const_perm, msCommandProgressdAddr, cmdAddr);
      assert(progressAddr.isValid());
      ScAddr resultAddr = mMemoryCtx.createNode(sc_type_const | sc_type_node_struct);
      assert(resultAddr.isValid());

      sc_result const resCode = runImpl(cmdAddr, resultAddr);

      mMemoryCtx.eraseElement(progressAddr);

      ScAddr const commonEdge = mMemoryCtx.createEdge(sc_type_const | sc_type_arc_common, cmdAddr, resultAddr);
      SC_ASSERT(commonEdge.isValid(), ());
      ScAddr const edge = mMemoryCtx.createEdge(sc_type_arc_pos_const_perm, msNrelResult, commonEdge);
      SC_ASSERT(edge.isValid(), ());

      ScAddr const edgeResult = mMemoryCtx.createEdge(ScType::EdgeAccessConstPosPerm, GetResultCodeAddr(resCode), resultAddr);
      SC_ASSERT(edgeResult.isValid(), ());

      mMemoryCtx.createEdge(sc_type_arc_pos_const_perm, msCommandFinishedAddr, cmdAddr);

      return SC_RESULT_OK;
    }
  }

  return SC_RESULT_ERROR;
}

ScAddr ScAgentAction::getParam(ScAddr const & cmdAddr, ScAddr const & relationAddr, sc_type paramType)
{
  ScIterator5Ptr iter = mMemoryCtx.iterator5(cmdAddr,
                                             SC_TYPE(sc_type_arc_pos_const_perm),
                                             SC_TYPE(paramType),
                                             SC_TYPE(sc_type_arc_pos_const_perm),
                                             relationAddr);

  if (!iter->next())
    return ScAddr();

  return iter->value(2);
}

ScAddr const & ScAgentAction::GetCommandInitiatedAddr()
{
  return msCommandInitiatedAddr;
}

ScAddr const & ScAgentAction::GetCommandFinishedAddr()
{
  return msCommandFinishedAddr;
}

ScAddr const & ScAgentAction::GetNrelResultAddr()
{
  return msNrelResult;
}

ScAddr const & ScAgentAction::GetResultCodeAddr(sc_result resCode)
{
  switch (resCode)
  {
  case SC_RESULT_ERROR:
    return ms_keynodeScResultError;
  case SC_RESULT_OK:
    return ms_keynodeScResultOk;
  case SC_RESULT_ERROR_INVALID_PARAMS:
    return ms_keynodeScResultErrorInvalidParams;
  case SC_RESULT_ERROR_INVALID_TYPE:
    return ms_keynodeScResultErrorInvalidType;
  case SC_RESULT_ERROR_IO:
    return ms_keynodeScResultErrorIO;
  case SC_RESULT_ERROR_INVALID_STATE:
    return ms_keynodeScResultInvalidState;
  case SC_RESULT_ERROR_NOT_FOUND:
    return ms_keynodeScResultErrorNotFound;
  case SC_RESULT_ERROR_NO_WRITE_RIGHTS:
    return ms_keynodeScResultErrorNoWriteRights;
  case SC_RESULT_ERROR_NO_READ_RIGHTS:
    return ms_keynodeScResultErrorNoReadRights;
  };

  return ms_keynodeScResultError;
}