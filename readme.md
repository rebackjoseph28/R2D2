
# Real Life R2-D2

Designed for an ECE 202 sophmore project. Goal is to create a remotely controlled R2-D2, with room for expansion and other functionalities.

## Parts ##
Part Name      | Info
-------------  | -------------
Odrive v3.6    | Depreciated by Odrive, but still works well, get an odesc if you can't find one
Hoverboard     | any works, make sure to follow the odrive hoverboard-specific guide
Raspberry Pi   | We're using a 3B+ but it shouldn't matter, recommend using a screen too to run code with
PS4 Controller | Both on and offbrand ones work, the controller visualization can show you if you're mapping is off
24V Relay      | For powering the odrive without frying the switch
24V Stepdown   | For powering the pi at the correct voltage / amperage

Power system comes from the hoverboard, however it is recommended to add a 24V+ rated relay and a fuse to make sure nothing goes awry.

### File Directory ###
These are the important directories:

Folder         | Contains
-------------  | -------------
test           | any test / setup files
images         | images for the visualizer

#### Test Directory ####

File           | Info
-------------  | -------------
controller.py  | Testing the controller inputs
gpio_test.py   | Testing leds and stepper motor
os_test.py     | Testing to change controller mapping based on os
screen_test.py | Depreciated pygame testing

Mostly you will be using main.py as this contains everything you will need for running the code.

## Setup ##
Odrives when they work well are a godsend, however getting them to work was what took most of the time in this project.
We use the odrive guide on odrive's wiki with some other help. I'll link all guides used for help. 

### Make Sure: ###
- Odrive Encoders are connected to 3.3V and not 5V, it messes with the signal
- Odrive firmware worked best on v5.1 with our hall encoder setup
- Run calibration code (setup.py), and modify any values per the hoverboard guide

## Editing the Code ##
As it stands currently, the code itself very plug and play after setup, the only edit that you want to make is in main.py.

Change to true when using the odrive, this line was added for testing (line 14):
```
odrv_enable = False
```
If you want to see ui without the odrive connected, you can turn it off.

## Running the code ##
All you need to run is the main.py file, make sure you have the newest version of python and pygame.

## Robot Control ##
- Controlling the robot is tank controls, so one stick moves one side forward/backward.
- Any action buttons make noises (TODO)
- Playstation button kills the program
- Shoulder buttons move the turret gears (TODO)

## Troubleshooting ##
- Any communication errors coming from the encoders, add either 47nf or 22nf capacitors in paralell for grounding (see odrive guide for more info)
- Our encoders cannot be supplied anything greater than 3.3V, so don't wire your encoder to 5V or else you'll get bad noise
- Make sure you've downloaded all the necessary libraries!!

## TODO ##
- Get head rotating
- Get LEDs blinking
- Get sound effects working
