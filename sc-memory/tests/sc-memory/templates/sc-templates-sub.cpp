#include <gtest/gtest.h>

#include "sc-memory/sc_memory.hpp"
#include "sc-memory/sc_scs_helper.hpp"

#include "sc_test.hpp"
#include "template_test_utils.hpp"

using ScSubTemplateTest = ScTemplateTest;

TEST_F(ScSubTemplateTest, smoke)
{
  SCsHelper scs(*m_ctx, std::make_shared<DummyFileInterface>());

  char const * data =
      "x -> y;;"
      "y -> z;;"
      "y -> w;;";

  scs.GenerateBySCsText(data);

  ScAddr const x = m_ctx->HelperResolveSystemIdtf("x");
  EXPECT_TRUE(x);

  ScAddr const y = m_ctx->HelperResolveSystemIdtf("y");
  EXPECT_TRUE(y);

  ScAddr const z = m_ctx->HelperResolveSystemIdtf("z");
  EXPECT_TRUE(z);

  ScAddr const w = m_ctx->HelperResolveSystemIdtf("w");
  EXPECT_TRUE(w);

  ScTemplate templ;
  templ.Triple(
        x >> "x",
        ScType::EdgeAccessVarPosPerm,
        y >> "y");

  templ.Triple(
        "y",
        ScType::EdgeAccessVarPosPerm,
        ScType::NodeVar >> "last");

  // check by base template
  {
    ScTemplateSearchResult result;
    EXPECT_TRUE(m_ctx->HelperSearchTemplate(templ, result));

    EXPECT_EQ(result.Size(), 2u);
  }

  // create substitution
  ScTemplateParams params;
  params.Add("w", w);

  ScTemplate subTempl = templ.Substitution(params);
  {
    ScTemplateSearchResult result;
    EXPECT_TRUE(m_ctx->HelperSearchTemplate(subTempl, result));

    EXPECT_EQ(result.Size(), 1u);
    EXPECT_EQ(result[1]["last"], w);
  }
}

TEST_F(ScSubTemplateTest, edge)
{
  SCsHelper scs(*m_ctx, std::make_shared<DummyFileInterface>());

  char const * data =
      "x -> y;;"
      "x -> z;;";

  scs.GenerateBySCsText(data);

  ScAddr const x = m_ctx->HelperResolveSystemIdtf("x");
  EXPECT_TRUE(x);

  ScTemplate templ;
  templ.Triple(
        x >> "x",
        ScType::EdgeAccessVarPosPerm >> "_edge",
        ScType::NodeVar >> "_found");

  ScAddr edge;
  ScAddr const z = m_ctx->HelperResolveSystemIdtf("z");
  EXPECT_TRUE(z);

  // check base template
  {
    ScTemplateSearchResult result;
    EXPECT_TRUE(m_ctx->HelperSearchTemplate(templ, result));
    EXPECT_EQ(result.Size(), 2u);

    for (size_t i = 0; i < result.Size(); ++i)
    {
      ScAddr const addr = result[i]["_y"];
      if (addr == z)
        edge = result[i][1];
    }

    EXPECT_TRUE(edge);
  }

  // make valid substitution with edge
  {
    ScTemplateParams params;
    params.Add("_edge", edge);

    ScTemplate sub = templ.Substitution(params);

    ScTemplateSearchResult result;
    EXPECT_TRUE(m_ctx->HelperSearchTemplate(sub, result));
    EXPECT_EQ(result.Size(), 1u);

    EXPECT_EQ(result[1]["x"], x);
    EXPECT_EQ(result[1]["_edge"], edge);
    EXPECT_EQ(result[1]["_found"], z);
  }

  // make invalid subsitution with edge
  {

  }
}

TEST_F(ScSubTemplateTest, check_types)
{

}
