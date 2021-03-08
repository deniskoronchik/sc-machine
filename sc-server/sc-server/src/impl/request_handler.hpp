#pragma once

#include "auth_service.hpp"

#include <cstdint>
#include <memory>
#include <optional>
#include <string>
#include <vector>

namespace sctp
{

class Response;
class HandshakeRequest;
class AuthorizationRequest;

} // namespace sctp


namespace impl
{

class RequestHandler
{
public:
  RequestHandler(std::shared_ptr<AuthService> authService);

  /*!
   * \brief Process input packet and produce output one
   * \param inPacket Input packet
   * \param outResponse Reference to response
   * \return If there are no any errors during packet processing, then returns true.
   * Otherwise returns false.
   */
  bool Handle(std::vector<uint8_t> const & inPacket, std::vector<uint8_t> & outResponse);

private:
  //! Handle handshake request
  bool HandleHandshake(sctp::HandshakeRequest const & request, sctp::Response & outResponse);
  //! Handle auth
  bool HandleAuth(sctp::AuthorizationRequest const & request, sctp::Response & outResponse);

  //! Generates new salt string
  std::optional<std::string> GenerateSalt() const;

private:
  //! Auth service
  std::shared_ptr<AuthService> m_authService = nullptr;
  //! Current user login
  std::string m_userLogin;
  //! Auth hash value
  std::string m_authSalt;
};


} // namespace impl
