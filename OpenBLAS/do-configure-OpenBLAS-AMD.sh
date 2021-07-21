#!/bin/bash

SOURCE_PATH=../OpenBLAS

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
cmake \
  -D CMAKE_INSTALL_PREFIX:FILEPATH="$SFTPATH" \
  -D CMAKE_INSTALL_LIBDIR="lib" \
  -D CMAKE_BUILD_TYPE:STRING="Release" \
  -D CMAKE_C_COMPILER:STRING="gcc" \
  -D CMAKE_C_FLAGS:STRING="$CFLAGS" \
  -D CMAKE_Fortran_COMPILER:STRING="gfortran" \
  -D CMAKE_Fortran_FLAGS:STRING="$CFLAGS" \
  -D BUILD_SHARED_LIBS=ON \
  -D TARGET=ZEN \
  -D DYNAMIC_ARCH=0 \
  -D USE_THREAD=1 \
  -D USE_OPENMP=1 \
  -D BUILD_RELAPACK=0 \
  -D NUM_THREADS=64 \
  -D NUM_PARALLEL=16 \
  -D CPP_THREAD_SAFETY_GEMV=ON \
  -D CPP_THREAD_SAFETY_TEST=ON \
  $EXTRA_ARGS \
  $SOURCE_PATH
