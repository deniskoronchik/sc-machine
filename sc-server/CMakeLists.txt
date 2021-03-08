find_package(SQLite3 REQUIRED)

add_subdirectory(sc-server)
add_subdirectory(sc-users)

if (BUILD_TESTING)
    add_subdirectory(tests)
endif ()
