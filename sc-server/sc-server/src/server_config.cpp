#include "server_config.hpp"

#include <sc-memory/utils/sc_log.hpp>

ServerConfig::ServerConfig(boost::program_options::variables_map && vm)
  : m_varMap(std::move(vm))
{
}

std::string ServerConfig::StorageConfigPath() const
{
  return GetValue<std::string>(kStorageConfigPath);
}

std::string ServerConfig::StorageExtPath() const
{
  return GetValue<std::string>(kStorageExtPath);
}

std::string ServerConfig::StorageRepoPath() const
{
  return GetValue<std::string>(kStorageRepoPath);
}

bool ServerConfig::IsStorageClear() const
{
  return GetValue<bool>(kStorageClear);
}

std::string ServerConfig::ServerHost() const
{
  return GetValue<std::string>(kServerHost);
}

uint16_t ServerConfig::ServerPort() const
{
  return GetValue<uint16_t>(kServerPort);
}

uint16_t ServerConfig::ServerThreads() const
{
  return GetValue<uint16_t>(kServerThreads);
}

std::string ServerConfig::ServerUserDB() const
{
  return GetValue<std::string>(kServerUserDB);
}

void ServerConfig::LogConfig()
{
  for (auto const & it : m_varMap)
  {
    std::stringstream ss;
    boost::any const value = (boost::any)it.second.value();

    ss << it.first;
    if (value.empty())
      ss << "(empty)";

    if (it.second.defaulted())
      ss << "(default)";

    ss << " = ";

    bool is_char;
    try
    {
      boost::any_cast<const char *>(it.second.value());
      is_char = true;
    }
    catch (const boost::bad_any_cast &)
    {
      is_char = false;
    }
    bool is_str;
    try
    {
      boost::any_cast<std::string>(it.second.value());
      is_str = true;
    }
    catch (const boost::bad_any_cast &)
    {
      is_str = false;
    }

    if (value.type() == typeid(int))
    {
      ss << it.second.as<int>();
    }
    else if (value.type() == typeid(bool))
    {
      ss << it.second.as<bool>();
    }
    else if (value.type() == typeid(double))
    {
      ss << it.second.as<double>();
    }
    else if (value.type() == typeid(uint16_t))
    {
      ss << it.second.as<uint16_t>();
    }
    else if (is_char)
    {
      ss << it.second.as<const char * >();
    }
    else if (is_str)
    {
      std::string const temp = it.second.as<std::string>();
      if (temp.size())
        ss << temp;
      else
        ss << "true";
    }
    else
    {
      ss << "UnknownType(" << value.type().name() << ")";
    }

    SC_LOG_INFO(ss.str());
  }
}
