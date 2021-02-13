#include "server.hpp"
#include "server_config.hpp"

#include <boost/program_options.hpp>

#include <sc-memory/sc_debug.hpp>
#include <sc-memory/utils/sc_log.hpp>
#include <sc-memory/utils/sc_signal_handler.hpp>

int main(int argc, char *argv[]) try
{
  namespace bpo = boost::program_options;
  std::string configFile;

  // command-line
  {
    bpo::options_description options_description("sc-server usage");
    options_description.add_options()
        ("help", "Display this message")
        ("config,c",bpo::value<std::string>(), "Path to configuration file");

    bpo::variables_map vm;
    bpo::store(bpo::command_line_parser(argc, argv).options(options_description).run(), vm);
    bpo::notify(vm);

    if (vm.count("config"))
      configFile = vm["config"].as<std::string>();
    else
      return 0;

    if (vm.count("help"))
    {
      std::cout << options_description;
      return 0;
    }
  }

  // configuration file

  bpo::options_description opt_descr("sc-server config");
  opt_descr.add_options()
      // --- Storage ---
      ("storage.config_path", bpo::value<std::string>()->default_value(""),
       "Path to sc-storage configuration file")
      ("storage.ext_path", bpo::value<std::string>()->default_value("extensions"),
       "Path to sc-memory extensions")
      ("storage.repo_path", bpo::value<std::string>()->default_value("repo"),
       "Path to built knowledge base")
      ("storage.clear", bpo::value<bool>()->default_value(false),
       "Flag to clear sc-memory on start")
      // --- Server ---
      ("server.host", bpo::value<std::string>()->default_value("localhost"),
       "Host adress")
      ("server.port", bpo::value<uint16_t>()->default_value(55770),
       "Server port")
      ("server.threads", bpo::value<uint16_t>()->default_value(0),
       "Number of threads to process connections");

  bpo::variables_map vm;
  try
  {
    SC_LOG_INFO_COLOR("Load configuration from file: " << configFile, ScConsole::Color::Green);

    bpo::store(bpo::parse_config_file(configFile.c_str(), opt_descr), vm);
    bpo::notify(vm);
  }
  catch (const bpo::error &ex)
  {
    SC_LOG_ERROR(ex.what());
    return 0;
  }

  std::unique_ptr<ServerConfig> config = std::make_unique<ServerConfig>(std::move(vm));
  std::unique_ptr<Server> server = std::make_unique<Server>(std::move(config));

//  utils::ScSignalHandler::Initialize();
//  utils::ScSignalHandler::m_onTerminate = [&server]()
//  {
//    SC_LOG_INFO_COLOR("Request to stop server by user", ScConsole::Color::Blue);
//    server->Stop();
//  };

  server->Run();

  return EXIT_SUCCESS; // : EXIT_FAILURE;
}
catch (utils::ScException const & ex)
{
  SC_LOG_ERROR(ex.Description());
}
