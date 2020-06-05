# Environment
A simple collection of necessary external libraries for my simulation
You should have `cmake>=3.10` installed.

# Case 1 if you do not have any compilers:
- install `conda`
- create a conda environment, for example
```bash
conda create -n py3 python=3
```
- install compilers and necessary libs in the conda environment:
```bash
conda activate py3
conda install mkl-devel scipy numpy openmpi mpi4py gcc_linux-64 gxx_linux-64 gfortran_linux-64 boost
```
- setup environment variables
```bash
export MKL_THREADING_LAYER=GNU         # necessary because conda uses gcc
export MKL_INTERFACE_LAYER=GNU,LP64    # necessary because conda uses gcc
export MKLROOT=/full/path/to/conda/envs/py3
```
- run `Compile.py`:
```bash
python3 ./Compile.py # default to gcc & non-debug flags
``` 
# Case 2 if you have compiler and other math libraries
Modify `Compile.py` properly so you are invoking the correct compiler with proper flags. 
An example of invoking intel compilers with multiple arch dispatch is included there.

# After compilation:
- check the compilation logs in `*/build/Testing/Temporary` to see if any error occurs.
- check if the installed `/full/install/path/share/pvfmm/pvfmmConfig.cmake` file has correct path


# Dependency:
- `gcc>=7` for full `c++14` support
- `mpicxx` and `mpicc`
- `mkl` or other proper BLAS, LAPACK, and FFTW libs
- Proper MKL environment variables setup:
```bash
$ env | grep MKL
MKL_THREADING_LAYER=GNU         # necessary if using gcc
MKL_INTERFACE_LAYER=GNU,LP64    # necessary if using gcc
MKLROOT=/full/path/to/MKL/library/base/folder
$ ls $MKLROOT/lib | grep libmkl_rt.so
libmkl_rt.so
$ ls $MKLROOT/include | grep mkl.h
mkl.h

```
