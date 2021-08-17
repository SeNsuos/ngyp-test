cmake_minimum_required(VERSION 3.20)
project(test)

set(CMAKE_CXX_STANDARD 11)

include_directories(~/.node-gyp/14.15.1/include/node)
include_directories(./node_modules/node-addon-api)

add_executable(addon src/cpp/addon.cpp)