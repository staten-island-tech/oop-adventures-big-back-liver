import pygame 



class character(pygame.sprite.Sprite):
    def __init__(self, image, width, height):
       
       pygame.sprite.Sprite.__init__(self, )
       self.image = pygame.image.load(image)
       self.rect = self.image.get_rect()















pygame.init()
time = pygame.time.Clock()
window = pygame.display.set_mode((1280, 720))
running = True
bg = pygame.image.load('backgroundspookyforest.jpg') 
bg = pygame.transform.scale(bg, (1280, 720))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.blit(source= bg, dest= (0,0) )
    pygame.display.flip()
    time.tick(60)

pygame.quit()