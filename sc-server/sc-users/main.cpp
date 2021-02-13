#include <boost/program_options.hpp>
#include <boost/filesystem.hpp>

#include <mbedtls/sha256.h>
#include <termcolor.hpp>

#include <iostream>
#include <unistd.h>
#include <sqlite3.h>

size_t const kMaxLoginLength = 32;

#define SQL_ERROR  termcolor::red << "SQL Error: " << termcolor::reset

namespace
{

class Database
{
public:
  Database() = default;
  ~Database()
  {
    Close();
  }

  bool Open(std::string const & dbPath)
  {
    int const rc = sqlite3_open(dbPath.c_str(), &m_db);
    if (rc)
    {
      std::cerr << SQL_ERROR
                << "Can't open database: "
                << sqlite3_errmsg(m_db)
                << std::endl;
      return false;
    }
    else
    {
      std::cout << "Database opened" << std::endl;
    }

    return true;
  }

  void Close()
  {
    if (m_db)
    {
      std::cout << "Close database" << std::endl;
      sqlite3_close(m_db);
      m_db = nullptr;
    }
  }

  bool HasTable()
  {
    std::string const sql = "select count(Login) from Users;";
    return ExecSQL(sql).first;
  }

  bool HasUser(std::string const & login)
  {
    std::string const sql = "SELECT Login FROM Users WHERE Login == '" + login + "'";

    bool result = false;
    ExecSQL(sql,
            &result,
            [](void * p_data,
               int /* num_fields */,
               char ** /* p_fields */,
               char ** /* p_col_names */) -> int
    {
      *(static_cast<bool*>(p_data)) = true;
      return 0;
    });

    return result;
  }

  void CreateTable()
  {
    /* Create SQL statement */
    std::stringstream sql;
    sql << "CREATE TABLE Users ("
        << "Login           varchar(" << std::to_string(kMaxLoginLength + 1) << ") NOT NULL,"
        << "Password        BINARY(64) NOT NULL,"
        << "UNIQUE (Login));";

    std::string const request = sql.str();
    auto res = ExecSQL(request);

    if (!res.first)
    {
      std::cerr << SQL_ERROR << res.second << std::endl;
    }
    else
    {
      std::cout << "SQL: Table created" << std::endl;
    }

    std::string const sqlCreateIndex = "CREATE INDEX idx_login ON Users (Login);";
    res = ExecSQL(sqlCreateIndex);
    if (!res.first)
    {
      std::cerr << SQL_ERROR << res.second << std::endl;
    }
  }

  bool AddUser(std::string const & login, std::string const & passwd)
  {
    if (HasUser(login))
    {
      std::cerr << "User `"
                << termcolor::yellow
                << login
                << termcolor::reset
                << "` already exists."
                << std::endl;
      return false;
    }

    // calculate hash
    auto const hash = CalculateHash(passwd);
    if (!hash)
    {
      std::cerr << termcolor::red
                << "Error: "
                << termcolor::reset
                << "Error during hash calculation"
                << std::endl;
      return false;
    }

    std::string const sql =
        "INSERT INTO Users (Login, Password)"
        "VALUES ('" + login +"', '" + *hash + "');";

    auto res = ExecSQL(sql);
    if (!res.first)
      std::cerr << SQL_ERROR << res.second << std::endl;

    return res.first;
  }

  bool RemoveUser(std::string const & login)
  {
    if (!HasUser(login))
    {
      std::cerr << "Can't find user `"
                << termcolor::yellow
                << login
                << termcolor::reset
                << "`"
                << std::endl;
      return false;
    }

    std::string const sql = "DELETE FROM Users WHERE Login == '" + login + "';";

    auto res = ExecSQL(sql);
    if (!res.first)
      std::cerr << SQL_ERROR << res.second << std::endl;

    return res.first;
  }

private:
  std::pair<bool, std::string> ExecSQL(std::string const & request,
                                       void * arg = nullptr,
                                       int (*callback)(void*,int,char**,char**) = nullptr)
  {
    char * errMsg = nullptr;
    int const rc = sqlite3_exec(m_db, request.c_str(), callback, arg, &errMsg);
    if (rc != SQLITE_OK)
    {
      sqlite3_free(errMsg);
      return { false, errMsg };
    }

    return { true, "" };
  }

