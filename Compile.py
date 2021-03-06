import os
import multiprocessing
import yaml


f = open('config.yaml')
config = yaml.load(f, Loader=yaml.FullLoader)
f.close()
print(config)


# sets environment variables
# installation destination
os.environ["SFTPATH"] = config['install_destination']
os.environ["CXXFLAGS"] = config['cxxflags']
os.environ["CFLAGS"] = config['cflags']
os.environ["OPENMP_CXX_FLAGS"] = config['openmp_cxx_flags']
os.environ["OPENMP_C_FLAGS"] = config['openmp_c_flags']

print("install destination:", os.environ["SFTPATH"])
print(os.environ["CXXFLAGS"])
print(os.environ["CFLAGS"])
print(os.environ["OPENMP_CXX_FLAGS"])
print(os.environ["OPENMP_C_FLAGS"])

openblas = False

if config['amd']:
    # use openblas
    openblas = True
    print("Enable OpenBLAS")
else:
    # use mkl
    print("Enable MKL")
    if 'MKLROOT' in os.environ:
        os.environ['MKL_INCLUDE_DIRS'] = os.environ['MKLROOT']+'/include'
        os.environ['MKL_LIB_DIRS'] = os.environ['MKLROOT']+'/lib/intel64'
    elif config['mkl_root']:
        os.environ['MKLROOT'] = config['mkl_root']
        os.environ['MKL_INCLUDE_DIRS'] = os.environ['MKLROOT']+'/include'
        os.environ['MKL_LIB_DIRS'] = os.environ['MKLROOT']+'/lib/intel64'
    elif config['mkl_include_dirs'] and config['mkl_lib_dirs']:
        os.environ['MKL_INCLUDE_DIRS'] = config['mkl_include_dirs']
        os.environ['MKL_LIB_DIRS'] = config['mkl_lib_dirs']
    else:
        msg = "must set either MKL_INCLUDE_DIRS/MKL_LIB_DIRS or MKLROOT in config.yaml\n"
        print(msg)
        exit()
    os.system('env | grep MKL')

print("Enable: ", config['enable_packages'])

install = config['install']
check_eigen = False
test_Trilinos = config['test_Trilinos']
make_jobs = multiprocessing.cpu_count()/2
if config['make_jobs']:
    make_jobs = config['make_jobs']

k = input("Press Y to continue, else to quit...  ")
if k != 'y' and k != 'Y':
    exit()


cwd = os.getcwd()
log = cwd+'/compile.log'
err = cwd+'/compile.err'
os.system('date >'+log)
os.system('date >'+err)

if openblas:
    # current openblas cannot be built properly
    # load from cluster module
    print(os.environ['OPENBLAS_BASE'])
    # os.chdir(cwd)
    # os.chdir('OpenBLAS')
    # os.system('rm -rf ./build && mkdir ./build')
    # os.chdir('build')
    # os.system('bash ../do-configure-OpenBLAS-AMD.sh && make -j' +
    #           str(make_jobs)+' >> '+log+'  2>>'+err)
    # if install:
    #     os.system('bash ../install.sh ' +
    #               os.environ["SFTPATH"]+' >> '+log+'  2>>'+err)
    pass

# TRNG
if 'trng' in config['enable_packages']:
    os.chdir(cwd)
    os.chdir('TRNG')
    os.system('rm -rf ./build && mkdir ./build')
    os.chdir('build')
    os.system('bash ../do-configure-TRNG4.sh && make -j' +
              str(make_jobs)+' >> '+log+'  2>>'+err)
    os.system('./examples/time')
    if install:
        os.system('make install'+' >> '+log+'  2>>'+err)

# YamlCpp
if 'yamlcpp' in config['enable_packages']:
    os.chdir(cwd)
    os.chdir('YamlCpp')
    os.system('rm -rf ./build && mkdir ./build')
    os.chdir('build')
    os.system('bash ../do-configure-YamlCpp.sh && make -j' +
              str(make_jobs)+' >> '+log+'  2>>'+err)
    if install:
        os.system('make install'+' >> '+log+'  2>>'+err)

# MsgPack
if 'msgpack' in config['enable_packages']:
    os.chdir(cwd)
    os.chdir('MsgPack')
    os.system('rm -rf ./build && mkdir ./build')
    os.chdir('build')
    os.system('bash ../do-configure-MsgPack.sh && make -j' +
              str(make_jobs)+' >> '+log+'  2>>'+err)
    if install:
        os.system('make install'+' >> '+log+'  2>>'+err)

# Eigen
if 'eigen' in config['enable_packages']:
    os.chdir(cwd)
    os.chdir('Eigen')
    os.system('rm -rf ./build && mkdir ./build')
    os.chdir('build')
    os.system('bash ../do-configure-Eigen.sh && make -j' +
              str(make_jobs)+'  >> '+log+'  2>>'+err)
    if check_eigen:
        os.system('make check -j8')
    if install:
        os.system('make install'+' >> '+log+'  2>>'+err)


# VTK
if 'vtk' in config['enable_packages']:
    os.chdir(cwd)
    os.chdir('VTK')
    os.system('rm -rf ./build && mkdir ./build')
    os.chdir('build')
    os.system('bash ../do-configure-VTK.sh && make -j' +
              str(make_jobs)+'  >> '+log+'  2>>'+err)
    if install:
        os.system('make install'+' >> '+log+'  2>>'+err)

# PVFMM
if 'pvfmm' in config['enable_packages']:
    os.chdir(cwd)
    os.chdir('PVFMM')
    os.system('rm -rf ./build && mkdir ./build')
    os.chdir('build')
    if openblas:
        script = 'do-configure-pvfmm-AMD.sh'
    else:
        script = 'do-configure-pvfmm.sh'
    os.system('bash ../'+script+' && make -j' +
              str(make_jobs)+'  >> '+log+'  2>>'+err)
    os.system('PVFMM_DIR=./ ./examples/example1 -N 65536 -omp 4')
    if install:
        os.system('make install'+' >> '+log+'  2>>'+err)

# Trilinos
if 'trilinos' in config['enable_packages']:
    os.chdir(cwd)
    os.chdir('Trilinos')
    os.system('rm -rf ./build && mkdir ./build')
    os.chdir('build')
    if openblas:
        script = 'do-configure-Trilinos-AMD.sh'
    else:
        script = 'do-configure-Trilinos.sh'
    os.system('bash ../'+script+' && make -j' +
              str(make_jobs)+'  >> '+log+'  2>>'+err)
    if test_Trilinos:
        os.environ["OMP_NUM_THREADS"] = "3"
        os.system('make test')
    if install:
        os.system('make install'+' >> '+log+'  2>>'+err)
