# We can use a simple 
# while loop with the mylcd.lcd_display_string() 
# and mylcd.lcd_clear() functions to create a continuous 
# blinking text effect:
import time
import I2C_LCD_driver


mylcd = I2C_LCD_driver.lcd()

while True:
    mylcd.lcd_display_string(u"Hello world!")
    time.sleep(1)
    mylcd.lcd_clear()
    time.sleep(1)

# You can use the time.sleep() function on line 7 to change the time 
#(in seconds) the text stays on. 
# The time the text stays off can be changed in 
# the time.sleep() function on line 9. 
# To end the program, press Ctrl-C.

