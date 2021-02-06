#pragma once

#include <atomic>
#include <memory>

class ServerConfig;
namespace impl
{
class Server;
} // namespace impl

class Server final
{
public:
  explicit Server(std::unique_ptr<ServerConfig> && config);
  ~Server();

  void Run();

private:
  void StartStorage();
  void StopStorage();

private:
  std::unique_ptr<ServerConfig> m_config;
  std::unique_ptr<impl::Server> m_impl;
};
