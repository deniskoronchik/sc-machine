#pragma once

#include <mbedtls/sha256.h>

#include <optional>
#include <string>

namespace utils
{

std::string HexString(uint8_t * data, size_t len);

/// Calculates SHA256 hash for data
std::optional<std::string> CalculateSHA256(uint8_t const * data, size_t size);
std::optional<std::string> CalculateSHA256(std::string const & str);

} // namespace
