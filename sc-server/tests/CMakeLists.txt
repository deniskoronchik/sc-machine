make_tests_from_folder(${CMAKE_CURRENT_LIST_DIR}/units
  NAME sc-server-tests
  DEPENDS sc-memory mbedtls sc-server-lib
  INCLUDES 
    ${SC_MEMORY_SRC}
    ${CMAKE_CURRENT_LIST_DIR}/units
    ${CMAKE_CURRENT_LIST_DIR}/../sc-server/src)