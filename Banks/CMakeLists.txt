cmake_minimum_required(VERSION 3.5)

set(CMAKE_CXX_FLAGS ${ROOT_CXX_FLAGS})
add_definitions(-fPIC)
add_library(clas12obj OBJECT
  clas12event.cpp
  detector.cpp
  header.cpp
  particle.cpp
  vectors.cpp
)

# shared libraries need PIC
set_property(TARGET clas12obj PROPERTY POSITION_INDEPENDENT_CODE 1)
# shared and static libraries built from the same object files
add_library(clas12tool SHARED $<TARGET_OBJECTS:clas12obj>)
add_library(clas12tool_static STATIC $<TARGET_OBJECTS:clas12obj>)

target_link_libraries(clas12tool PUBLIC hipocpp)
target_link_libraries(clas12tool_static PUBLIC hipocpp)

install(TARGETS clas12tool clas12tool_static
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)
