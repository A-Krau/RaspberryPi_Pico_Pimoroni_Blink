import time
import picodisplay
import json

class FileManage:
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
        with open(self.filename) as self.f:
            self.open_file = json.load(self.f)
        return self.open_file

class LCD:
    def flash_a():
        picodisplay.set_pen(175, 175, 175)                  
        picodisplay.clear()                              
        picodisplay.set_pen(255, 255, 255)               
        picodisplay.text("Morning...", 5, 10, 240, 4)  
        picodisplay.set_pen(0, 0, 0)
        picodisplay.text("Its monday!", 5, 50, 240, 5)
        picodisplay.update()
        
    def flash_b():
        picodisplay.set_pen(100, 100, 100)     
        picodisplay.clear()                  
        picodisplay.set_pen(255, 255, 255)               
        picodisplay.text("F#$%!", 5, 10, 240, 5)  
        picodisplay.set_pen(0, 0, 0)
        picodisplay.text("Its monday!", 5, 50, 240, 5)
        picodisplay.update()
        
class Blink:    
    def __init__(self):
        self.thing_switch_time = time.ticks_ms()
        self.state = False
        self.first_loop = True
        print(self.state)
    
    def blink_thing(self, condition_1, condition_2, interval):
        if time.ticks_ms() - self.thing_switch_time >= interval or self.first_loop == True:
            self.first_loop = False
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
            #print("LED INT: " + str(self.led_int))
            return self.led_int
        if key == "lcd_key":
            if picodisplay.is_pressed(picodisplay.BUTTON_X):
                self.lcd_int += 50
            if picodisplay.is_pressed(picodisplay.BUTTON_Y):
                self.lcd_int -= 50
            #print("LCD INT: " + str(self.lcd_int))
            return self.lcd_int

