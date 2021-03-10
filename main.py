import time
import picodisplay
from Blinky import LCD
from Blinky import Blink
from Blinky import Buttons
from Blinky import FileManage

# Initialise Picodisplay with a bytearray display buffer
buf = bytearray(picodisplay.get_width() * picodisplay.get_height() * 2)
picodisplay.init(buf)
picodisplay.set_backlight(.5)

#set colors
orange = (100, 100, 255)
blue = (255, 102, 0)
gray = (125, 128, 128)
white = (200, 255, 255)

#set variables
buttons = (picodisplay.BUTTON_A, picodisplay.BUTTON_B, picodisplay.BUTTON_X, picodisplay.BUTTON_Y)
led_orange = (picodisplay.set_led, orange)
led_blue = (picodisplay.set_led, blue)
led_gray = (picodisplay.set_led, gray)
led_white = (picodisplay.set_led, white)

#save stuff
last_save = time.ticks_ms()
save_int = 1000

#class subtantiation
led = Blink()
screen = Blink()
saved = FileManage("saved", 250)
int_dict = saved.read()  # blink interval
click = Buttons(int_dict)

if __name__ == "__main__":
    while True:
        led.blink_thing(led_white, led_gray, int_dict.get("led_key"))
        screen.blink_thing((LCD.flash_monday, None), (LCD.flash_monday_white, None), int_dict.get("lcd_key"))
        for key in int_dict:  #set blink intervals based on
            int_dict[key] = click.rate_control(key)
        #Commenting out the code below will cuse the code to run witout issue
        if time.ticks_ms() - last_save >= save_int:
            print("Saving...")
            saved.write(int_dict)
            last_save = time.ticks_ms()
            
        