import time
import picodisplay
from Blinky import LCD
from Blinky import Blink
from Blinky import Buttons
from Blinky import FileManage
from copy import copy


# Initialise Picodisplay with a bytearray display buffer
buf = bytearray(picodisplay.get_width() * picodisplay.get_height() * 2)
picodisplay.init(buf)
picodisplay.set_backlight(1)

#set colors
blue = (0, 0, 255)
orange = (255, 102, 0)
gray = (125, 128, 128)
white = (200, 255, 255)
red = (255, 0, 0) 

#set variables
buttons = (picodisplay.BUTTON_A, picodisplay.BUTTON_B, picodisplay.BUTTON_X, picodisplay.BUTTON_Y)
led_orange = (picodisplay.set_led, orange)
led_blue = (picodisplay.set_led, blue)
led_gray = (picodisplay.set_led, gray)
led_white = (picodisplay.set_led, white)
led_red = (picodisplay.set_led, red)

#save stuff
last_save = time.ticks_ms()
save_int = 1000

#class subtantiation
led = Blink()
screen = Blink()
saved = FileManage("saved", 250)
int_dict = saved.read()  # blink interval
saved_dict = copy(int_dict)
click = Buttons(int_dict)
print(int_dict)
print(saved_dict)

if __name__ == "__main__":
    while True:
        led.blink_thing(led_white, led_blue, int_dict.get("led_key"))
        screen.blink_thing((LCD.flash_a, None), (LCD.flash_b, None), int_dict.get("lcd_key"))
        for key in int_dict:  #set blink intervals based on
            int_dict[key] = click.rate_control(key)
        #Commenting out the code below will cuse the code to run witout issue
        if  time.ticks_ms() - last_save >= save_int and saved_dict != int_dict:
            print("Saving...")
            saved.write(int_dict)
            saved_dict = copy(int_dict)
            print(saved_dict)
            last_save = time.ticks_ms()
            
        
