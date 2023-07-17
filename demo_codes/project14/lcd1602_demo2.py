import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Hello World!", 2, 3)

# On a 16×2 LCD, 
# the rows are numbered 1 – 2, 
# while the columns are numbered 0 – 15. 
# So to print “Hello World!” 
# at the first column of the top row, you would use 
mylcd.lcd_display_string("Hello World!", 1, 0).


