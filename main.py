# DO NOT UPDATE PYGAME (current ver. 20.2.3)
import pygame

# Initialize the pygame
pygame.init()
# Create the screen
screen = pygame.display.set_mode((800,600))

# Title and Icon Setting
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
# Game Loop
running = True
while running:
    for event in pygame.event.get():
        # when click close button
        if event.type == pygame.QUIT:
            running = False