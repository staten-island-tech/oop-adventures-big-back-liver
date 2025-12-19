import pygame 


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