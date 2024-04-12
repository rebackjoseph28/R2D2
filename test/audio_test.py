import pygame

sound_enable = True

pygame.mixer.init()
dir = "/sounds/"

sfx1 = pygame.mixer.Sound(dir + "sfx1")
sfx2 = pygame.mixer.Sound(dir + "sfx2")

sound_dict = {
    "sfx1": sfx1,
    "sfx2": sfx2
}
#bee
def play_sound(filename):
    if(sound_enable):
        pygame.mixer.Sound.play(sound_dict[filename])

play_sound("sfx1")