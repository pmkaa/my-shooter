from pygame import *

font.init()
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
font = font.Font(None, 70)
win = font.render('VICTORY!', True, (255, 215, 0))
lose = font.render('LLOSE!', False, (255, 215, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy (GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x,
    wall_y, wall_wight, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wight = wall_wight
        self.height = wall_height
        self.image = Surface((self.wight, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

hero = Player('hero.png', 100, 100, 5)
monster = Enemy('cyborg.png', 350, 100, 5)
wall1 = Wall(89, 126, 123, 250, 150, 10, 200)
wall2 = Wall(89, 126, 123, 250, 350, 10, 200)
wall3 = Wall(89, 126, 123, 250, 350, 200, 10)
final = GameSprite('treasure.png', 200, 200, 0)

clock = time.Clock()
FPS = 60


game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
    
        window.blit(background,(0, 0))
        hero.update()
        monster.update()
        hero.reset()        
        monster.reset()
        final.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
    if sprite.collide_rect(hero, final):
        window.blit(win, (200, 200))
        finish = True
    if sprite.collide_rect(hero, monster) or sprite.collide_rect(hero, wall1) or sprite.collide_rect(hero, wall2):
        window.blit(lose, (200, 200))
        finish = True
    display.update()
    clock.tick(FPS)
