import pygame
import random

pygame.init()
score = 0
scale = 30
pixels = 20
Speed = 10

# Define the Dimentions of the Pygame Window
Width = scale * pixels
Height = scale * pixels

# Define Colors (R,G,B)
Backgroundcol = (0, 0, 0) #Background
Snakecol = (0, 255, 10) #Snake
Foodcol = (255 ,0 ,0) #Food

    
# Creating the Canvas / Window
Window = pygame.display.set_mode((Width, Height))
# Changing the Window heading
pygame.display.set_caption("Snake")
# creating the fps variable
Clock = pygame.time.Clock()




class Snake():
    def __init__(self,x,y,surface,Colour):
        self.x = x
        self.y = y
        self.surface = surface
        self.colour = Colour
    def Show(self):
        self.rect = pygame.Rect(self.x+1, self.y+1, scale -2, scale -2)
        pygame.draw.rect(self.surface, self.colour, self.rect, 0)

class Food():
    def __init__(self,surface,Colour):
        self.x = random.randint(1, int(pixels - 2)) * scale
        self.y = random.randint(1, int(pixels - 2)) * scale
        self.surface = surface
        self.colour = Colour
    def Show(self):
        self.rect = pygame.Rect(self.x + 2, self.y + 2, scale -4, scale -4)
        pygame.draw.rect(self.surface, self.colour, self.rect, 0)

def die():
    print('your size was:',Size)
    print("Game over")
    
    file = open("Scores.txt","r+")
    x,y,z = file.readline(),file.readline(),file.readline()
    scores = sorted([int(x),int(y),int(z),int(Size)])
    file.close()
    file = open("Scores.txt", "w")
    for j, i in enumerate(reversed(scores)):
        file.write((str(i)+"\n"))
        print(str(j+1)+": "+str(i),sep = "")
    file.close()
    pygame.quit()
    SystemExit()
    


XChange = 0
YChange = scale
Size = 0
X = 0
Y = 0
snake = []
eat = True
food = Food(Window,Foodcol)
eats = 2

Done = False
while not Done:

    # Event Handling Start
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = True
            die()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Paused = True
                while Paused:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            Done = True
                            Paused = False
                            die()
                            break
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                Paused = False
                    Clock.tick(30)
                    
            if event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()
                
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if XChange == scale:
                    pass
                else:
                    XChange = -scale
                    YChange = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if XChange == -scale:
                    pass
                else:
                    XChange = scale
                    YChange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if YChange == scale:
                    pass
                else:
                    XChange = 0
                    YChange = -scale
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if YChange == -scale:
                    pass
                else:
                    XChange = 0
                    YChange = scale

    # Event Handling End

    # Logic Start
    if eats == 0:
        eat = False
    else:
        eat = True


    X += XChange
    Y += YChange
    for i in snake:
        if (i.x == X) and (i.y == Y):
            die()
            break
    if 0 > X or X > Width-1 or 0 > Y or Y > Height-1:
        die()
        break
    snake.insert(0,(Snake(X,Y,Window,Snakecol)))
    if not(eat):
        snake.pop(len(snake)-1)

    if (food.x == X) and (food.y == Y):
        eats += 1
        food = Food(Window,Foodcol)
    if eat:
        Size += 1
        eats -= 1


    #Check if dead


    # Logic End

    # Reset Background
    Window.fill(Backgroundcol)

    # Update Display Start
    for i in snake:
        i.Show()
    food.Show()
    # Update Display End

    # Flip Display
    pygame.display.update()

    # seting the FPS
    Clock.tick(Speed+int(score)*4)


