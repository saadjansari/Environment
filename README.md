# Environment
A simple collection of necessary external libraries for my simulation

Easy steps:
- `git clone`, `git submodule init` and `git submodule update` to download those software
- modify Compile.py for your compiler and cpu settings, and choose if install or not
- `python3 Compile.py` to compile the library
- go to `PVFMM/pvfmm` and using the provided `do-configure.sh` to compile manually if `pvfmm` is necessary

Dependency:
- `gcc>=7` for full `c++14` support
- `mpicxx` and `mpicc`