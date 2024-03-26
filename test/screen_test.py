import pygame
import pygame.locals as pgl
from math import pi

pygame.init()
screen = pygame.display.set_mode((640, 480))

r2d2 = pygame.image.load('images/r2.png')
ctrl = pygame.image.load('images/controller.png')
pygame.display.set_caption("R2-D2")

pos_r2d2 = (320,100)

pygame.joystick.init()
clock = pygame.time.Clock()

font1 = pygame.font.SysFont("helvetica", 20)
font2 = pygame.font.SysFont("arial", 30)
amber = (255,141,51)
white=(255,255,255)
done = False

def draw_joypad(xpos,ypos,keys):
    circlepos = (xpos+10*keys[0],ypos+10*keys[1])
    pygame.draw.ellipse(screen, amber, [circlepos[0],circlepos[1],50,50], 2)

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
    elif button == 4: # L1 / L2
        pygame.draw.arc(screen, amber, ((xpos,ypos,50,20)),0,pi,2)
    elif button == 5: # Optn / Start
        pygame.draw.rect(screen, amber, (xpos,ypos,10,30), 2, border_radius=10)
    elif button == 6: # Touchpad
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

def screen_test():
    #joysticks
    draw_joypad(210,225,(analog_keys[0],analog_keys[1]))
    draw_joypad(375,225,(analog_keys[2],analog_keys[3]))

    #text and controller image
    pygame.draw.rect(screen, amber, [20, 20, 600, 420], 2, border_radius=15)
    title = font1.render("R2 ASTROMECH UNIT", False, amber)
    screen.blit(title,(240,450))
    screen.blit(ctrl,(0,-30))

    # Action Buttons
    draw_button(470,195,0)
    draw_button(500,165,1)
    draw_button(465,125,3)
    draw_button(430,165,2)

    # L1 / R1
    draw_button(130,80,4)
    draw_button(450,80,4)

    # Start / Option
    draw_button(215,105,5)
    draw_button(405,105,5)

    # Touchpad
    draw_button(230,105,6)

    # D-Pad
    draw_dpad(110,160,1)
    draw_dpad(145,130,2)
    draw_dpad(170,160,3)  
    draw_dpad(145,180,4)     

    #print(str(pygame.mouse.get_pos()))
    

analog_keys = [0,0,0,0]
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True
        screen_test()
        pygame.display.update()

pygame.quit()