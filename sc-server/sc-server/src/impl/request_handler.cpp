#include "request_handler.hpp"

#include "../utils/hash.hpp"

#include <sc-memory/sc_debug.hpp>

#include "sctp.pb.h"

#include <random>

namespace impl
{

RequestHandler::RequestHandler(std::shared_ptr<AuthService> authService)
  : m_authService(authService)
{
}

bool RequestHandler::Handle(std::vector<uint8_t> const & inPacket, std::vector<uint8_t> & outResponse)
{
  sctp::Request req;
  if (req.ParseFromArray(inPacket.data(), inPacket.size()))
  {
    sctp::Response response;

    std::time_t timestamp = std::time(nullptr);
    response.set_id(req.id());
    response.set_timestamp(timestamp);

    bool isHandled = false;

    // handshake
    if (req.has_handshake())
      isHandled = HandleHandshake(req.handshake(), response);
    else if (req.has_auth())
      isHandled = HandleAuth(req.auth(), response);

    if (isHandled)
    {
      outResponse.resize(response.ByteSizeLong());
      return response.SerializeToArray(outResponse.data(), outResponse.size());
    }
  }

  return false;
}

bool RequestHandler::HandleHandshake(sctp::HandshakeRequest const & request, sctp::Response & outResponse)
{
  m_userLogin = request.login();

  auto const salt = GenerateSalt();
  if (!salt)
    return false;

  m_authSalt = salt.value();

  sctp::HandshakeResponse * handshake = new sctp::HandshakeResponse();
  handshake->set_salt(m_authSalt);

  outResponse.set_allocated_handshake(handshake);

  return true;
}

bool RequestHandler::HandleAuth(sctp::AuthorizationRequest const & request, sctp::Response & outResponse)
{
  std::string const receivedHash = request.hash();
  auto const status = m_authService->CheckAuth(m_userLogin, m_authSalt, receivedHash);

  sctp::AuthorizationResponse * response = new sctp::AuthorizationResponse();

  if (status == impl::AuthService::Status::Authorized)
    response->set_status(sctp::AuthorizationResponse_AuthStatus_Success);
  else if (status == impl::AuthService::Status::NonAuthorized)
    response->set_status(sctp::AuthorizationResponse_AuthStatus_Failed);
  else
    response->set_status(sctp::AuthorizationResponse_AuthStatus_Failed);

  outResponse.set_allocated_auth(response);

  return true;
}

std::optional<std::string> RequestHandler::GenerateSalt() const
{
  std::random_device rd;
  std::uniform_int_distribution<int> dist(0, 255);

  static constexpr size_t kSaltLength = 8096;
  std::array<uint8_t, kSaltLength> saltData;
  for (size_t i = 0; i < saltData.size(); ++i)
    saltData[i] = 0;//static_cast<uint8_t>(dist(rd));

  return utils::CalculateSHA256(saltData.data(), saltData.size());
}

} // namespace impl
