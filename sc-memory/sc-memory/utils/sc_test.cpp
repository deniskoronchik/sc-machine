/*
* This source file is part of an OSTIS project. For the latest info, see http://ostis.net
* Distributed under the MIT License
* (See accompanying file COPYING.MIT or copy at http://opensource.org/licenses/MIT)
*/

#include "sc_test.hpp"

namespace test
{

std::set<ScTestUnit*, ScTestUnit::TestLess> ScTestUnit::ms_tests;
uint32_t ScTestUnit::ms_subtestsNum = 0;

ScTestUnit::ScTestUnit(char const * name, char const * filename, void(*fn)())
  : m_name(name)
  , m_filename(filename)
  , m_fn(fn)
{
  ms_tests.insert(this);
}

ScTestUnit::~ScTestUnit() 
{
  ms_tests.erase(this);
}

void ScTestUnit::Run(std::string const & configPath, std::string const & extPath)
{
  ScConsole::Print() << "Run test " << ScConsole::Color::LightBlue
                     << m_name << " ... ";

  uint32_t const prevSubtests = ms_subtestsNum;

  InitMemory(configPath, extPath);

  ScMemory::LogMute();

  if (m_fn)
    m_fn();

  ScMemory::LogUnmute();

  ShutdownMemory(false);

  if (prevSubtests == ms_subtestsNum)
    ScConsole::Print() << SC_TEST_STATUS_COLOR(true) << SC_TEST_STATUS(true);

  std::cout << std::endl;
}

void ScTestUnit::InitMemory(std::string const & configPath, std::string const & extPath)
{
  sc_memory_params params;
  sc_memory_params_clear(&params);

  params.clear = SC_TRUE;
  params.repo_path = "repo";
  params.config_file = configPath.c_str();
  params.ext_path = extPath.empty() ? nullptr : extPath.c_str();

  ScMemory::LogMute();
  ScMemory::Initialize(params);
  ScMemory::LogUnmute();
}

void ScTestUnit::ShutdownMemory(bool save)
{
  ScMemory::LogMute();
  ScMemory::Shutdown(save);
  ScMemory::LogUnmute();
}

void ScTestUnit::RunAll(std::string const & configPath, std::string const & extPath)
{
  ScConsole::Print() << "Run " << ScConsole::Color::Green << ms_tests.size() << ScConsole::Color::Reset << " tests";
  ScConsole::Endl();

  for (ScTestUnit * unit : ms_tests)
    unit->Run(configPath, extPath);

  ScConsole::Print() << "Passed "
                     << ScConsole::Color::Green << ms_subtestsNum << ScConsole::Color::Reset << " subtests in "
                     << ScConsole::Color::Green << ms_tests.size() << ScConsole::Color::Reset << " tests";
  ScConsole::Endl();
}

void ScTestUnit::NotifySubTest()
{
  ++ms_subtestsNum;
}


} // namespace test
