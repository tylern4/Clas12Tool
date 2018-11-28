find_package(PythonInterp)
find_package(PythonLibs)
find_package(PythonExtensions)
find_package(Cython REQUIRED)

add_definitions(-D__LZ4__)

add_cython_target(hipopy hipopy.pyx CXX PY3 OUTPUT_VAR _hipopy)
include_directories(${PYTHON_INCLUDE_DIRS})

add_definitions(-D__LZ4__)
set(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} ${EXTRA_FLAGS}" )

add_library(hipopy MODULE ${_hipopy})
python_extension_module(hipopy)


IF(${LZ4_FOUND})
  target_link_libraries(hipopy hipocpp clas12tool ${LZ4_LIBRARY} ${PYTHON_LIBRARIES} ${ROOT_LIBRARIES})
ELSE()
  target_link_libraries(hipopy hipocpp clas12tool LZ4 ${PYTHON_LIBRARIES} ${ROOT_LIBRARIES})
ENDIF()




install(TARGETS hipopy LIBRARY DESTINATION lib)
