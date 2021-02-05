#pragma once

#include <boost/program_options/variables_map.hpp>

class ServerConfig final
{
public:
  std::string const kStorageClear = "storage.clear";
  std::string const kStorageConfigPath = "storage.config_path";
  std::string const kStorageExtPath = "storage.ext_path";
  std::string const kStorageRepoPath = "storage.repo_path";

public:
  explicit ServerConfig(boost::program_options::variables_map && vm);

  std::string StorageConfigPath() const;
  std::string StorageExtPath() const;
  std::string StorageRepoPath() const;
  bool IsStorageClear() const;

  void LogConfig();

private:
  template <typename Type>
  Type GetValue(std::string const & key, Type defaultValue) const
  {
    if (m_varMap.count(key))
      return m_varMap[key].as<Type>();

    return defaultValue;
  }

private:
  boost::program_options::variables_map m_varMap;
};
