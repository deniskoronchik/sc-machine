
file(GLOB_RECURSE SOURCES "*.cpp")
file(GLOB_RECURSE HEADERS "*.hpp")

add_executable(sc-server ${SOURCES} ${HEADERS})
target_include_directories(sc-server 
  PRIVATE ${SC_MEMORY_SRC} 
  PRIVATE ${GLIB2_INCLUDE_DIRS}
  )
target_link_libraries(sc-server 
  sc-memory
  sctp
  Boost::program_options
  Boost::thread)

add_dependencies(sc-server
  sc-kpm
  sc-memory
)
