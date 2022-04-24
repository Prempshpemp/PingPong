from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, widht, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (widht, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def  reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_presed = key.get_pressed()
        if keys_presed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_presed[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
            
    def update_r(self):
        keys_presed = key.get_pressed()
        if keys_presed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_presed[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

win_widht = 600
win_height = 500
back = [120, 219, 226]

window = display.set_mode((win_widht, win_height))
window.fill(back)

finish = False
game = True
clock = time.Clock()
FPS = 60

racket1 = Player('pngegg.png', 30, 200,4, 50, 50)
racket2 = Player('pngegg (1).png', 520, 200,4, 50, 50)
ball = GameSprite('pngwing.com.png', 200, 200, 4, 50, 50)

speed_x = 3
speed_y = 3

font.init()
font = font.Font(None, 40)
lose1 = font.render('Player 1 LOSE!', True, (255, 0, 0))
lose2 = font.render('Player 2 LOSE!', True, (255, 0, 0))


while game:
    for e in event.get():
        if e. type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height - 55 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > win_widht:
            finish = True
            window.blit(lose2, (200, 200))

        racket1.reset()
        racket2.reset()
        ball.reset()
   
    display.update()
    clock.tick(FPS)
    
