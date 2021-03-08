#include "session.hpp"

#include "auth_service.hpp"

#include <boost/bind.hpp>
#include <boost/logic/tribool.hpp>
#include <boost/tuple/tuple.hpp>

#include <sc-memory/sc_debug.hpp>

#include <sctp.pb.h>

size_t constexpr kPacketHeaderSize = 8;
uint32_t const kPacketWatermark = 's' << 3 | 'c' << 2 | 't' << 1 | 'p';

namespace impl
{

std::atomic_uint32_t Session::ms_idCounter = { 1 };

Session::Session(boost::asio::io_service & ioService, std::shared_ptr<AuthService> authService)
  : m_strand(ioService)
  , m_socket(ioService)
  , m_handler(authService)
{
  m_partialData.reserve(1024);
  m_id = ms_idCounter.fetch_add(1);
}

void Session::Start()
{
  ReadSocket();
}

boost::asio::ip::tcp::socket & Session::Socket()
{
  return m_socket;
}

void Session::ReadSocket()
{
  m_socket.async_read_some(boost::asio::buffer(m_buffer),
        m_strand.wrap(boost::bind(&Session::HandleRead, shared_from_this(),
                                  boost::asio::placeholders::error,
                                  boost::asio::placeholders::bytes_transferred)));
}

void Session::ProcessPacket()
{
  std::vector<uint8_t> reply;
  if (!m_handler.Handle(m_packet->data, reply))
    SC_THROW_EXCEPTION(utils::ExceptionCritical, "Error during package processing");

  uint32_t const replySize = reply.size();
  std::vector<uint8_t> packet(kPacketHeaderSize + replySize);
  uint8_t * data = packet.data();
  std::memcpy(data, &kPacketWatermark, sizeof(kPacketWatermark));
  data += sizeof(kPacketWatermark);
  std::memcpy(data, &replySize, sizeof(uint32_t));
  data += sizeof(uint32_t);
  std::memcpy(data, reply.data(), replySize);

  m_packet.reset();

  // Send response
  boost::asio::async_write(m_socket, boost::asio::buffer(packet),
            m_strand.wrap(boost::bind(&Session::HandleWrite, shared_from_this(),
                                      boost::asio::placeholders::error)));
}

void Session::HandleRead(boost::system::error_code const & error, size_t bytesTransfered)
{
  if (error)
  {
    if (error == boost::asio::error::eof)
    {
      SC_LOG_INFO_COLOR(MakeMessage("Disconnected"),
                        ScConsole::Color::Green);
    }
    else
    {
      SC_LOG_ERROR(MakeMessage(error.message()));
    }

    return;
  }

  SC_ASSERT(bytesTransfered > 0, ("Boost shouldn't call this function with zero bytes"));

  std::vector<uint8_t> joined;
  joined.resize(m_partialData.size() + bytesTransfered);
  std::memcpy(joined.data(), m_partialData.data(), m_partialData.size());
  std::memcpy(joined.data() + m_partialData.size(), m_buffer.data(), bytesTransfered);
  std::swap(m_partialData, joined);

  size_t processedBytes = 0;
  while (processedBytes < m_partialData.size())
  {
    size_t const remainBytes = m_partialData.size() - processedBytes;

    // try to start new packet
    if (!m_packet)
    {
      if (remainBytes >= kPacketHeaderSize)
      {
        // parse header
        uint32_t const watermark = *((uint32_t*)m_partialData.data());
        static_assert (sizeof(watermark) == std::tuple_size<std::array<uint8_t, 4>>(), "Invalid watermark size");
        processedBytes += sizeof(uint32_t);

        // TODO: provide error if watermark is invalid
        if (watermark != kPacketWatermark)
          SC_THROW_EXCEPTION(utils::ExceptionInvalidState, "Invalid watermark of a packet");

        uint32_t const packetSize = *((uint32_t*)(m_partialData.data() + processedBytes));
        processedBytes += sizeof(uint32_t);

        m_packet = std::make_unique<Packet>(packetSize);
        if (m_packet->IsReceived())
          ProcessPacket();
      }
      else // wait next potion of data
      {
        break;
      }
    }
    else // extend packet with new portion of data
    {
      if (!m_packet->IsReceived())
      {
        SC_ASSERT(m_packet->received < m_packet->size, ("Invalid packet state"));
        size_t const remainPacketBytes = m_packet->size - m_packet->received;
        size_t const bytesToCopy = std::min(remainBytes, remainPacketBytes);

        std::memcpy(m_packet->data.data() + m_packet->received, m_partialData.data() + processedBytes, bytesToCopy);
        m_packet->received += bytesToCopy;
        processedBytes += bytesToCopy;
      }

      // if packet become fully recived, then process it
      if (m_packet->IsReceived())
        ProcessPacket();
    }
  }

  // store non parsed bytes for next iteration
  size_t const remainBytes = m_partialData.size() - processedBytes;
  if (remainBytes > 0)
  {
    std::vector<uint8_t> newBytes(remainBytes);
    std::memcpy(newBytes.data(), m_partialData.data() + processedBytes, remainBytes);
    std::swap(m_partialData, newBytes);
  }
  else
  {
    m_partialData.resize(0);
  }

  ReadSocket();
}

void Session::HandleWrite(boost::system::error_code const & error)
{
  if (error)
  {
    SC_LOG_ERROR(MakeMessage(error.message()));

    // Initiate graceful connection closure.
    boost::system::error_code ignored_ec;
    m_socket.shutdown(boost::asio::ip::tcp::socket::shutdown_both, ignored_ec);
  }
}

std::string Session::MakeMessage(std::string const & msg) const
{
  return "Session " + std::to_string(m_id) + ": " + msg;
}

} // namespace impl
