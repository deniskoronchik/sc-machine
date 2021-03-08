#include "server.hpp"

#include "impl/server.hpp"
#include "server_config.hpp"

#include <boost/asio.hpp>

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
  SC_LOG_INFO_COLOR("Run server with configuration: ", ScConsole::Color::Green);
  m_config->LogConfig();

  StartStorage();

  m_impl = std::make_unique<impl::Server>(
        m_config->ServerHost(),
        m_config->ServerPort(),
        m_config->ServerThreads(),
        m_config->ServerUserDB());

  m_impl->Run();

  StopStorage();
}

void Server::StartStorage()
{
  SC_LOG_INFO_COLOR("Initialize sc-memory", ScConsole::Color::Green);

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
  SC_LOG_INFO_COLOR("Shutdown sc-memory", ScConsole::Color::Green);

  ScMemory::Shutdown(true);
}
