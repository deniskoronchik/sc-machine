#include "server_config.hpp"

ServerConfig::ServerConfig(boost::program_options::variables_map && vm)
  : m_varMap(std::move(vm))
{
}

std::string ServerConfig::StorageConfigPath() const
{
  return GetValue<std::string>(kStorageConfigPath, "");
}

std::string ServerConfig::StorageExtPath() const
{
  return GetValue<std::string>(kStorageExtPath, "");
}

std::string ServerConfig::StorageRepoPath() const
{
  return GetValue<std::string>(kStorageRepoPath, "repo");
}

bool ServerConfig::IsStorageClear() const
{
  return GetValue<bool>(kStorageClear, false);
}
