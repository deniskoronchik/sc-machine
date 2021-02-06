#include "server.hpp"

#include <boost/thread/thread.hpp>
#include <boost/bind.hpp>
#include <boost/shared_ptr.hpp>

#include <sc-memory/utils/sc_log.hpp>

#include <thread>
#include <vector>

namespace impl
{

Server::Server(std::string const & host, uint16_t port, uint16_t threadsNum)
  : m_threadsNum(threadsNum)
  , m_signals(m_ioService)
  , m_acceptor(m_ioService)
{
  // Register to handle the signals that indicate when the server should exit.
  // It is safe to register for the same signal multiple times in a program,
  // provided all registration for the specified signal is made through Asio.
  m_signals.add(SIGINT);
  m_signals.add(SIGTERM);
#if defined(SIGQUIT)
  m_signals.add(SIGQUIT);
#endif // defined(SIGQUIT)
  m_signals.async_wait(boost::bind(&Server::HandleStop, this));

  // Open the acceptor with the option to reuse the address (i.e. SO_REUSEADDR).
  boost::asio::ip::tcp::resolver resolver(m_ioService);
  boost::asio::ip::tcp::resolver::query query(host, std::to_string(port));
  boost::asio::ip::tcp::endpoint endpoint = *resolver.resolve(query);
  m_acceptor.open(endpoint.protocol());
  m_acceptor.set_option(boost::asio::ip::tcp::acceptor::reuse_address(true));
  m_acceptor.bind(endpoint);
  m_acceptor.listen();

  StartAccept();
}

void Server::Run()
{
  size_t threadsNum = m_threadsNum;

  // use number of cores on device
  if (threadsNum == 0)
  {
    threadsNum = std::thread::hardware_concurrency();
    // if wasn't able to determine setup default
    if (threadsNum == 0)
      threadsNum = 1;
  }

  SC_LOG_INFO("Start server with " << threadsNum << " threads");

  // Create a pool of threads to run all of the io_services.
  std::vector<boost::shared_ptr<boost::thread> > threads;
  threads.reserve(threadsNum);
  for (size_t i = 0; i < threadsNum; ++i)
  {
    boost::shared_ptr<boost::thread> thread(new boost::thread(boost::bind(&boost::asio::io_service::run, &m_ioService)));
    threads.emplace_back(thread);
  }

  // Wait for all threads in the pool to exit.
  for (size_t i = 0; i < threads.size(); ++i)
    threads[i]->join();
}

void Server::StartAccept()
{
  SessionPtr session(new Session(m_ioService));

  m_acceptor.async_accept(
        session->Socket(),
        boost::bind(&Server::HandleAccept, this, session,
        boost::asio::placeholders::error));
}

void Server::HandleAccept(SessionPtr newSession, boost::system::error_code const & error)
{
  if (!error)
  {
    newSession->Start();
    SC_LOG_INFO_COLOR("New connection. Session ID = " << newSession->ID(),
                      ScConsole::Color::Green);
  }

  StartAccept();
}

void Server::HandleStop()
{
  SC_LOG_INFO_COLOR("Stopping server...",
                    ScConsole::Color::Green);
  m_ioService.stop();
}

} // namespace impl
