#pragma once

#include <atomic>
#include <memory>

class ServerConfig;

class Server final
{
public:
  explicit Server(std::unique_ptr<ServerConfig> && config);
  ~Server();

  void Run();
  void Stop();

private:
  void StartStorage();
  void StopStorage();

private:
  std::unique_ptr<ServerConfig> m_config;
  std::atomic_bool m_isRunning = { true };
};
