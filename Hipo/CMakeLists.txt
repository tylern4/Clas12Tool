cmake_minimum_required(VERSION 3.5)

set(CMAKE_CXX_FLAGS ${ROOT_CXX_FLAGS})
add_definitions(-fPIC)
add_definitions(-D__LZ4__)

add_library(hipoobj OBJECT
      data.cpp
      dictionary.cpp
      event.cpp
      node.cpp
      reader.cpp
      record.cpp
      text.cpp
      utils.cpp
      wrapper.cpp
      writer.cpp
    )

# shared libraries need PIC
set_property(TARGET hipoobj PROPERTY POSITION_INDEPENDENT_CODE 1)
# shared and static libraries built from the same object files
#add_library(hipocpp SHARED $<TARGET_OBJECTS:hipoobj>)
add_library(hipocpp STATIC $<TARGET_OBJECTS:hipoobj>)


IF(${LZ4_FOUND})
  #target_link_libraries(hipocpp PRIVATE ${LZ4_LIBRARY})
  target_link_libraries(hipocpp PRIVATE ${LZ4_LIBRARY})
  install(TARGETS hipocpp
          LIBRARY DESTINATION lib
          ARCHIVE DESTINATION lib)
ENDIF()
