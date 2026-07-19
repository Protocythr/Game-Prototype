#HECEnge and wen

import pygame
import random

pygame.init()

# intialize the screen with a width and height of 640 pixels
screen = pygame.display.set_mode((640,640))
clock = pygame.time.Clock()
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
        self.experience = 0
        self.next_level_experience = 100
        self.stat_rolls = 1 # how many dice rolls player has that they recieve for level up

    def level_up(self):
        if self.experience >= self.next_level_experience:
            self.experience -= self.next_level_experience
            self.next_level_experience *= 1.5
            self.stat_rolls += 2

    def roll_stat(self, stat):
        if self.stat_rolls > 0:
            roll = random.randint(1, 6)
            if stat == "health":
                self.health += roll
            elif stat == "str":
                self.str += roll
            elif stat == "vit":
                self.vit += roll
            elif stat == "int":
                self.int += roll
            elif stat == "luck":
                self.luck += roll
            self.stat_rolls -= 1

class Vanguard(Player):
    def __init__():
        super().__init__()
        self.health = 20 + random.randint(0, 12)
        self.str = 5 + random.randint(0, 5)
        self.vit = 3 + random.randint(0, 3)
        self.int = 2 + random.randint(0, 2)
        self.luck = 0 + random.randint(-5, 5)

    def calculate_critical_hit_multiplier(self):
        chance = (self.luck * 0.01) * 0.05
        overflow = int(chance/1) + 1
        remaining_chance = chance % 1
        return overflow + 1 if remaining_chance >= random.random() else overflow

    def attack(self):
        growth_rate = 1.035
        base_damage = 5
        return base_damage * (growth_rate ** self.str) * self.calculate_critical_hit_multiplier()

class Tank(Player):
    def __init__():
        super().__init__()
        self.health = 30 + random.randint(0, 12)
        self.str = 3 + random.randint(0, 2)
        self.vit = 5 + random.randint(0, 5)
        self.int = 2 + random.randint(0, 2)
        self.luck = 0 + random.randint(-6, 6)
    
    def calculate_critical_hit_multiplier(self):
        chance = (self.luck * 0.01) * 0.05
        overflow = int(chance/1) + 1
        remaining_chance = chance % 1
        return overflow + 1 if remaining_chance >= random.random() else overflow

    def attack(self):
        growth_rate = 1.0175
        base_damage = 3
        return base_damage * (growth_rate ** self.str) * self.calculate_critical_hit_multiplier()

class Support(Player):
    def __init__():
        super().__init__()
        self.health = 15 + random.randint(0, 12)
        self.str = 3 + random.randint(0, 3)
        self.vit = 2 + random.randint(0, 2)
        self.int = 5 + random.randint(0, 5)
        self.luck = 0 + random.randint(-6, 6)

    def calculate_critical_hit_multiplier(self):
        chance = (self.luck * 0.01) * 0.05
        overflow = int(chance/1) + 1
        remaining_chance = chance % 1
        return overflow + 1 if remaining_chance >= random.random() else overflow

    def attack(self):
        growth_rate = 1.035
        base_damage = 5
        return base_damage * (growth_rate ** self.int) * self.calculate_critical_hit_multiplier()

# game loop
while running:
    screen.fill((255, 255, 255)) # Fill the screen with white color
    
    # checking if someone clicked the close button on the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60) # Limit the frame rate to 60 frames per second
    pygame.display.flip() # Update the display/ basically displays the changes made to the screen

pygame.quit()