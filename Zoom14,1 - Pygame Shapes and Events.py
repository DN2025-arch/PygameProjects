import pygame
pygame.init()

class Circle():
    def __init__(self, r, x, y, c, t):
        self.radius = r
        self.px = x
        self.py = y
        self.color = c
        self.thickness = t  # If thickness is passed, shape is an outline.

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.px, self.py), self.radius, self.thickness)

    

title = "Pygame Title"
width = 400
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)

rock = Circle(width/2, width/2, width/2, "red", 6)
ball = Circle(0, 0, 0, "white", 0)

run = True
while run==True:
    screen.fill("white")

    rock.draw()
    
    for event in pygame.event.get():  # pygame.event is a sub-module
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
##        if event.type == pygame.MOUSEBUTTONDOWN:
##            position = pygame.mouse.get_pos()
##            ball = Circle(40, position[0], position[1], "green", 7)
        if event.type == pygame.MOUSEMOTION:
            position = pygame.mouse.get_pos()
            ball = Circle(40, position[0], position[1], "green", 7)

    ball.draw()
    
    pygame.display.update()


