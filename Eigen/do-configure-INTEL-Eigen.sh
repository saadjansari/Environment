#!/bin/bash

SOURCE_PATH=../eigen

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
  -D CMAKE_INSTALL_PREFIX:FILEPATH="$HOME/local/" \
  -D CMAKE_BUILD_TYPE:STRING="Release" \
  -D Boost_NO_BOOST_CMAKE:BOOL=ON \
  -D MKL_INCLUDE_DIRS:FILEPATH="$MKLROOT/include" \
  -D MKL_LIBRARY_DIRS:FILEPATH="$MKLROOT/lib/intel64" \
  -D MKL_LIBRARY_NAMES:STRING="mkl_rt" \
  -D BLAS_LIBRARY_DIRS:FILEPATH="$MKLROOT/lib/intel64" \
  -D BLAS_LIBRARY_NAMES:STRING="mkl_rt" \
  -D LAPACK_LIBRARY_DIRS:FILEPATH="$MKLROOT/lib/intel64" \
  -D LAPACK_LIBRARY_NAMES:STRING="mkl_rt" \
  -D CMAKE_CXX_COMPILER:STRING="mpicxx" \
  -D CMAKE_C_COMPILER:STRING="mpicc" \
  -D CMAKE_CXX_FLAGS:STRING="$CXXFLAGS" \
  -D CMAKE_C_FLAGS:STRING="$CFLAGS" \
  -D OpenMP_CXX_FLAGS:STRING="$OPENMP_CXX_FLAGS" \
  -D OpenMP_C_FLAGS:STRING="$OPENMP_C_FLAGS" \
  -D EIGEN_MAX_CPP_VER:STRING="14" \
  -D EIGEN_TEST_AVX:BOOL=ON \
  -D EIGEN_TEST_CXX11:BOOL=ON \
  -D EIGEN_TEST_FMA:BOOL=ON \
  -D EIGEN_TEST_OPENMP:BOOL=ON \
$EXTRA_ARGS \
$SOURCE_PATH

