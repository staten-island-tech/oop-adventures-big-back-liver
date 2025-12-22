import pygame 
from movingBackground import backgrond


class character(pygame.sprite.Sprite):
    def __init__(self, image, width, height):
       
       pygame.sprite.Sprite.__init__(self, )
       self.image = pygame.image.load(image)
       self.image = pygame.transform.scale(self.image, (width, height))
       self.position = self.image.get_rect()
       print(self.position)

bg1 = backgrond()


pygame.init()
time = pygame.time.Clock()
window = pygame.display.set_mode((1280, 720))
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.blit(source= bg1, dest= (0,0) )
    pygame.display.flip()
    time.tick(60)

pygame.quit()