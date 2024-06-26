import pygame
import random

class Sounds:
    pygame.mixer.init()
    sound_enable = True
    dir = "sounds/"
    ext = ".mp3"

    gen1 = pygame.mixer.Sound(dir + "gen1" + ext)
    gen2 = pygame.mixer.Sound(dir + "gen2" + ext)
    gen3 = pygame.mixer.Sound(dir + "gen3" + ext)
    gen4 = pygame.mixer.Sound(dir + "gen4" + ext)
    gen5 = pygame.mixer.Sound(dir + "gen5" + ext)
    gen6 = pygame.mixer.Sound(dir + "gen6" + ext)
    gen7 = pygame.mixer.Sound(dir + "gen7" + ext)
    gen8 = pygame.mixer.Sound(dir + "gen8" + ext)
    gen9 = pygame.mixer.Sound(dir + "gen9" + ext)

    emote1 = pygame.mixer.Sound(dir + "emote1" + ext)
    emote2 = pygame.mixer.Sound(dir + "emote2" + ext)
    emote3 = pygame.mixer.Sound(dir + "emote3" + ext)
    emote4 = pygame.mixer.Sound(dir + "emote4" + ext)
    emote5 = pygame.mixer.Sound(dir + "emote5" + ext)
    emote6 = pygame.mixer.Sound(dir + "emote6" + ext)
    emote7 = pygame.mixer.Sound(dir + "emote7" + ext)

    happy1 = pygame.mixer.Sound(dir + "happy1" + ext)
    happy2 = pygame.mixer.Sound(dir + "happy2" + ext)
    happy3 = pygame.mixer.Sound(dir + "happy3" + ext)
    happy4 = pygame.mixer.Sound(dir + "happy4" + ext)
    happy5 = pygame.mixer.Sound(dir + "happy5" + ext)
    happy6 = pygame.mixer.Sound(dir + "happy6" + ext)
    happy7 = pygame.mixer.Sound(dir + "happy7" + ext)

    chat1 = pygame.mixer.Sound(dir + "chat1" + ext)
    chat2 = pygame.mixer.Sound(dir + "chat2" + ext)
    chat3 = pygame.mixer.Sound(dir + "chat3" + ext)
    chat4 = pygame.mixer.Sound(dir + "chat4" + ext)
    chat5 = pygame.mixer.Sound(dir + "chat5" + ext)
    chat6 = pygame.mixer.Sound(dir + "chat6" + ext)
    chat7 = pygame.mixer.Sound(dir + "chat7" + ext)
    chat8 = pygame.mixer.Sound(dir + "chat8" + ext)
    chat9 = pygame.mixer.Sound(dir + "chat9" + ext)

    help = pygame.mixer.Sound(dir + "help" + ext)
    scream = pygame.mixer.Sound(dir + "scream" + ext)

    gen_dict = {
        1 : gen1,
        2 : gen2,
        3 : gen3,
        4 : gen4,
        5 : gen5,
        6 : gen6,
        7 : gen7,
        8 : gen8,
        9 : gen9,
    }

    emote_dict = {
        1 : emote1,
        2 : emote2,
        3 : emote3,
        4 : emote4,
        5 : emote5,
        6 : emote6,
        7 : emote7,
    }

    happy_dict = {
        1 : happy1,
        2 : happy2,
        3 : happy3,
        4 : happy4,
        5 : happy5,
        6 : happy6,
        7 : happy7
    }

    chat_dict = {
        1 : chat1,
        2 : chat2,
        3 : chat3,
        4 : chat4,
        5 : chat5,
        6 : chat6,
        7 : chat7,
        8 : chat8,
        9 : chat9
    }

    other_dict = {
        "scream" : scream,
        "help" : help
    }

    def __init__(sound_enable):
        Sounds.sound_enable = sound_enable

    def play_sound(type):
        if type == "gen":
            n = random.randrange(1,9)
            sound = Sounds.gen_dict[n]
        elif type == "emote":
            n = random.randrange(1,7)
            sound = Sounds.emote_dict[n]
        elif type == "happy":
            n = random.randrange(1,6)
            sound = Sounds.happy_dict[n]
        elif type == "chat":
            n = random.randrange(1,9)
            sound = Sounds.chat_dict[n]
        elif type == "help":
            sound = Sounds.other_dict[type]
        elif type == "scream":
            sound = Sounds.other_dict[type]
        pygame.mixer.Sound.play(sound)