import pygame
import time
import random

pygame.init()

swidth = 1000
sheight = 800

screen = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption("Recycle Marathon")

starting_time = time.time()
total_time = 0
time_left = 5

score = 0

i_bin  = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\RM-Bin.png")
i_back = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\RM-Background.png")
i_bag  = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\RM-Bag.png")
i_box  = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\RM-Box.png")
i_paper= pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\RM-Paperbag.png")
i_pen  = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\RM-Pencil.png")

i_bin = pygame.transform.scale(i_bin, (37,49))
i_back = pygame.transform.scale(i_back, (swidth, sheight))
i_paper = pygame.transform.scale(i_paper, (40, 50))
i_bag = pygame.transform.scale(i_bag, (65, 65))

recyc_i = [i_bag, i_bag, i_paper]
unrecyc_i = [i_pen, i_box]

class Bin(pygame.sprite.Sprite):
    def __init__(self,x,y,i):
        super().__init__()
        self.image = i
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.clock1 = 0
    def move(self, quantity, direction):
        if int(round(time_left, 0)) > 0:
            self.clock1 += 1
            if self.clock1 >= 3:
                self.clock1 = 0
                if direction == "x":
                    self.rect.x += quantity
                else:
                    self.rect.y += quantity

class Unrecycable(pygame.sprite.Sprite):
    def __init__(self,x,y,i):
        super().__init__()
        self.image = i
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Recycable(pygame.sprite.Sprite):
    def __init__(self,x,y,i):
        super().__init__()
        self.image = i
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


player_sprites = pygame.sprite.Group()
player = Bin(0,0, i_bin)
player_sprites.add(player)

recycable_sprites = pygame.sprite.Group()
for i in range(1,30):
    ima = random.choice(recyc_i)
    recyc = Recycable(random.randint(50, swidth-50),random.randint(50,sheight-50), ima)
    recycable_sprites.add(recyc)

unrecycable_sprites = pygame.sprite.Group()
for i in range(1,30):
    ima = random.choice(unrecyc_i)
    unrecyc = Unrecycable(random.randint(50, swidth-50),random.randint(50,sheight-50), ima)
    unrecycable_sprites.add(unrecyc)

running = True
while running:

    total_time = time.time() - starting_time
    time_left = 60 - total_time
    time_left = int(round(time_left, 0))
    

    screen.blit(i_back, (0,0))

    unrecycable_sprites.draw(screen)
    recycable_sprites.draw(screen)
    player_sprites.draw(screen)

    font = pygame.font.SysFont("arial", 40)
    scoretext = font.render(f"SCORE: {score}", True, "black")
    if time_left <= 0:
        timetext = font.render(f"GAME OVER", True, "black")
    else:
        timetext = font.render(f"TIME: {time_left}", True, "black")
    screen.blit(scoretext, (0,0))
    screen.blit(timetext, (0,60))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_s]:
        player.move(1,"y")
        if player.rect.y > sheight-49:
            player.move(-1, "y")
    if keys_pressed[pygame.K_w]:
        player.move(-1,"y")
        if player.rect.y < 0:
            player.move(1, "y")
    if keys_pressed[pygame.K_d]:
        player.move(1,"x")
        if player.rect.x > swidth-37:
            player.move(-1, "x")
    if keys_pressed[pygame.K_a]:
        player.move(-1,"x")
        if player.rect.x < 0:
            player.move(1, "x")

##    for i in recycable_sprites:
##        if player.rect.colliderect(i):
##            i.kill()
##            score += 1
##    for i in unrecycable_sprites:
##        if player.rect.colliderect(i):
##            i.kill()
##            score -= 1

    if pygame.sprite.groupcollide(recycable_sprites, player_sprites, True, False): # Group1, Group2, Kill G1 Sprt, Kill G2 Sprt
        score += 1
    if pygame.sprite.groupcollide(unrecycable_sprites, player_sprites, True, False):
        score -= 1

    if time_left <= -5:
        pygame.quit()

    pygame.display.update()
