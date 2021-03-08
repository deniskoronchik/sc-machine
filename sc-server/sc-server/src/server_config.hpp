#pragma once

#include <boost/program_options/variables_map.hpp>

class ServerConfig final
{
public:
  std::string const kStorageClear = "storage.clear";
  std::string const kStorageConfigPath = "storage.config_path";
  std::string const kStorageExtPath = "storage.ext_path";
  std::string const kStorageRepoPath = "storage.repo_path";

  std::string const kServerHost = "server.host";
  std::string const kServerPort = "server.port";
  std::string const kServerThreads = "server.threads";
  std::string const kServerUserDB = "server.user_db";

public:
  explicit ServerConfig(boost::program_options::variables_map && vm);

  std::string StorageConfigPath() const;
  std::string StorageExtPath() const;
  std::string StorageRepoPath() const;
  bool IsStorageClear() const;

  std::string ServerHost() const;
  uint16_t ServerPort() const;
  uint16_t ServerThreads() const;
  std::string ServerUserDB() const;

  void LogConfig();

private:
  template <typename Type>
  Type GetValue(std::string const & key) const
  {
    assert(m_varMap.count(key) > 0);
    return m_varMap[key].as<Type>();
  }

private:
  boost::program_options::variables_map m_varMap;
};
