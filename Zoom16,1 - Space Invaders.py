import pygame

pygame.init()

width = 1000
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Invaders")


# Images
i_redship = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\RedShip.png")
i_yellowship = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\YellowShip.png")
i_stars = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\MoreStars.png")

i_stars = pygame.transform.scale(i_stars, (width, height))

class Ship(pygame.sprite.Sprite):  # Inheriting from Sprite Class
    def __init__(self, x, y, i, angle):
        super().__init__()
        self.image = pygame.transform.scale(i, (60, 50))
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def move(self,direction, quantity):
        if direction == "x":
            self.rect.x += quantity
        if direction == "y":
            self.rect.y += quantity
        



ship_sprites = pygame.sprite.Group()

yellow = Ship(400, 250, i_yellowship, 90)
red = Ship(600, 250, i_redship, 270)

ship_sprites.add(yellow)
ship_sprites.add(red)

r_hp = 100
y_hp = 100

speed = 1

y_bullets = []
r_bullets = []

winner = ""

running = True
while running:

    screen.blit(i_stars, (0,0))
    pygame.draw.line(screen, "black", (width/2,0), (width/2,height), 12)

    font = pygame.font.SysFont("arial", 22)
    y_hp_text = font.render(f"{y_hp}", True, "yellow")
    r_hp_text = font.render(f"{r_hp}", True, "red")
    

    screen.blit(y_hp_text, (10, 10))
    screen.blit(r_hp_text, (width/2+10, 10))
    
    ship_sprites.draw(screen)

    for bullet in y_bullets:
        pygame.draw.rect(screen, "yellow", bullet)
        bullet.x += 1

        if bullet.colliderect(red.rect):
            r_hp -= 5
            y_bullets.remove(bullet)
        
        if bullet.x > width:
            y_bullets.remove(bullet)

    if r_hp <= 0:
        if winner == "":
            winner = "yellow"
            y_win_text = font.render("YELLOW WINS", True, "yellow")
            screen.blit(y_win_text, (10,40))

            pygame.display.update()
            pygame.time.delay(3000)
            pygame.quit()
    
    for bullet in r_bullets:
        pygame.draw.rect(screen, "red", bullet)
        bullet.x -= 1

        if bullet.colliderect(yellow.rect):
            y_hp -= 5
            r_bullets.remove(bullet)

        if bullet.x < 0:
            r_bullets.remove(bullet)

    if y_hp <= 0:
        if winner == "":
            winner = "red"
            r_win_text = font.render("RED WINS", True, "red")
            screen.blit(r_win_text, (width/2+10,40))

            pygame.display.update()
            pygame.time.delay(3000)
            pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                y_bullet = pygame.Rect(yellow.rect.x+10, yellow.rect.y+30, 20, 10)
                y_bullets.append(y_bullet)
            if event.key == pygame.K_RCTRL:
                r_bullet = pygame.Rect(red.rect.x+10, red.rect.y+30, 20, 10)
                r_bullets.append(r_bullet)
        
        if event.type == pygame.QUIT:
           pygame.quit()
    keys_pressed = pygame.key.get_pressed()
    
    if keys_pressed[pygame.K_LEFT]:
        red.move("x", -speed)
    if keys_pressed[pygame.K_RIGHT]:
        red.move("x", speed)
    if keys_pressed[pygame.K_UP]:
        red.move("y", -speed)
    if keys_pressed[pygame.K_DOWN]:
        red.move("y", speed)
        
    if keys_pressed[pygame.K_a]:
        yellow.move("x", -speed)
    if keys_pressed[pygame.K_d]:
        yellow.move("x", speed)
    if keys_pressed[pygame.K_w]:
        yellow.move("y", -speed)
    if keys_pressed[pygame.K_s]:
        yellow.move("y", speed)


    if yellow.rect.right >= width/2:
        yellow.rect.x -= speed
    if yellow.rect.left <= 0:
        yellow.rect.x += speed
        
    if yellow.rect.bottom >= height:
        yellow.rect.y -= speed
    if yellow.rect.top <= 0:
        yellow.rect.y += speed


    if red.rect.left <= width/2:
        red.rect.x += speed
    if red.rect.right >= width:
        red.rect.x -= speed
        
    if red.rect.bottom >= height:
        red.rect.y -= speed
    if red.rect.top <= 0:
        red.rect.y += speed

    pygame.display.update()
