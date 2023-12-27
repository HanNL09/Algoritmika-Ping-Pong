import pygame

pygame.init()

RES = width,height = 700,500
window = pygame.display.set_mode(RES)
pygame.display.set_caption("Ping Fong")

fps = pygame.time.Clock()
frame = 30

while True:
    window.fill((100,230,255))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    pygame.display.update()
    fps.tick(frame)