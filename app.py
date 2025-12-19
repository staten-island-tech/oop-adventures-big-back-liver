import pygame 


pygame.init()
time = pygame.time.Clock()
window = pygame.display.set_mode()
running = True
bg. 

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

pygame.quit()