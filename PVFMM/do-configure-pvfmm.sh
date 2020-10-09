#!/bin/bash

SOURCE_PATH=../pvfmm

# You can invoke this shell script with additional command-line
# arguments.  They will be passed directly to CMake.
#
EXTRA_ARGS=$@

# use aocl library
#export FFTWDIR=$AOCL_BASE/amd-fftw/ 
export FFTWDIR=$AOCL_BASE/

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
  -D CMAKE_INSTALL_PREFIX:FILEPATH="$SFTPATH" \
  -D CMAKE_BUILD_TYPE:STRING="Release" \
  -D CMAKE_CXX_COMPILER:STRING="mpicxx" \
  -D CMAKE_CXX_FLAGS:STRING="$CXXFLAGS" \
  -D BLA_VENDOR="FLAME" \
  -D BLAS_LIBRARIES:FILEPATH="$AOCL_BASE/lib/libblis-mt.a" \
  -D LAPACK_LIBRARIES:FILEPATH="$AOCL_BASE/lib/libflame.a" \
  -D FFTW_INCLUDE_DIRS:FILEPATH="$AOCL_BASE/amd-fftw/include" \
  -D FFTW_DOUBLE_LIB="$AOCL_BASE/lib/libfftw3.so" \
  -D FFTW_DOUBLE_OPENMP_LIB="$AOCL_BASE/lib/libfftw3_omp.so" \
  -D FFTW_FLOAT_LIB="$AOCL_BASE/lib/libfftw3f.so" \
  -D FFTW_FLOAT_OPENMP_LIB="$AOCL_BASE/lib/libfftw3f_omp.so" \
$EXTRA_ARGS \
$SOURCE_PATH

#  -D BLA_STATIC:BOOL=ON \
