
unset PVFMM_DIR
./configure MPICXX=mpicxx --prefix=$HOME/local \
--with-openmp-flag='qopenmp' \
CXXFLAGS="-O3 -xHost -std=c++14 -DPVFMM_FFTW3_MKL" \
--with-fftw-include="$MKLROOT/include/fftw" \
--with-fftw-lib="-lmkl_rt" 

