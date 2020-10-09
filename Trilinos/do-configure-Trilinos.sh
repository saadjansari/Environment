#!/bin/bash

# Set this to the root of your Trilinos source directory.
TRILINOS_PATH=../Trilinos

#
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
  -D CMAKE_INSTALL_PREFIX:FILEPATH="$SFTPATH" \
  -D CMAKE_BUILD_TYPE:STRING="Release" \
  -D BUILD_SHARED_LIBS=OFF \
  -D Trilinos_HIDE_DEPRECATED_CODE=ON \
  -D CMAKE_CXX_FLAGS:STRING="$CXXFLAGS" \
  -D CMAKE_C_FLAGS:STRING="$CFLAGS" \
  -D Kokkos_ENABLE_HWLOC:BOOL=OFF \
  -D Kokkos_ENABLE_OpenMP:BOOL=ON \
  -D Trilinos_ENABLE_EXPLICIT_INSTANTIATION=ON \
  -D Trilinos_ENABLE_Fortran:BOOL=OFF \
  -D Trilinos_ENABLE_EXAMPLES:BOOL=OFF \
  -D Trilinos_ENABLE_OpenMP:BOOL=ON \
  -D Trilinos_ENABLE_CXX11:BOOL=ON \
  -D Trilinos_ENABLE_Kokkos:BOOL=ON \
  -D Trilinos_ENABLE_Tpetra:BOOL=ON \
  -D Trilinos_ENABLE_Belos:BOOL=ON \
  -D Trilinos_ENABLE_Ifpack2:BOOL=ON \
  -D Trilinos_ENABLE_Zoltan2:BOOL=ON \
  -D Trilinos_ENABLE_TESTS:BOOL=ON \
  -D TpetraCore_Threaded_MKL:BOOL=ON \
  -D TPL_ENABLE_HWLOC:BOOL=OFF \
  -D TPL_ENABLE_MPI:BOOL=ON \
  -D BLA_STATIC:BOOL=ON \
  -D BLA_VENDOR="FLAME" \
$EXTRA_ARGS \
$TRILINOS_PATH

#  -D Trilinos_ENABLE_ROL:BOOL=ON \
#  -D BLAS_LIBRARY_DIRS:FILEPATH="$MKL_LIB_DIRS" \
#  -D BLAS_LIBRARY_NAMES:STRING="mkl_rt" \
#  -D LAPACK_LIBRARY_DIRS:FILEPATH="$MKL_LIB_DIRS" \
#  -D LAPACK_LIBRARY_NAMES:STRING="mkl_rt" \
