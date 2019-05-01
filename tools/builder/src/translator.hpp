/*
 * This source file is part of an OSTIS project. For the latest info, see http://ostis.net
 * Distributed under the MIT License
 * (See accompanying file COPYING.MIT or copy at http://opensource.org/licenses/MIT)
 */

#pragma once

#include "sc-memory/sc_addr.hpp"
#include "sc-memory/sc_object.hpp"

#include <string>

#include "translator.generated.hpp"

class Translator : public ScObject
{
  SC_CLASS()
  SC_GENERATED_BODY()

public:

  struct Params
  {
    //! Name of file to translate
    std::string m_fileName;
    //! Flag to generate format information based on file extensions
    bool m_autoFormatInfo;
  };
      
  explicit Translator(class ScMemoryContext & context);
  virtual ~Translator() = default;

  /*! Translate specified file into memory
   * @param params Input parameters
   * @return If file translated without any errors, then returns true; otherwise returns false.
   */
  bool Translate(Params const & params);

  //! Implementation of translate
  virtual bool TranslateImpl(Params const & params) = 0;

protected:
  /*! Generates format relation in sc-memory by file extension
   * @param addr sc-addr of sc-link to create format relation
   * @param ext File extension
   */
  void GenerateFormatInfo(ScAddr const & addr, std::string const & ext);

  void GetFileContent(std::string const & fileName, std::string & outContent);

protected:
  //! Pointer to memory context
  class ScMemoryContext & m_ctx;

  SC_PROPERTY(Keynode("nrel_format"), ForceCreate(ScType::NodeConstNoRole))
  static ScAddr ms_kNrelFormat;
};

