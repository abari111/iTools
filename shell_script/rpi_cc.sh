#! /bin/bash

set -e

#=============== SOME UTILITIES TO DOWNLOAD =======================================================================================================================================
#sudo apt-get install g++ make gawk #Deja installe
#=============== SOME VARIABLES FOR THE SCRIPT=====================================================================================================================================
CC_DIR="/home/abari/abari_cc_src/abari_cc"
TARGET="arm-abariDodo-linux-gnueabihf"
LINUX_ARCH=arm64
CONFIG_OPT="--disable-multilib"
BIN_VERSION=binutils-2.36
GCC_VERSION=gcc-10.2.0
KERNEL_VERSION=linux-5.4.9
GLIBC_VERSION=glibc-2.32
MPFR_VERSION=mpfr-4.1.0
GMP_VERSION=gmp-6.2.1
MPC_VERSION=mpc-1.2.0
ISL_VERSION=isl-0.18
CLOOG_VERSION=cloog-0.18.1
export 	PATH=$CC_DIR/bin:$PATH
#============== DOWNLOAD SRC TO abari_cc_src====================================================================================================================================
 cd ~/abari_cc_src
 
 #wget https://ftp.gnu.org/gnu/binutils/$BIN_VERSION.tar.gz
 #wget https://ftp.gnu.org/gnu/gcc/$GCC_VERSION/$GCC_VERSION.tar.gz
 #wget https://cdn.kernel.org/pub/linux/kernel/v5.x/$KERNEL_VERSION.tar.gz
 #wget https://ftp.gnu.org/gnu/glibc/$GLIBC_VERSION.tar.gz
 #wget https://ftp.gnu.org/gnu/mpfr/$MPFR_VERSION.tar.gz
 #wget https://ftp.gnu.org/gnu/mpc/$MPC_VERSION.tar.gz
 #wget https://ftp.gnu.org/gnu/gmp/$GMP_VERSION.tar.xz
 #wget https://gcc.gnu.org/pub/gcc/infrastructure/$ISL_VERSION.tar.bz2
 #wget https://gcc.gnu.org/pub/gcc/infrastructure/$CLOOG_VERSION.tar.gz

 #=============== EXTRACTING SRC ================================================================================================================================================
 for f in *.tar*; do tar xfk $f; done

 #===============================================================================================================================================================================
 #                                                                            DEBUT DE LA PROCEDURE
 #===============================================================================================================================================================================


 #=========== SYMBOLIC FOR mpfr mpc gmp isl cloog===============================================================================================================================
 cd $GCC_VERSION
 ln -sf `ls -1d ../mpfr-*/` mpfr
 ln -sf `ls -1d ../gmp-*/` gmp
 ln -sf `ls -1d ../mpc-*/` mpc
 ln -sf `ls -1d ../isl-*/` isl
 ln -sf `ls -1d ../cloog-*/` cloog
 cd ..

 #=========== BUILDING BINUTILS===============================================================================================================================
 mkdir -p abari_build_binutils
 cd abari_build_binutils
 ../$BIN_VERSION/configure --prefix=$CC_DIR --target=$TARGET $CONFIG_OPT
 make -j4
 make install
 cd ..

 #=========== LINUX KERNEL HEADERS===============================================================================================================================
 cd $KERNEL_VERSION
 make ARCH=$LINUX_ARCH INSTALL_HDR_PATH=$CC_DIR/$TARGET headers_install
 cd ..

 #=========== C/C++ COMPILERS===============================================================================================================================
  mkdir -p abari_build-gcc
  cd abari_build-gcc
  ../$GCC_VERSION/configure --prefix=$CC_DIR --target=$TARGET --enable-languages="c,c++" --disable-multilib
  make -j4 all-gcc
  make install-gcc
  cd ..

  #=========C LIBRARY FILES AND STARTUP FILES===============================================================================================================================
  mkdir -p abari_build-glibc
  cd abari_build-glibc
  ../$GLIBC_VERSION/configure --prefix=$CC_DIR/$TARGET --build=$MACHTYPE --host=$TARGET --target=$TARGET --with-headers=$CC_DIR/$TARGET/include libc_cv_forced_unwind=yes $CONFIG_OPT 
  make install-bootstrap-headers=yes install-headers
  make -j4 csu/subdir_lib
  install csu/crt1.o csu/crti.o csu/crtn.o $CC_DIR/$TARGET/lib
  $TARGET-gcc -nostdlib -nostartfiles -shared -x c /dev/null -o $CC_DIR/$TARGET/lib/libc.so
  touch $CC_DIR/$TARGET/include/gnu/stubs.h
  cd ..

  #==========COMPILER SUPPORT LIBRARY===============================================================================================================================
   cd abari_build-gcc
   make -j4 all-target-libgcc
   make install-target-libgcc
   cd ..

  #==========STANDARD LIBRARY & REST OF GLIBC===============================================================================================================================
  cd abari_build-glibc
  make -j4
  make install
  cd ..

  #========== STANDARD C++ LIBRARY===============================================================================================================================
  cd abari_build-gcc
  make -j4 all
  make install
  cd ..


  #=============================================================================================================================================================================================
  #=============================================================================================================================================================================================

