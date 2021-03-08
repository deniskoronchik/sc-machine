#include "auth_service.hpp"

#include "../utils/hash.hpp"

#include <sc-memory/utils/sc_log.hpp>

#include <sqlite3.h>

namespace
{

class Database final
{
public:
  Database() = default;
  ~Database()
  {
    Close();
  }

  bool Open(std::string const & path)
  {
    int const rc = sqlite3_open(path.c_str(), &m_db);

    if (rc)
    {
      SC_LOG_ERROR("Can't open database: " << sqlite3_errmsg(m_db));
      return false;
    }

    return true;
  }

  std::optional<std::string> GetUserPassword(std::string const & login) const
  {
    std::string const sql = "SELECT Login, Password FROM Users WHERE Login == '" + login + "'";

    std::optional<std::string> password;
    char * errMsg = nullptr;
    int const rc = sqlite3_exec(m_db, sql.c_str(),
      [](void * p_data, int num_fields, char ** p_fields, char ** p_col_names) -> int
    {
      std::optional<std::string> * res = static_cast<std::optional<std::string>*>(p_data);

      for (int i = 0; i < num_fields; ++i)
      {
        if (strcmp(p_col_names[i], "Password") == 0)
          *res = { std::string(p_fields[i]) };
      }

      //! TODO: check duplicates

      return 0;
    }, &password, &errMsg);

    if (rc != SQLITE_OK)
    {
      sqlite3_free(errMsg);
      return {};
    }

    return password;
  }

  void Close()
  {
    if (m_db)
    {
      sqlite3_close(m_db);
      m_db = nullptr;
    }
  }

private:
  sqlite3 * m_db = nullptr;
};

} // namespace

namespace impl
{

AuthService::AuthService(std::string const & dbPath)
  : m_dbPath(dbPath)
{
}

AuthService::Status AuthService::CheckAuth(std::string const & login, std::string const & salt, std::string const & authHash) const
{
  Database db;

  if (db.Open(m_dbPath))
  {
    auto const password = db.GetUserPassword(login);
    db.Close();

    if (!password)
      return Status::NonAuthorized;

    auto const userHash = CalculateAuthHash(*password, salt);
    return userHash == authHash ? Status::Authorized : Status::NonAuthorized;
  }

  return Status::InternalError;
}

std::string AuthService::CalculateAuthHash(std::string const & password, std::string const & salt) const
{
  std::string result(salt.size() * 2, '0');

  assert(!password.empty ());
  assert(salt.size() == password.size());
  for (size_t i = 0; i < salt.size(); ++i)
  {
    size_t const idx = i * 2;
    result[idx] = salt[i];
    result[idx + 1] = password[i];
  }

  auto const hash = utils::CalculateSHA256(result);
  return hash ? *hash : "";
}

} // namespace impl
