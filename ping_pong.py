from pygame import *


window = display.set_mode((700, 500))
clock = time.Clock()
display.set_caption('Пинг Понг')
game = True
font.init()
finish = False
lose1 = font.SysFont('Arial', 50)
lose2 = font.SysFont('Arial', 50)
class GameSprite(sprite.Sprite):
    def __init__(self, x, y, image_player, speed, size):
        self.image = transform.scale(image.load(image_player), size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.size = size
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

player1 = Player1(50, 250, 'image.png', 7, (20, 100))
player2 = Player2(630, 250, 'image.png', 7, (20, 100))
ball = GameSprite(350, 250, 'ball.png', 0, (60, 60))
speed_x = 5
speed_y = 5
while game:
    window.fill((255, 255, 255))
    ball.reset()
    player1.reset()
    player1.update()
    player2.reset()
    player2.update()
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        lose_txt = lose1.render('Игрок 1 проиграл!', True, (255, 0, 0))
        window.blit(lose_txt, (150, 200))
    if ball.rect.x > 640:
        finish = True
        lose_txt = lose2.render('Игрок 2 проиграл!', True, (255, 0, 0))
        window.blit(lose_txt, (150, 200))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)