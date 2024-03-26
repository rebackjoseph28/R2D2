import pygame
import pygame.locals as pgl

pygame.init()

# Init Screen
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("R2-D2")

# Init Fonts
font1 = pygame.font.SysFont("helvetica", 20)
font2 = pygame.font.SysFont("arial", 30)

# Init Images
r2d2 = pygame.image.load('images/r2.png')
ctrl = pygame.image.load('images/controller.png')

pos_r2d2 = (320,100)

pygame.joystick.init()

# Initialize the first connected joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()
print("Found controller:", joystick.get_name())

analog_keys = {0: 0, 1: 0, 2: 0, 3: 0, 4: -1, 5: -1}

font = pygame.font.SysFont("helvetica", 20)
white=(255,255,255)
amber = (255,141,51)

def draw_button(xpos,ypos,button):
    if button == 0: # X
        pygame.draw.line(screen, amber, (xpos,ypos),(xpos+15,ypos+20),2)
        pygame.draw.line(screen, amber, (xpos,ypos+20),(xpos+15,ypos),2)
    elif button == 1: # O
        pygame.draw.ellipse(screen, amber, ((xpos,ypos,25,25)), 2)
    elif button == 2: # Square
        pygame.draw.polygon(screen, amber, ((xpos,ypos),(xpos+20,ypos),(xpos+20,ypos+20),(xpos,ypos+20)), 2)
    elif button == 3: # Triangle
        pygame.draw.polygon(screen, amber, ((xpos,ypos+25),(xpos+12,ypos),(xpos+25,ypos+25)), 2)

def draw_joypad(xpos,ypos,keys):
    circlepos = (xpos+10*keys[0],ypos+10*keys[1])
    pygame.draw.ellipse(screen, amber, [circlepos[0],circlepos[1],50,50], 2)

def draw_ui():
    pygame.draw.rect(screen, amber, [20, 20, 600, 420], 2, border_radius=15)
    title = font1.render("R2 ASTROMECH UNIT", False, amber)
    screen.blit(title,(240,450))
    screen.blit(ctrl,(0,-30))

def clear_field():
    pygame.draw.ellipse(screen, "black", (425,120,105,105))
    pygame.draw.ellipse(screen,"black", (195,210,80,80))
    pygame.draw.ellipse(screen,"black", (360,210,80,80))
done = False

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
                    draw_button(500,165,1)
                
                if joystick.get_button(2): # Square
                    draw_button(430,165,2)

                if joystick.get_button(3): # Triangle
                    draw_button(465,125,3)

                if joystick.get_button(5 ): # Optn
                    done = True

            elif event.type == pygame.JOYAXISMOTION:
                analog_keys[event.axis] = event.value

                # Horizontal Analog (Right Stick)
                if abs(analog_keys[0]) > 0.4:
                    if analog_keys[0] < -0.7:
                        print("Left")
                    elif analog_keys[0] > 0.7:
                        print("Right")
                
                # Vertical Analog (Left Stick)
                if abs(analog_keys[1]) > 0.4:
                    if analog_keys[1] < -0.7:
                        print("Up")
                    elif analog_keys[1] > 0.7:
                        print("Down")

                # Horizontal Analog (Right Stick)
                if abs(analog_keys[2]) > 0.4:
                    if analog_keys[2] < -0.7:
                        print("Right Stick Left")
                    elif analog_keys[2] > 0.7:
                        print("Right Stick Right")
                # Vertical Analog (Right Stick)
                if abs(analog_keys[3]) > 0.4:
                    if analog_keys[3] < -0.7:
                        print("Right Stick Up")
                    elif analog_keys[3] > 0.7:
                        print("Right Stick Down")
            
            #Displaying text
            #rstick = font.render("Right Stick: {:.2f}, {:.2f}".format(analog_keys[2],analog_keys[3]), False, white)
            #lstick = font.render("Left Stick: {:.2f}, {:.2f}".format(analog_keys[0],analog_keys[1]), False, white)
            #screen.blit(lstick,(10,10))
            #screen.blit(rstick,(10,30))

            
            #Drawing the joysticks
            draw_joypad(210,225,(analog_keys[0],analog_keys[1]))
            draw_joypad(375,225,(analog_keys[2],analog_keys[3]))
            
            pygame.display.update()
        pygame.display.flip()

except KeyboardInterrupt:
    print("EXITING NOW")
    joystick.quit()

