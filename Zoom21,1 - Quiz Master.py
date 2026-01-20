import pygame

pygame.init()

file_path = r"C:\Users\flori\OneDrive\Desktop\Python\questions.txt"

questions = []
question = []

file = open(file_path, "r")
content = file.read()

questions = content.split("\n")
question = questions[0].split(",")



file.close()
#print(content)


swidth  = 700
sheight = 700

screen = pygame.display.set_mode((swidth,sheight))
pygame.display.set_caption("QUIZ MASTER")

def text_wrap(given_question, maxwidth, font):
    test = ""
    lines = []
    words = given_question.split(" ")
    for word in words:
        testline = test + word + " "
        if font.size(testline)[0] <= maxwidth:
            test = testline
        else:
            lines.append(test)
            test = word 
    return "\n".join(lines)


class qB():
    def __init__(self,x,y,l,w,c, t):
        #self.image = pygame.Surface((l, w))
        #self.rect = self.image.get_rect()
        self.w = w
        self.rect = pygame.Rect(x,y,l,w)
        self.colour = c
        self.tstr = t
        self.font = pygame.font.SysFont("arial", 30)
        self.tstr = text_wrap(self.tstr, self.w, self.font)
    def draw_rect(self):
        pygame.draw.rect(screen, self.colour, self.rect)

        self.text = self.font.render(self.tstr, True, "white")
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center
        screen.blit(self.text, (self.rect.x,self.rect.y))
        


title    = qB(0,0,swidth,75, "darkgray", "QUIZ MASTER")
qbox     = qB(50,100, 450, 140, "darkblue", f"{question[0]}")
marksbox = qB(530,100, 140, 140, "darkblue", "0")
aboxes = []
ab1 = qB(50,300, 200, 140, "orange", f"{question[1]}")
ab2 = qB(300,300, 200, 140, "orange", f"{question[2]}")
ab3 = qB(50,500, 200, 140, "orange", f"{question[3]}")
ab4 = qB(300,500, 200, 140, "orange", f"{question[4]}")
aboxes.append(ab1)
aboxes.append(ab2)
aboxes.append(ab3)
aboxes.append(ab4)
sBtn= qB(530,300, 140, 340, "darkgreen", "SKIP")


running = True
while running:

    title.draw_rect()
    qbox.draw_rect()
    marksbox.draw_rect()
    for i in aboxes:
        i.draw_rect()
    sBtn.draw_rect()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
