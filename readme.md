
# Real Life R2-D2

Designed for an ECE 202 sophmore project. Goal is to create a remotely controlled R2-D2, with room for expansion and other functionalities.

## Parts ##
Part Name      | Link
-------------  | -------------
Odrive v3.6    | 
Hoverboard     | 
Raspberry Pi   | 
PS4 Controller | 

Power system comes from the hoverboard, however it is recommended to add a 24V+ rated relay and a fuse to make sure nothing goes awry.

### File Directory ###
These are the important directories:

Folder         | Contains
-------------  | -------------
test           | any test / setup files
images         | images for  (main arduino file)

Mostly you will be using main.py as this contains everything you will need for running the code.

## Setup ##
Odrives when they work well are a godsend, however getting them to work was what took most of the time in this project.

## Editing the Code ##
As it stands currently, the code itself very plug and play after setup, the only edit that you want to make is in main.py.

Replace with network info on line 14:
```
odrv_enable = False
```
This line was added for testing the ui without the odrive connected.

## Running the code ##
Make sure you have both an odrive properly connected, and a controller. Specifically for this project we use a PlayStation 4 controller.

-> Build Filesystem image

-> Upload and Monitor

## Accessing the Webserver ##
Once you get to this step you should be successfully running your code. In the serial monitor it should tell you what the ESP32's IP address is.

Log into your router, and go to that IP address. If you did everything correctly you should see your website with realtime data.

## Troubleshooting ##
- Make sure when you're uploading the code, that you don't have the ports open or else you won't be able to access them.
- If for whatever reason you need to change filenames make sure you change any references in all the files
- The ESP32 that I use has 4MB of flash memory which means that any 3D model has to be simplified to fit. Removing chamfers can sometimes save you up to 500kb of data.
