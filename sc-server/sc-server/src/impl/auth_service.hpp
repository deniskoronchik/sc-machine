#pragma once

#include <string>

namespace impl
{

class AuthService
{
public:
  enum class Status : uint8_t
  {
    Authorized = 0,
    NonAuthorized,
    InternalError
  };

  explicit AuthService(std::string const & dbPath);

  /*! Checks authentification for user
   *  \param login User login
   *  \param salt Salt for a password
   *  \param authHash Authentification hash (hash of salted password)
   *  \return Returns authorization status
   */
  Status CheckAuth(std::string const & login, std::string const & salt, std::string const & authHash) const;

protected:
  //! Calculates auth hash for specified password
  std::string CalculateAuthHash(std::string const & password, std::string const & salt) const;

private:
  std::string m_dbPath;
};

} // namespace impl
