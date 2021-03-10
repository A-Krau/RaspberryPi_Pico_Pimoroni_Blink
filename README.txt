# RaspberryPi_Pico_Pimoroni_Blink

When running the linked code, Thonny and RP Pico will freeze and require the RP Pico to be unplugged and plugged back in. After power cycle code will run fine. Stopping and rerunning the same code with Thonny will cause the issue to return.

https://github.com/A-Krau/RaspberryPi_Pico_Pimoroni_Blink

Commenting out all lines after 43 in main.py eliminate the problem which leads me to believe it has to do with writing the json file which happens in the Class FileManage in Blinky.py.

Thonny 3.3.3
Windows 10 (64-bit)
Python 3.7.9 (32-bit)
Tk 8.6.9

pimoroni-pico-micropython.uf2 0.0.9
https://github.com/pimoroni/pimoroni-pico/releases

Thonny 3.3.3
Windows 10 (64-bit)
Python 3.7.9 (32-bit)
Tk 8.6.9

pimoroni-pico-micropython.uf2 0.0.9
https://github.com/pimoroni/pimoroni-pico/releases
