#pragma once

#include "hash.hpp"

#include <mbedtls/sha256.h>

namespace utils
{

namespace
{

constexpr char hexmap[] = {'0', '1', '2', '3', '4', '5', '6', '7',
                           '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};

} // namespace

std::string HexString(uint8_t * data, size_t len)
{
  std::string s(len * 2, ' ');
  for (size_t i = 0; i < len; ++i)
  {
    s[2 * i + 1] = hexmap[data[i] & 0x0F];
    s[2 * i] = hexmap[(data[i] & 0xF0) >> 4];
  }

  return s;
}

std::optional<std::string> CalculateSHA256(uint8_t const * data, size_t size)
{
  std::optional<std::string> result;

  mbedtls_sha256_context hashContext;
  mbedtls_sha256_init(&hashContext);
  if (mbedtls_sha256_starts_ret(&hashContext, 0) == 0)
  {
    int const rc = mbedtls_sha256_update_ret(
          &hashContext,
          static_cast<unsigned char const *>(data),
          size);

    if (rc == 0)
    {
      unsigned char buffer[32];
      if (mbedtls_sha256_finish_ret(&hashContext, buffer) == 0)
        result = { HexString(buffer, 32) };
    }
  }
  mbedtls_sha256_free(&hashContext);

  return result;
}

std::optional<std::string> CalculateSHA256(std::string const & str)
{
  return CalculateSHA256((uint8_t*)str.c_str(), str.size());
}

} // namespace
