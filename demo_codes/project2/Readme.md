# The C code needs to rely on the wiringPi library file, 
# which needs to be downloaded and installed through the link below.
# URL: http://wiringpi.com/ 
# or
# URL: https://github.com/WiringPi
# command: git clone https://github.com/WiringPi/WiringPi.git
# How to install wiringPi
# =======================

#The easiest way is to use the supplied 'build' script:
#
##  ./build
#
#that should do a complete install or upgrade of wiringPi for you.
#
#That will install a dynamic library.
#
#Some distributions do not have /usr/local/lib in the default LD_LIBRARY_PATH. To
#fix this, you need to edit /etc/ld.so.conf and add in a single line:
#
#  /usr/local/lib
#
#then run the ldconfig command.
#
#  sudo ldconfig
#
#To un-install wiringPi:
#
#  ./build uninstall
#
#For help and support see:
#
#* https://github.com/WiringPi/WiringPi/issues
#* https://discord.gg/SM4WUVG
#
#
#wiringPi originally created by Gordon Henderson
#https://projects.drogon.net/

## How to compile mpu6050 c code?
## make sure you have installed build-essential package 
# sudo apt-get update 
# sudo apt-get -y upgrade 
# sudo apt-get -y install build-essential
## Compile the demo code 
# gcc -o mpu6050-test  MPU6050_sensor_demo2.c -lwiringPi 
## Execute 
# ./mpu6050-test
## Have fun

