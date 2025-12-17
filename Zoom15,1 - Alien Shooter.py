import pygame
import pygame.draw
import random

pygame.init()  # sometimes pygame needs to be initialised.

class Bullet():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect((self.x, self.y, self.w, self.h))

    def draw(self):
        pygame.draw.rect(screen, "red", self.rect)  # self.rect stores the variables for making rectangle
        

score = 0

width = 400
height = 400
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Alien Shooter")

ship = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\SpaceShip.png")
ship = pygame.transform.scale(ship, (30,30))
alien = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\Alien1.png")
#bullet_image = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\SpaceShip-Bullet.png")
stars = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\Stars.png")

px = (width/2) - 15
py = (height/2)*1.8

def reset_alien():
    alien_rect.x = random.uniform(width*0.1, width*0.9)
    alien_rect.y = 0

alien_rect   = alien.get_rect()  # Get rectangle of image for collision.
reset_alien()

counter = 0
counterlimit = 15
def alien_move():
    global counter
    global counterlimit
    global score
    counter += 1
    if score != 0:
        if score % 5000 == 0:
            score += 500
            counterlimit -= random.randint(1,3)
            if counterlimit <=3:
                counterlimit = 3

            print(f"inc: {counterlimit}")
    if counter > counterlimit:
        alien_rect.y += 1
        if alien_rect.y >= height:
            reset_alien()
        counter = 0

speed = 30

bullets = []

while True:
    
    screen.blit(stars, (0,0))
    screen.blit(ship, (px, py))
    screen.blit(alien, (alien_rect.x, alien_rect.y))

    font = pygame.font.SysFont("arial", 22)
    
    text = font.render(f"{score}", True, "white")

    screen.blit(text, (10, 10))
    
    alien_move()

    for bullet in bullets:
        bullet.draw()
        bullet.rect.y -= 1

        if bullet.rect.colliderect(alien_rect):
            reset_alien()
            score += 500
            bullets.remove(bullet)

        elif bullet.rect.y <= 0:
            bullets.remove(bullet)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                px -= speed
            if event.key == pygame.K_d:
                px += speed
            if event.key == pygame.K_w:
                bullet = Bullet(px+15, py, 5, 10)
                bullets.append(bullet)
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
