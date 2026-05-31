cmake_minimum_required(VERSION 3.10)
project(kick-lucky-block-helper)

set(CMAKE_CXX_STANDARD 17)

add_executable(kick_lucky_block_helper src/main.cpp src/lucky_block.cpp src/roblox_interface.cpp)
target_include_directories(kick_lucky_block_helper PRIVATE include)