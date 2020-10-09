import os
import multiprocessing

# sets environment variables
# installation destination
os.environ["SFTPATH"] = os.environ["HOME"]+"/env_amd"

# gcc
os.environ["CXXFLAGS"] = "-O3 -march=native -DNDEBUG"
os.environ["CFLAGS"] = "-O3 -march=native -DNDEBUG"

# comment out component you don't want
enable = [
#    'trng',
#    'eigen',
#    'msgpack',
#    'yamlcpp',
    'trilinos',
#    'pvfmm',
#    'vtk'
]

install = False
check_eigen = False
test_Trilinos = True
make_jobs = multiprocessing.cpu_count()


cwd = os.getcwd()

print("install destination:", os.environ["SFTPATH"])
os.system('git submodule init')
os.system('git submodule update')

# TRNG
if 'trng' in enable:
    os.chdir(cwd)
    os.chdir('TRNG')
    os.system('rm -rf ./build && mkdir ./build')
    os.chdir('build')
    os.system('bash ../do-configure-TRNG4.sh && make -j'+str(make_jobs))
    os.system('./examples/time')
    if install:
        os.system('make install')

# YamlCpp
if 'yamlcpp' in enable:
    os.chdir(cwd)
    os.chdir('YamlCpp')
    os.system('rm -rf ./build && mkdir ./build')
    os.chdir('build')
    os.system('bash ../do-configure-YamlCpp.sh && make -j'+str(make_jobs))
    if install:
        os.system('make install')

# MsgPack
if 'msgpack' in enable:
    os.chdir(cwd)
    os.chdir('MsgPack')
    os.system('rm -rf ./build && mkdir ./build')
    os.chdir('build')
    os.system('bash ../do-configure-MsgPack.sh && make -j'+str(make_jobs))
    if install:
        os.system('make install')

# Eigen
if 'eigen' in enable:
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
if 'trilinos' in enable:
    os.chdir(cwd)
    os.chdir('Trilinos')
    os.system('rm -rf ./build && mkdir ./build')
    os.chdir('build')
    os.system('bash ../do-configure-Trilinos.sh && make -j'+str(make_jobs))
    if test_Trilinos:
        os.environ["OMP_NUM_THREADS"] = "3"
        os.system('make test')
    if install:
        os.system('make install')

# PVFMM
if 'pvfmm' in enable:
    os.chdir(cwd)
    os.chdir('PVFMM')
    os.system('rm -rf ./build && mkdir ./build')
    os.chdir('build')
    os.system('bash ../do-configure-pvfmm.sh && make -j'+str(make_jobs))
    os.system('./examples/example1 -N 65536 -omp 4')
    if install:
        os.system('make install')

# VTK
if 'vtk' in enable:
    os.chdir(cwd)
    os.chdir('VTK')
    os.system('rm -rf ./build && mkdir ./build')
    os.chdir('build')
    os.system('bash ../do-configure-VTK.sh && make -j'+str(make_jobs))
    if install:
        os.system('make install')
