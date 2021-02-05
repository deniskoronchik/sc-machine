
find_package(Protobuf REQUIRED)

# include (${CMAKE_CURRENT_LIST_DIR}/generated/gen.cmake)
include_directories(${PROTOBUF_INCLUDE_DIR})
protobuf_generate_cpp(PROTO_SOURCES PROTO_HEADERS sctp.proto)

add_library(sctp SHARED ${CMAKE_CURRENT_LIST_DIR}/sctp.cpp ${PROTO_SOURCES} ${PROTO_HEADERS})
target_include_directories(sctp PUBLIC ${Protobuf_INCLUDE_DIRS})
target_link_libraries(sctp ${Protobuf_LIBRARIES})