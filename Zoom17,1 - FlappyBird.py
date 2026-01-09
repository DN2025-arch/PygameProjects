import pygame
import random

pygame.init()

pipefrequency = 1500
last_pipe = pygame.time.get_ticks() - pipefrequency

swidth  = 864
sheight = 768

score = 0

screen = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption("Flappy Bird")

i_mbird  = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\FB-BirdMid.png")
i_ubird  = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\FB-BirdUp.png")
i_dbird  = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\FB-BirdDown.png")
i_ground = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\FB-Ground.png")
i_sky    = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\FB-Sky.png")
i_pipe   = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\FB-Pipe.png")
i_pabtn  = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\play again.png")

flying = False
gameover = False

class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,i,dir):
        super().__init__()
        self.image = i
        self.givenscore = False
        self.dir = dir
        if self.dir == "up":
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect = self.image.get_rect()
            self.rect.bottomleft = (x,y)
        else:
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
    def update(self):
        global gameover
        global score
        if gameover == False:
            self.rect.x -= 1
            if self.rect.x <= -80:
                self.kill()
            if self.rect.colliderect(bird.rect):
                gameover = True

            if self.rect.x <= 120 and self.givenscore == False and self.dir == "up":
                self.givenscore = True
                score += 1


class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y,i):
        super().__init__()
        self.velocity = 0
        self.image = i
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.clock1 = 0
    def move(self):
        if self.velocity < 0:
            self.image = i_ubird
        elif self.velocity < 1:
            self.image = i_mbird
        else:
            self.image = i_dbird
        
        if flying == True:
            self.rect.y += self.velocity
            if self.clock1 > 49:
                self.clock1 = 0
                self.velocity += 1
            else:
                self.clock1 += 1
        

bird_sprites = pygame.sprite.Group()

bird = Bird(80, sheight/2, i_mbird)
bird_sprites.add(bird)

pipe_sprites = pygame.sprite.Group()

playagainbtn = i_pabtn.get_rect(topleft=(swidth/2.5, sheight/3+80))


running = True
while running:
    screen.blit(i_sky, (0,0))
    pipe_sprites.draw(screen)
    screen.blit(i_ground, (0,600))

    scorefont = pygame.font.SysFont("arial", 40)
    birdscore = scorefont.render(f"SCORE: {score}", True, "black")
    screen.blit(birdscore, (swidth/2.5, 50))

    gameoverfont = pygame.font.SysFont("arial", 60)
    gameovertext = gameoverfont.render("GAME OVER", True, "black")

    bird_sprites.draw(screen)

    if pygame.time.get_ticks() - last_pipe >= pipefrequency and gameover == False and flying == True:
        pipe_distance = random.randint(50,250)
        top_pipe = Pipe(800,pipe_distance,i_pipe,"up")
        bottom_pipe = Pipe(800,pipe_distance+170,i_pipe,"bottom")  # 170
        pipe_sprites.add(bottom_pipe)
        pipe_sprites.add(top_pipe)
        last_pipe = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and gameover == False:
                flying = True
                bird.velocity = -2
        if event.type == pygame.MOUSEBUTTONDOWN:
            if playagainbtn.collidepoint(event.pos) and gameover == True:
                print("hi")
                bird.rect.y = sheight/2
                for sprite in pipe_sprites:
                    sprite.kill()
                flying = False
                gameover = False
        if event.type == pygame.QUIT:
            pygame.quit()
            

    if bird.rect.y >= 562:
        gameover = True

    if gameover == True:
        screen.blit(gameovertext, (swidth/3, sheight/3))
        bird.velocity = 0

        screen.blit(i_pabtn, (swidth/2.5, sheight/3+80))
##        if playagainbtn.collidepoint(pygame.mouse.get_pos()):
##            print("hi")
##            bird.y = sheight/2
##            flying = False
##            gameover = False
    
    bird.move()
    pipe_sprites.update()

    pygame.display.update()
    
