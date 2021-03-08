#include <gtest/gtest.h>

#include "utils/hash.hpp"

TEST(sc_server_utils, sha256)
{
  {
    std::string const input = "The quick brown fox jumps over the lazy dog";
    std::optional<std::string> hash = utils::CalculateSHA256((uint8_t*)input.c_str(), input.size());
    EXPECT_TRUE(hash);

    std::string const correct = "d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592";
    EXPECT_EQ(*hash, correct);
  }

  {
    std::string const input = "The quick brown fox jumps over the lazy cog";
    std::optional<std::string> hash = utils::CalculateSHA256(input);
    EXPECT_TRUE(hash);

    std::string const correct = "e4c4d8f3bf76b692de791a173e05321150f7a345b46484fe427f6acc7ecc81be";
    EXPECT_EQ(*hash, correct);
  }
}
