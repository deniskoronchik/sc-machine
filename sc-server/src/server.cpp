#include "server.hpp"

#include "server_config.hpp"

#include <sc-memory/sc_memory.hpp>
#include <sc-memory/utils/sc_log.hpp>

#include <thread>

Server::Server(std::unique_ptr<ServerConfig> && config)
  : m_config(std::move(config))
{
}

Server::~Server()
{
}

void Server::Run()
{
  m_isRunning = true;

  StartStorage();

  while (m_isRunning)
  {
    std::this_thread::sleep_for(std::chrono::milliseconds(1000));
  }

  StopStorage();
}

void Server::Stop()
{
  m_isRunning = false;
}

void Server::StartStorage()
{
  SC_LOG_COLOR(utils::ScLog::Type::Info,
               "Initialize sc-memory",
               ScConsole::Color::Green);

  std::string const configPath = m_config->StorageConfigPath();
  std::string const extPath = m_config->StorageExtPath();
  std::string const repoPath = m_config->StorageRepoPath();

  sc_memory_params params;
  sc_memory_params_clear(&params);

  params.clear = m_config->IsStorageClear() ? SC_TRUE : SC_FALSE;
  params.config_file = configPath.c_str();
  params.enabled_exts = nullptr;
  params.ext_path = extPath.c_str();
  params.repo_path = repoPath.c_str();

  ScMemory::Initialize(params);
}

void Server::StopStorage()
{
  SC_LOG_COLOR(utils::ScLog::Type::Info,
               "Shutdown sc-memory",
               ScConsole::Color::Green);

  ScMemory::Shutdown(true);
}
