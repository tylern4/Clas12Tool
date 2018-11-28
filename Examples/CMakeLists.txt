cmake_minimum_required(VERSION 3.5)

add_executable(analysis analysis.cc)
target_link_libraries(analysis PRIVATE hipocpp_static clas12tool_static ${ROOT_LIBRARIES})

add_executable(clas12event_example clas12event_example.cc)
target_link_libraries(clas12event_example PRIVATE hipocpp_static clas12tool_static ${ROOT_LIBRARIES})

add_executable(readBanks readBanks.cc)
target_link_libraries(readBanks PRIVATE hipocpp_static clas12tool_static ${ROOT_LIBRARIES})

add_executable(readParticles readParticles.cc)
target_link_libraries(readParticles PRIVATE hipocpp_static clas12tool_static ${ROOT_LIBRARIES})


install(TARGETS analysis clas12event_example readBanks readParticles
        RUNTIME DESTINATION bin)
