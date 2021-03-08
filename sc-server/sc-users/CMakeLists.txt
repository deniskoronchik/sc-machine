
file(GLOB_RECURSE SOURCES "*.cpp")
file(GLOB_RECURSE HEADERS "*.hpp")

add_executable(sc-users ${SOURCES} ${HEADERS})    
target_link_libraries(sc-users
    Boost::filesystem
    Boost::program_options
    SQLite::SQLite3
    mbedtls
    termcolor)
