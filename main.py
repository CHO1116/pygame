# DO NOT UPDATE PYGAME (current ver. 20.2.3)
import pygame
from random import *

# Initialize the pygame
pygame.init()

# Create the Screen
screen = pygame.display.set_mode((800,600))

# Background Setting
background = pygame.image.load('background.jpg')

# Caption and Icon Setting
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 500
playerX_move = 0

# Enemy
# Alive - Enemy is on screen
# Dead - Time to generate new enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = randint(0, 736)
enemyY = 0
enemyY_move = random() * 0.25
enemy_state = "dead"

# Bullet
# Ready - can't see bullet on the screen
# Fire - bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_move = 0
bulletY_move = 0.4
bullet_state = "ready"

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy_appear(x, y):
    global enemy_state
    enemy_state = "alive"
    screen.blit(enemyImg, (x, y))

def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# Game Loop
running = True
while running:
    # Setting Background No.1
    # RGB Setting - Red Green Blue
    # screen.fill((80, 0, 80))
    
    # Setting Background No.2
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        # Command when quit button is clicked
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether its right or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_move = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_move = 0.2
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    bullet_fire(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_move = 0
    
    # Movement Range Setting About Player
    playerX += playerX_move
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Movement Range Setting About Enemy
    if enemyY >= 500:
        enemyX = randint(0, 736)
        enemyY = 0
        enemy_state = "dead"
        
    if enemy_state is "alive":
        enemy_appear(enemyX, enemyY)
        enemyY += enemyY_move

    # Movement Range Setting About Bullet
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_move

    player(playerX, playerY)
    enemy_appear(enemyX, enemyY)
    pygame.display.update()