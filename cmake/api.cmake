function(GenerateAPI outputPath apiName)
  set (API_NAME ${apiName})
  configure_file("${CMAKE_MODULE_PATH}/api.hpp.in" "${outputPath}")
endfunction()