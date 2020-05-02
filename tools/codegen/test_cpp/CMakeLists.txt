
file(GLOB_RECURSE SOURCES "*.cpp" "*.hpp")

add_executable(sc-codegen-tests ${SOURCES})

target_include_directories(sc-codegen-tests 
  PRIVATE ${GLIB2_INCLUDE_DIRS}
  PRIVATE ${SC_MEMORY_SRC}
  )

target_link_libraries(sc-codegen-tests 
  sc-memory
  sc-test-framework)

sc_codegen(sc-codegen-tests ${CMAKE_CURRENT_LIST_DIR})
