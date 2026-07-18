import pygame

pygame.init()

# intialize the screen with a width and height of 640 pixels
screen = pygame.display.set_mode((640,640))

running = True

# game loop
while running:
    screen.fill((255, 255, 255)) # Fill the screen with white color
    
    # checking if someone clicked the close button on the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip() # Update the display/ basically displays the changes made to the screen

pygame.quit()