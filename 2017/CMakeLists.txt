cmake_minimum_required(VERSION 3.20)
project(2017 C)

set(CMAKE_C_STANDARD 11)

include_directories(c)

add_executable(day01 c/day01.c c/io-util.h)
add_executable(day02 c/day02.c c/io-util.h)
