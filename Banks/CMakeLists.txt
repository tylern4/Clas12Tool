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
#add_library(clas12banks SHARED $<TARGET_OBJECTS:clas12obj>)
add_library(clas12banks STATIC $<TARGET_OBJECTS:clas12obj>)

#target_link_libraries(clas12banks PRIVATE hipocpp)
target_link_libraries(clas12banks PRIVATE hipocpp)

install(TARGETS clas12banks
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)
