import os
import multiprocessing

# sets environment variables
os.environ["SFTPATH"] = os.environ["HOME"]+"/local"
print("install destination:", os.environ["SFTPATH"])
# intel compiler
# os.environ["CXXFLAGS"] = "-O3 -xHost -DNDEBUG -qno-offload"
# os.environ["CFLAGS"] = "-O3 -xHost -DNDEBUG -qno-offload"
# os.environ["OPENMP_CXX_FLAGS"] = "-qopenmp"
# os.environ["OPENMP_C_FLAGS"] = "-qopenmp"

# gcc
os.environ["CXXFLAGS"] = "-O3 -march=native -DNDEBUG"
os.environ["CFLAGS"] = "-O3 -march=native -DNDEBUG"
os.environ["OPENMP_CXX_FLAGS"] = "-fopenmp"
os.environ["OPENMP_C_FLAGS"] = "-fopenmp"

install = False
check_eigen = False
test_Trilinos = True
make_jobs = multiprocessing.cpu_count()


cwd = os.getcwd()

os.system('git submodule init')
os.system('git submodule update')

# TRNG
os.chdir(cwd)
os.chdir('TRNG')
os.system('rm -rf ./build && mkdir ./build')
os.chdir('build')
os.system('bash ../do-configure-TRNG4.sh && make -j'+str(make_jobs))
os.system('./examples/time')
if install:
    os.system('make install')

# YamlCpp
os.chdir(cwd)
os.chdir('YamlCpp')
os.system('rm -rf ./build && mkdir ./build')
os.chdir('build')
os.system('bash ../do-configure-YamlCpp.sh && make -j'+str(make_jobs))
if install:
    os.system('make install')

# MsgPack
os.chdir(cwd)
os.chdir('MsgPack')
os.system('rm -rf ./build && mkdir ./build')
os.chdir('build')
os.system('bash ../do-configure-MsgPack.sh && make -j'+str(make_jobs))
if install:
    os.system('make install')

# Eigen
os.chdir(cwd)
os.chdir('Eigen')
os.system('rm -rf ./build && mkdir ./build')
os.chdir('build')
os.system('bash ../do-configure-Eigen.sh && make -j'+str(make_jobs))
if check_eigen:
    os.system('make check -j8')
if install:
    os.system('make install')


# Trilinos
os.chdir(cwd)
os.chdir('Trilinos')
os.system('rm -rf ./build && mkdir ./build')
os.chdir('build')
os.system('bash ../do-configure-Trilinos.sh && make -j'+str(make_jobs))
if test_Trilinos:
    os.environ["OMP_NUM_THREADS"] = "4"
    os.system('make test')
if install:
    os.system('make install')

# PVFMM, does not work yet
# os.chdir(cwd)
# os.chdir('PVFMM/pvfmm')
# os.system('./autogen.sh')
# os.system('bash ../do-configure.sh && make clean')
# os.system('make -j8')
# if install:
#     os.system('make install')
