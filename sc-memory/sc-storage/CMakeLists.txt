file(GLOB_RECURSE SOURCES "*.cpp" "*.hpp")

add_library (sc-storage SHARED ${SOURCES})

GenerateAPI("${CMAKE_CURRENT_LIST_DIR}/sc_storage_api.hpp" "SC_STORAGE")

target_include_directories(sc-storage
    PRIVATE ${SC_MEMORY_SRC}
  )

target_link_libraries(sc-storage
    PUBLIC sc-memory
  )

add_dependencies(sc-storage 
    sc-memory
  )
