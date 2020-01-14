#!/bin/bash

SOURCE_PATH=../msgpack-c

# You can invoke this shell script with additional command-line
# arguments.  They will be passed directly to CMake.
#
EXTRA_ARGS=$@

#
# Each invocation of CMake caches the values of build options in a
# CMakeCache.txt file.  If you run CMake again without deleting the
# CMakeCache.txt file, CMake won't notice any build options that have
# changed, because it found their original values in the cache file.
# Deleting the CMakeCache.txt file before invoking CMake will insure
# that CMake learns about any build options you may have changed.
# Experience will teach you when you may omit this step.
#
rm -f CMakeCache.txt

#
# Enable all primary stable Trilinos packages.
#
cmake  \
  -D CMAKE_INSTALL_PREFIX:FILEPATH="/home/wyan/local/" \
  -D CMAKE_BUILD_TYPE:STRING="Release" \
  -D CMAKE_CXX_COMPILER:STRING="mpicxx" \
  -D CMAKE_C_COMPILER:STRING="mpicc" \
  -D CMAKE_CXX_FLAGS:STRING="-O3 -march=native" \
  -D CMAKE_C_FLAGS:STRING="-O3 -march=native" \
  -D BUILD_TESTING:BOOL=ON \
  -D MSGPACK_32BIT:BOOL=OFF \
  -D MSGPACK_BOOST:BOOL=OFF \
  -D MSGPACK_BUILD_EXAMPLES:BOOL=OFF \
  -D MSGPACK_BUILD_TESTS:BOOL=OFF \
  -D MSGPACK_CXX11:BOOL=ON \
  -D MSGPACK_CXX17:BOOL=OFF \
$EXTRA_ARGS \
$SOURCE_PATH
