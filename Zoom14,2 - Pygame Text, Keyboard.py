import pygame

#print("294\\536")
#print(r"294\536")



title  = "My Project"
width  = 400
height = 400

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(title)

rocket = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\Image20251216164244.png")
rocket = pygame.transform.scale(rocket, (50, 65))
stars  = pygame.image.load(r"C:\Users\flori\OneDrive\Desktop\Python\Zoom Images\Image20251216164251.png")

rocket_x = 0
rocket_y = 0
speed = 10

running = True
while running:

    screen.blit(stars,  (0,0))
    screen.blit(rocket, (rocket_x, rocket_y))
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                rocket_x += speed
            if event.key == pygame.K_a:
                rocket_x -= speed
            if event.key == pygame.K_s:
                rocket_y += speed
            if event.key == pygame.K_w:
                rocket_y -= speed
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    pygame.display.update()


