import pygame
from math import fabs,sqrt
from random import randint

pygame.init()

RES = width,height = 700,500
window = pygame.display.set_mode(RES)
pygame.display.set_caption("Ping Fong")

fps = pygame.time.Clock()
frame = 30

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,playerImage,speed,coordinates,dimension=(50,50)):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(playerImage+".png"),dimension
        )
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = coordinates[0]
        self.rect.y = coordinates[1]
    def update(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Ball(GameSprite):
    # def __init__(self,playerImage,speed,coordinates,dimension,direction):
    #     super().__init__()
    #     self.direction = direction
    def move(self):
        # if self.speed < 0:
        #     speedx = sqrt(fabs(self.speed)**2+self.direction**2)
        #     speedy = sqrt()
        self.rect.x += self.speed
        self.rect.y += self.speed
        self.update()

ball = Ball("ball",3,(width/2-25,height/2-25))

while True:
    window.fill((100,230,255))

    ball.move()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    pygame.display.update()
    fps.tick(frame)