  std::optional<std::string> CalculateHash(std::string const & data)
  {
    std::optional<std::string> result = {};

    mbedtls_sha256_context hashContext;
    mbedtls_sha256_init(&hashContext);
    if (mbedtls_sha256_starts_ret(&hashContext, 0) == 0)
    {
      int const rc = mbedtls_sha256_update_ret(
            &hashContext,
            (unsigned char *)(data.c_str()),
            data.size());

      if (rc == 0)
      {
        unsigned char buffer[32];
        if (mbedtls_sha256_finish_ret(&hashContext, buffer) == 0)
        {
          result = std::string ((char*)buffer, 32);
        }
      }
    }
    mbedtls_sha256_free(&hashContext);

    return result;
  }


private:
  sqlite3 * m_db = nullptr;
};

std::string EnterPassword(std::string const & msg)
{
  return std::string(getpass(msg.c_str()));
}

} // namesapce

int main(int argc, char *argv[])
{
  namespace bpo = boost::program_options;

  // command-line
  bpo::options_description options_description("sc-users usage");
  options_description.add_options()
      ("help", "Display this message")
      ("db", bpo::value<std::string>(), "Path to database file")
      ("add", bpo::value<std::string>(), "User login to add")
      ("password", bpo::value<std::string>(), "User password. Use only with --add")
      ("remove", bpo::value<std::string>(), "User login to remove");

  bpo::variables_map vm;
  try
  {
    bpo::store(bpo::command_line_parser(argc, argv).options(options_description).run(), vm);
    bpo::notify(vm);
  }
  catch(bpo::error const & err)
  {
    std::cerr << err.what() << std::endl;
    return EXIT_SUCCESS;
  }

  if (vm.count("help"))
  {
    std::cout << options_description << std::endl;
    return EXIT_SUCCESS;
  }

  if (vm.count("db") == 0)
  {
    std::cerr << "--db option is not specified. Please use --help to get more info." << std::endl;
    return EXIT_FAILURE;
  }

  if (vm.count("add") == 0 && vm.count("remove") == 0)
  {
    std::cerr << "No any command are specified. Please use --help to get more info." << std::endl;
    return EXIT_FAILURE;
  }

  if (vm.count("add") > 0 && vm.count("remove") > 0)
  {
    std::cerr << "This is impossible to run two commands at one time." << std::endl;
    return EXIT_FAILURE;
  }

  if (vm.count("remove") > 0 && vm.count("password") > 0)
  {
    std::cerr << "--password option can be used only with --add command" << std::endl;
    return EXIT_FAILURE;
  }

  // do work
  std::string const dbPath = vm["db"].as<std::string>();
  {
    Database db;
    if (db.Open(dbPath))
    {
      if (!db.HasTable())
        db.CreateTable();

      if (vm.count("add"))
      {

        std::string password;

        if (vm.count("password") == 0)
        {
          password = EnterPassword("Password: ");

          if (password.empty())
          {
            std::cerr << "Empty password. Please try again." << std::endl;
            return EXIT_FAILURE;
          }

          std::string const repeat = EnterPassword("Repeat password: ");

          if (password != repeat)
          {
            std::cerr << "Passwords are not equal. Please ty again." << std::endl;
            return EXIT_FAILURE;
          }
        }
        else
        {
          password = vm["password"].as<std::string>();
        }

        if (!db.AddUser(vm["add"].as<std::string>(), password))
          return EXIT_FAILURE;
      }
      else if (vm.count("remove"))
      {
        if (!db.RemoveUser(vm["remove"].as<std::string>()))
          return EXIT_FAILURE;
      }

      db.Close();
    }
    else
    {
      db.Close();
      return EXIT_FAILURE;
    }
  }

  // setup access flags for a file
  std::cout << "Setup access flags 600 for database" << std::endl;
  boost::filesystem::permissions(dbPath,
                                 boost::filesystem::perms::owner_read |
                                 boost::filesystem::perms::owner_write);

  return EXIT_SUCCESS; // : EXIT_FAILURE;
}
