#pragma once

#include "request_handler.hpp"

#include <boost/array.hpp>
#include <boost/asio.hpp>
#include <boost/noncopyable.hpp>
#include <boost/shared_ptr.hpp>
#include <boost/enable_shared_from_this.hpp>

#include <atomic>
#include <cstdint>
#include <queue>
#include <vector>

namespace impl
{

class Session :
    public boost::enable_shared_from_this<Session>,
    private boost::noncopyable
{
public:
  explicit Session(boost::asio::io_service & ioService, std::shared_ptr<AuthService> authService);

  void Start();

  uint32_t ID() const { return m_id; };

  boost::asio::ip::tcp::socket & Socket();

protected:
  void ReadSocket();

  void ProcessPacket();

  void HandleRead(boost::system::error_code const & error, size_t bytesTransfered);
  void HandleWrite(boost::system::error_code const & error);

  // Adds session info to string message
  std::string MakeMessage(std::string const & msg) const;

private:
  static std::atomic_uint32_t ms_idCounter;

  // Session id
  uint32_t m_id = 0;
  // Strand to ensure the connection's handlers are not called concurrently.
  boost::asio::io_service::strand m_strand;
  // Socket for the connection.
  boost::asio::ip::tcp::socket m_socket;
  // Buffer for incoming data.
  boost::array<char, 8192> m_buffer;

  // Packets
  struct Packet
  {
    uint32_t received = 0;
    uint32_t size = 0;
    std::vector<uint8_t> data;

    explicit Packet(size_t sz)
      : size(sz)
    {
      data.resize(size);
    }

    inline bool IsReceived() const
    {
      return received == size;
    }

    using Ptr = std::unique_ptr<Packet>;
  };

  std::vector<uint8_t> m_partialData;
  std::unique_ptr<Packet> m_packet;
  RequestHandler m_handler;
};

using SessionPtr = boost::shared_ptr<Session>;

} // namespace impl
