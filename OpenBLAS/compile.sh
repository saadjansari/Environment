#!/bin/bash
make clean

make TARGET=ZEN \
    CC=clang \
    CFLAGS="--gcc-toolchain=$GCC_BASE -O3 -DNDEBUG -march=znver1 -fPIC -fopenmp" \
    FC=flang \
    FFLAGS="--gcc-toolchain=$GCC_BASE -O3 -DNDEBUG -march=znver1 -fPIC -fopenmp" \
    USE_THREAD=1 USE_OPENMP=1 NUM_THREADS=64 \
    DYNAMIC_ARCH=0 BUILD_RELAPACK=0 \

