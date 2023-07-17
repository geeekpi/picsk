# First we have to install Adfruit DHT library for this tutorial. 
# Login to raspberry pi via VNC Viewer or SSH (Using putty) 
# and run the below code.
#
# git clone https://github.com/adafruit/Adafruit_Python_DHT.git
#
# It will download the necessary files under a folder named 
# Adafruit_Python_DHT. Once your download in completed run the command
#  “ls” for listing the files and folders. 
# You will see Adafruit_Python_DHT is listed there.
#
# pi@raspberrypi:~ $ ls
#Adafruit_Python_DHT Desktop
#Now go to Adafruit_Python_DHT folder as shown below
#
#pi@raspberrypi:~ $ cd Adafruit_Python_DHT/
#
#Run the below command for installation of Python version 2 and 3
#
#sudo python setup.py install
#
#sudo python3 setup.py install
#
#pi@raspberrypi:~/Adafruit_Python_DHT $ sudo python setup.py install
#
#pi@raspberrypi:~/Adafruit_Python_DHT $ sudo python3 setup.py install
#
#Once the python installation please make sure 
# GPIO is enabled in your raspberry Pi. 
# Run the below command and enable it.
#
#pi@raspberrypi:~ $ sudo raspi-config
#pi@raspberrypi:~/Adafruit_Python_DHT $ cd

### How to run the same code in Raspberry Pi 4?
# For executing the same python code in Raspberry Pi 4 
# we have to make some changes. 
# The above library supports till Raspberry Pi 3.
# Now to make it compatible with Raspberry Pi 4 
# we have to make below changes.
# Go to below directory
#
#/usr/local/lib/python3.7/dist-packages/Adafruit_DHT/
#
#pi@raspberrypi:~ $ cd /usr/local/lib/python3.7/dist-packages/Adafruit_DHT/
#
#Again list the files and folders with “ls” command as shown below
#
#pi@raspberrypi:/usr/local/lib/python3.7/dist-packages/Adafruit_DHT $ ls
#Beaglebone_Black.py __pycache__
#common.py Raspberry_Pi_2_Driver.cpython-37m-arm-linux-gnueabihf.so
#common.py.bup Raspberry_Pi_2.py
#__init__.py Raspberry_Pi.py
#platform_detect.py Test.py
#
#You will see a file named platform_detect.py, 
# This is the file we have to edit. 
# Since this file has read only permissions hence 
# we can’t make changes and save it. In order to change this file, 
# we have to change the permission of this file. 
# you can run below command to change the permission.
#
#sudo chmod a+w platform_detect.py
#
#pi@raspberrypi:/usr/local/lib/python3.7/dist-packages/Adafruit_DHT# 
# sudo chmod a+w platform_detect.py
#
# Now go to directory /usr/local/lib/python3.7/dist-packages/Adafruit_DHT
# and open the file platform_detect.py.
# Once you open it, 
# add the below lines of code at the bottom and save it.
# 
#
#elif match.group(1) == 'BCM2711':
#Pi 4b
#return 3
#Alternate way to edit this file
# You can edit platform_detect.py using putty by remote SSH session. 
# First navigate to usr/local/lib/python3.7/dist-packages/Adafruit_DHT # directory and then run the below command.
#
#nano platform_detect.py
#
#pi@raspberrypi:/usr/local/lib/python3.7/dist-packages/Adafruit_DHT $
# nano platform_detect.py
#
#You can add the same set of code here and save the file.
#After that, you can coding it with your favourate editor.



