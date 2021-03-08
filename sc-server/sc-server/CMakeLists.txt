
file(GLOB_RECURSE SOURCES "src/*.cpp")
file(GLOB_RECURSE HEADERS "src/*.hpp")

add_library(sc-server-lib STATIC ${SOURCES} ${HEADERS})
target_include_directories(sc-server-lib
  PUBLIC ${SC_MEMORY_SRC} 
  PUBLIC ${GLIB2_INCLUDE_DIRS}
  )
target_link_libraries(sc-server-lib
  sc-memory
  sctp
  Boost::program_options
  Boost::thread
  SQLite::SQLite3
  mbedtls)

add_dependencies(sc-server-lib
  sc-kpm
  sc-memory
)

add_executable(sc-server main.cpp)
target_include_directories(sc-server PRIVATE ${CMAKE_CURRENT_LIST_DIR}/src)
target_link_libraries(sc-server sc-server-lib)
