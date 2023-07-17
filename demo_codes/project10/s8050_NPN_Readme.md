# Procedure:
## Connect the positive terminal of the audio source
##  (e.g., Raspberry Pi's audio output) to the junction of R1 
# and the transistor's base.
# here we are using GPIO12 or GPIO 13 to be left and right channel
# of sound output channel, 
# we need to change /boot/config.txt file before using this function,
# Open and adding following paragraph into the file: 
# dtoverlay=audremap 
# 
# Save it and reboot your Raspberry Pi 4B. 
# * Connect the negative terminal of the audio source to the ground (GND) of the Raspberry Pi and the circuit.
# * Connect the collector of the transistor (the junction of R2 and the transistor's collector) to one terminal of the speaker or headphones.
# * Connect the other terminal of the speaker or headphones to the ground (GND) of the Raspberry Pi and the circuit.
# * Place a coupling capacitor (C1) 1uF between the collector of the transistor and the buzzer/speaker/headphones to block any DC component from reaching the speaker.
# * Connect a resistor (R2) between the collector of the transistor and the positive power supply (+5V).
# * Connect the emitter of the transistor to the ground (GND) of the circuit and the Raspberry Pi.
# * Make sure to choose appropriate resistor values for R1 and R2 based on your specific requirements and the characteristics of the S8050 transistor, in this experiment, we are using 1K resistors as R1 and R2. You may need to experiment with different resistor values to achieve the desired amplification level.

# Additionally, ensure that the audio signal from the Raspberry Pi is compatible with the input requirements of the amplification circuit. You may need to adjust the volume levels on the Raspberry Pi to prevent distortion or clipping in the amplified output.

# Please note that this is a basic amplification circuit, and for more sophisticated audio amplification or higher-quality results, you may need to explore dedicated audio amplifier ICs or modules specifically designed for audio amplification purposes

# After building circuit, login to Raspberry Pi and open a terminal, upload or record a mp3 audio file and play it with cvlc command: 
#
#sudo cvlc Music/my_song.mp3 
#
#And then, you will find your Raspberry Pi 4B’s GPIO 12 or GPIO13
#will trigger the S8050 to drive buzzer play audio!!! have fun! 

