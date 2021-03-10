import time
import picodisplay
import json

class FileManage:
    """Open and save json file to create persistance between power cycles"""
    def __init__(self, fn, interval):
        self.filename = fn + "_intervals.json"
        self.default_times = {"led_key": interval, "lcd_key": interval}
        try:
            temp = open(self.filename)
            temp.close()
        except OSError:
            with open(self.filename, "w") as json_file:
                json.dump(self.default_times, json_file)
                print("Default values loaded...")
        finally:
            print("Initialized...")
            
    def write(self, dict_x):
        with open(self.filename, "w") as json_file:
            json.dump(dict_x, json_file)

    def read(self):
        with open(self.filename) as f:
            open_file = json.load(f)
        return open_file

class LCD:
    """Define states for the Pimoroni Pack and call them."""
    def flash_monday():
        picodisplay.set_pen(128, 128, 128)                  
        picodisplay.clear()                              
        picodisplay.set_pen(255, 255, 255)               
        picodisplay.text("Morning!", 5, 10, 240, 5)  
        picodisplay.set_pen(0, 0, 0)
        picodisplay.text("Its Monday!", 5, 50, 240, 5)
        picodisplay.update()
        
    def flash_monday_white():
        picodisplay.set_pen(255, 255, 255)     
        picodisplay.clear()                  
        picodisplay.set_pen(128, 128, 128)               
        picodisplay.text("Morning!", 5, 10, 240, 5)  
        picodisplay.set_pen(0, 0, 0)
        picodisplay.text("Its Monday!", 5, 50, 240, 5)
        picodisplay.update()
        
class Blink:
    """Blink without delay"""
    
    def __init__(self):
        self.thing_switch_time = time.ticks_ms()
        self.state = False
        print(self.state)
    
    def blink_thing(self, condition_1, condition_2, interval):
        if time.ticks_ms() - self.thing_switch_time >= interval:
            if self.state == True:
                func, conargs= condition_1
                self.call_condition(func, conargs)
                self.thing_switch_time = time.ticks_ms()
                self.state = False
            else:
                func, conargs= condition_2
                self.call_condition(func, conargs)
                self.thing_switch_time = time.ticks_ms()
                self.state = True
        time.sleep(.01)
                
    def call_condition(self, x, y):
        if y is None:
            x()
        else:
            x(*y)

class Buttons:
    def __init__(self,interval_dict):
        self.led_int = interval_dict["led_key"]
        self.lcd_int = interval_dict["lcd_key"]
    def rate_control(self, key):
        if key == "led_key":
            if picodisplay.is_pressed(picodisplay.BUTTON_A):
                self.led_int += 50
            if picodisplay.is_pressed(picodisplay.BUTTON_B):
                self.led_int -= 50
            print("LED INT: " + str(self.led_int))
            return self.led_int
        if key == "lcd_key":
            if picodisplay.is_pressed(picodisplay.BUTTON_X):
                self.lcd_int += 50
            if picodisplay.is_pressed(picodisplay.BUTTON_Y):
                self.lcd_int -= 50
            print("LCD INT: " + str(self.lcd_int))
            return self.lcd_int

