import pygame

class backgrond():

    def __init__(self, path = 'backgroundspookyforest.jpg'):
        bg = pygame.image.load(path).convert()
        bg = pygame.transform.scale(bg, (1280, 720))
        