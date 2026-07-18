import pygame
import random

pygame.init()

# intialize the screen with a width and height of 640 pixels
screen = pygame.display.set_mode((640,640))

running = True

# this create the base player class with the basic stats that the player will have
# do not edit this class to create a subclass
class Player:
    def __init__():
        self.health = 0
        self.str = 0
        self.vit = 0
        self.int = 0
        self.luck = 0

class Vanguard(Player):
    def __init__():
        super().__init__()
        self.health = 20 + random.randint(0, 12)
        self.str = 5 + random.randint(0, 5)
        self.vit = 3 + random.randint(0, 3)
        self.int = 2 + random.randint(0, 2)
        self.luck = 0 + random.randint(-6, 6)

class Tank(Player):
    def __init__():
        super().__init__()
        self.health = 30 + random.randint(0, 12)
        self.str = 3 + random.randint(0, 2)
        self.vit = 5 + random.randint(0, 5)
        self.int = 2 + random.randint(0, 2)
        self.luck = 0 + random.randint(-6, 6)

class Support(Player):
    def __init__():
        super().__init__()
        self.health = 15 + random.randint(0, 12)
        self.str = 3 + random.randint(0, 3)
        self.vit = 2 + random.randint(0, 2)
        self.int = 5 + random.randint(0, 5)
        self.luck = 0 + random.randint(-6, 6)

# game loop
while running:
    screen.fill((255, 255, 255)) # Fill the screen with white color
    
    # checking if someone clicked the close button on the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip() # Update the display/ basically displays the changes made to the screen

pygame.quit()