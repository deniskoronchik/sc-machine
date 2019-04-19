/*
 * This source file is part of an OSTIS project. For the latest info, see http://ostis.net
 * Distributed under the MIT License
 * (See accompanying file COPYING.MIT or copy at http://opensource.org/licenses/MIT)
 */

#include "scs_translator.hpp"

#include "sc-memory/sc_memory.hpp"
#include "sc-memory/sc_scs_helper.hpp"

namespace impl
{

class FileProvider : public SCsFileInterface
{
public:
  FileProvider() = default;
  virtual ~FileProvider() = default;

  virtual ScStreamPtr GetFileContent(std::string const & fileURL)
  {
    return {};
  }
};

} // namespace impl

SCsTranslator::SCsTranslator(ScMemoryContext & context)
  : Translator(context)
{
}

bool SCsTranslator::TranslateImpl(Params const & params)
{
  std::string data;
  GetFileContent(params.m_fileName, data);

  SCsHelper scs(&m_ctx, std::make_shared<impl::FileProvider>());
  
  if (!scs.GenerateBySCsText(data))
  {
    SC_THROW_EXCEPTION(utils::ExceptionParseError, scs.GetLastError());
  }

  return true;
}