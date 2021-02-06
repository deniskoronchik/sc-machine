#pragma once

#include "session.hpp"

#include <boost/asio.hpp>
#include <boost/noncopyable.hpp>

#include <cstdint>
#include <string>

namespace impl
{

class Server : public boost::noncopyable
{
public:
  Server(std::string const & host, uint16_t port, uint16_t threadsNum);

  void Run();

private:
  void StartAccept();

  void HandleAccept(SessionPtr newSession,
                    boost::system::error_code const & error);
  void HandleStop();

private:
  std::uint16_t m_threadsNum;
  boost::asio::io_service m_ioService;
  boost::asio::signal_set m_signals;
  boost::asio::ip::tcp::acceptor m_acceptor;
};

} // namespace impl
