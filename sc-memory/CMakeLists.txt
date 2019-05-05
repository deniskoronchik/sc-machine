
add_subdirectory(sc-core)
add_subdirectory(sc-memory)
add_subdirectory(sc-storage)

if (${SC_BUILD_TESTS})
  add_subdirectory(unit_tests)
endif ()