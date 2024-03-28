'''
Project by Joey Reback and Cody Saunders

R2-D2 Robot
'''

import odrive
from odrive.enums import *
import time
import pygame
import pygame.locals as pgl
from math import pi

odrv_enable = False
done = False
white = (255,255,255)
amber = (255,141,51)
pos_r2d2 = (320,100)

analog_keys = {0: 0, 1: 0, 2: 0, 3: 0, 4: -1, 5: -1}

# Connect to ODrive
#odrive_serial_number = "your_odrive_serial_number"
if odrv_enable:
    odrv = odrive.find_any()

pygame.init()

# Init Screen
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("R2-D2")

# Init Fonts
font1 = pygame.font.SysFont("fonts/galbasic.ttf", 24)
font2 = pygame.font.SysFont("fonts/DS-DIGI.ttf", 30)

# Init Images
r2d2 = pygame.image.load('images/r2.png')
ctrl = pygame.image.load('images/controller.png')

# Initialize the first connected joystick

pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
print("Found controller:", joystick.get_name())

def draw_button(xpos,ypos,button):
    if button == 0: # X
        pygame.draw.line(screen, amber, (xpos,ypos),(xpos+15,ypos+20),2)
        pygame.draw.line(screen, amber, (xpos,ypos+20),(xpos+15,ypos),2)
    elif button == 1: # Circle
        pygame.draw.ellipse(screen, amber, ((xpos,ypos,25,25)), 2)
    elif button == 2: # Square
        pygame.draw.polygon(screen, amber, ((xpos,ypos),(xpos+20,ypos),(xpos+20,ypos+20),(xpos,ypos+20)), 2)
    elif button == 3: # Triangle
        pygame.draw.polygon(screen, amber, ((xpos,ypos+25),(xpos+12,ypos),(xpos+25,ypos+25)), 2)
    elif button == 4 or button == 6: # Optn / Share
        pygame.draw.rect(screen, amber, (xpos,ypos,10,30), 2, border_radius=10)
    elif button == 9 or button == 10: # L1 / L2
        pygame.draw.arc(screen, amber, ((xpos,ypos,50,20)),0,pi,2)
    elif button == 15: # Touchpad
        pygame.draw.rect(screen, amber, (xpos,ypos,170,75),2, border_radius=10)

def draw_dpad(xpos,ypos,ang):
    if ang == 1:
        pygame.draw.polygon(screen, amber, ((xpos,ypos),(xpos+20,ypos),(xpos+30, ypos+10),(xpos+20, ypos+20), (xpos,ypos+20)),2)
    if ang == 2:
        pygame.draw.polygon(screen, amber, ((xpos,ypos),(xpos+20,ypos),(xpos+20, ypos+20),(xpos+10, ypos+30), (xpos,ypos+20)),2)
    if ang == 3:
        pygame.draw.polygon(screen, amber, ((xpos,ypos+10),(xpos+10,ypos),(xpos+30,ypos),(xpos+30,ypos+20),(xpos+10,ypos+20)),2)
    if ang == 4:
        pygame.draw.polygon(screen, amber, ((xpos+10,ypos),(xpos+20,ypos+10),(xpos+20,ypos+30),(xpos,ypos+30),(xpos,ypos+10)),2)

def draw_joypad(xpos,ypos,keys):
    circlepos = (xpos+10*keys[0],ypos+10*keys[1])
    pygame.draw.ellipse(screen, amber, [circlepos[0],circlepos[1],50,50], 2)

def draw_ui():
    pygame.draw.rect(screen, amber, [20, 20, 600, 420], 2, border_radius=15)
    title = font1.render("R2 ASTROMECH UNIT", False, amber)
    screen.blit(title,(240,450))
    screen.blit(ctrl,(0,-30))

def clear_field():
    pygame.draw.rect(screen,"black",(50,50,500,40))
    pygame.draw.ellipse(screen, "black", (425,120,105,105))
    pygame.draw.ellipse(screen,"black", (195,210,80,80))
    pygame.draw.ellipse(screen,"black", (360,210,80,80))

def move_axis(input,axis):
    if odrv_enable:
        if axis == 0:
            odrv.axis0.controller.input_vel = 2.0*input
        if axis == 1:
            odrv.axis1.controller.input_vel = 2.0*input

try:
    while not done:
        draw_ui()
        for event in pygame.event.get():
            clear_field()
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            elif event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(0): # X Button
                    draw_button(470,195,0)
                
                if joystick.get_button(1): # O Button
                    draw_button(500,160,1)
                
                if joystick.get_button(2): # Square
                    draw_button(430,160,2)

                if joystick.get_button(3): # Triangle
                    draw_button(465,125,3)

                if joystick.get_button(9): # Rotate Head Left
                    draw_button(130,80,9)

                if joystick.get_button(10): # Rotate Head Right
                    draw_button(450,80,10)

                if joystick.get_button(12): # PS Button
                    done = True
                
            elif event.type == pygame.JOYAXISMOTION:
                analog_keys[event.axis] = event.value

                # Move Left Motor (Left Stick)
                if abs(analog_keys[1]) > 0.2:
                    move_axis(analog_keys[0],0)
                elif abs(analog_keys[1]) < 0.2:
                    move_axis(0,0)
            
                # Move Right Motor (Right Stick)
                if abs(analog_keys[3]) > 0.2:
                    move_axis(analog_keys[3],1)
                elif abs(analog_keys[3]) < 0.2:
                    move_axis(0,1)

            #Drawing the joysticks
            draw_joypad(210,225,(analog_keys[0],analog_keys[1]))
            draw_joypad(375,225,(analog_keys[2],analog_keys[3]))
            
            pygame.display.update()
        pygame.display.flip()

except KeyboardInterrupt:
    print("EXITING NOW")
    joystick.quit()

