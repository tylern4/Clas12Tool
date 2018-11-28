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
  include_directories("${CMAKE_SOURCE_DIR}/Lz4/lib")
  add_library(LZ4 STATIC IMPORTED)
  set_target_properties(LZ4 PROPERTIES
    IMPORTED_LOCATION "${CMAKE_SOURCE_DIR}/Lz4/lib/liblz4.a"
    INTERFACE_INCLUDE_DIRECTORIES "${CMAKE_SOURCE_DIR}/Lz4/lib"
  )
ENDIF()

include_directories(Hipo)
add_subdirectory(Hipo)

include_directories(Banks)
add_subdirectory(Banks)

find_package(Cython)
IF(${CYTHON_FOUND})
  add_subdirectory(hipopy)
ENDIF()

add_subdirectory(Examples)
