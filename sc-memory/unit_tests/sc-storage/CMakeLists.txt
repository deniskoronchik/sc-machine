
file(GLOB_RECURSE SOURCES "*.cpp" "*.hpp")

add_executable(sc-storage-tests ${SOURCES})

target_include_directories(sc-storage-tests 
  PRIVATE ${SC_MEMORY_SRC}
	)

target_link_libraries(sc-storage-tests sc-storage)
