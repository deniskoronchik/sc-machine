#include "session.hpp"

#include <boost/bind.hpp>
#include <boost/logic/tribool.hpp>
#include <boost/tuple/tuple.hpp>

#include <sc-memory/sc_debug.hpp>

#include <sctp.pb.h>

namespace impl
{

std::atomic_uint32_t Session::ms_idCounter = { 1 };

Session::Session(boost::asio::io_service & ioService)
  : m_strand(ioService)
  , m_socket(ioService)
{
  m_part.reserve(1024);
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
  joined.resize(m_part.size() + bytesTransfered);
  std::memcpy(joined.data(), m_part.data(), m_part.size());
  std::memcpy(joined.data() + m_part.size(), m_buffer.data(), bytesTransfered);
  std::swap(m_part, joined);

  size_t processedBytes = 0;
  while (processedBytes < bytesTransfered)
  {
    size_t const remainBytes = bytesTransfered - processedBytes;
    Packet * packet = nullptr;
    if (!m_packetsQueue.empty())
    {
      packet = m_packetsQueue.back().get();
      if (packet->IsReceived())
        packet = nullptr;
    }

    if (packet)
    {
      SC_ASSERT(packet->received < packet->size, ("Invalid packet state"));
      size_t const remainPacketBytes = packet->size - packet->received;
      size_t const bytesToCopy = std::min(remainBytes, remainPacketBytes);

      std::memcpy(packet->data.data() + packet->received, m_part.data() + processedBytes, bytesToCopy);
      packet->received += bytesToCopy;
      processedBytes += bytesToCopy;
    }
    else // start new package
    {
      size_t constexpr kHeaderSize = 8;
      sctp::PacketHeader header;
      if ((remainBytes >= kHeaderSize) &&
          header.ParseFromArray(m_part.data() + kHeaderSize, remainBytes))
      {
        Packet::Ptr newPacket = std::make_unique<Packet>(header.size());

        uint32_t const watermark = header.watermark();
        static_assert (sizeof(watermark) == std::tuple_size<Packet::DataArray>(), "Invalid watermark size");
        std::memcpy(newPacket->watermark.data(), &watermark, newPacket->watermark.size());

        processedBytes += kHeaderSize;
        m_packetsQueue.push(std::move(newPacket));
      }
      else // store non parsed bytes for next iteration
      {
        std::vector<uint8_t> newBytes;
        newBytes.reserve(m_buffer.size() + remainBytes);
        newBytes.resize(remainBytes);

        std::memcpy(newBytes.data(), m_part.data() + processedBytes, remainBytes);
        std::swap(m_part, newBytes);
      }
    }
  }

  SC_ASSERT(processedBytes == bytesTransfered, ());
  ReadSocket();
}

std::string Session::MakeMessage(std::string const & msg) const
{
  return "Session " + std::to_string(m_id) + ": " + msg;
}
} // namespace impl
