#include <gtest/gtest.h>

#include "impl/auth_service.hpp"
#include "utils/hash.hpp"

namespace
{
class TestAuthService : public impl::AuthService
{
public:
  explicit TestAuthService(std::string const & dbPath)
    : impl::AuthService(dbPath)
  {
  }

  std::string TestCalculateAuthHash(std::string const & password, std::string const & salt) const
  {
    return CalculateAuthHash(password, salt);
  }
};

} // namespace

TEST(AuthService, auth_hash)
{
  std::string const passwd_hash = "1234567890";
  std::string const salt = "qwertyuiop";

  auto const expected = utils::CalculateSHA256("q1w2e3r4t5y6u7i8o9p0");
  ASSERT_TRUE(expected);

  TestAuthService auth("users.db");
  EXPECT_EQ(auth.TestCalculateAuthHash(passwd_hash, salt), *expected);
}
