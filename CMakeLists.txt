cmake_minimum_required(VERSION 3.5)
project(clas12tool)
set(VERSION 1.0.0)

set(CMAKE_MODULE_PATH
   ${CMAKE_MODULE_PATH}
   ${PROJECT_SOURCE_DIR}/cmake)
list(APPEND CMAKE_PREFIX_PATH $ENV{ROOTSYS})
find_package(ROOT REQUIRED COMPONENTS RIO Net)
include(${ROOT_USE_FILE})
set(CMAKE_CXX_FLAGS ${ROOT_CXX_FLAGS})

set(LZ4_FOUND FALSE)
find_package(LZ4)
IF(NOT ${LZ4_FOUND})
  message(FATAL_ERROR "\nlz4 not found\nAt this time use make to build the libraries")
ENDIF()

include_directories(Hipo)
add_subdirectory(Hipo)

include_directories(Banks)
add_subdirectory(Banks)
