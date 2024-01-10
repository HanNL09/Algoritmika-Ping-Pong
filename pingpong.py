import pygame
from math import fabs,sqrt
from random import randint

pygame.init()
pygame.font.init()

RES = width,height = 700,500
window = pygame.display.set_mode(RES)
pygame.display.set_caption("Ping Fong")

fps = pygame.time.Clock()
frame = 60

# Game Variables
paddle_speed = 3
ball_speed = 2

left_score = 0
right_score = 0
#
# Fonts
score = pygame.font.SysFont("calibri",40)
#

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,playerImage,speed,coordinates,dimension=(32,32)):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(playerImage+".png"),dimension
        )
        self.speed_x,self.speed_y = speed,speed
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
        global left_score,right_score
        # if self.speed < 0:
        #     speedx = sqrt(fabs(self.speed)**2+self.direction**2)
        #     speedy = sqrt()
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.update()
        if self.rect.x < 0:
            left_score += 1
            self.rect.x = width/2-self.rect.width/2
            self.rect.y = height/2-self.rect.height/2
        if (self.rect.x+self.rect.width) > width:
            right_score += 1
            self.rect.x = width/2-self.rect.width/2
            self.rect.y = height/2-self.rect.height/2
class Paddle(GameSprite):
    def move(self,side):
        key_pressed = pygame.key.get_pressed()
        up = 0
        down = 0
        if side == "left":
            if key_pressed[pygame.K_w]:
                up = 0 - self.speed_y
            if key_pressed[pygame.K_s]:
                down = self.speed_y
        else:
            if key_pressed[pygame.K_UP]:
                up = 0 - self.speed_y
            if key_pressed[pygame.K_DOWN]:
                down = self.speed_y
        self.rect.y += up + down
        self.update()

ball = Ball("ball",ball_speed,(width/2-25,height/2-25))
left_paddle = Paddle("blue_paddle",paddle_speed,(30,200),(25,100))
right_paddle = Paddle("red_paddle",paddle_speed,(645,200),(25,100))

while True:
    window.fill((0,0,0))

    ball.move()
    left_paddle.move("left")
    right_paddle.move("right")
    
    if pygame.sprite.collide_rect(left_paddle,ball):
        ball.rect.x += (left_paddle.rect.x+left_paddle.rect.width) - ball.rect.x
        ball.speed_x *= -1
    if pygame.sprite.collide_rect(right_paddle,ball):
        ball.rect.x -= (ball.rect.x+ball.rect.width)-right_paddle.rect.x
        ball.speed_x *= -1
    if ball.rect.y < 0:
        ball.rect.y -= ball.rect.y
        ball.speed_y *= -1
    if ball.rect.y > (height-ball.rect.height):
        ball.rect.y -= ball.rect.y - (height-ball.rect.height)
        ball.speed_y *= -1
    
    window.blit(score.render((str(left_score)+":"+str(right_score)),True,(255,255,255)),(width/2-30,20))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
    fps.tick(frame)