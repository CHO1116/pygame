# DO NOT UPDATE PYGAME (current ver. 20.2.3)
import pygame
import math
from random import *
from tkinter import messagebox

from pygame.constants import QUIT

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
enemyImg = []
enemyX = []
enemyY = []
enemyY_move = []
num_of_enemies = 2
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(randint(0, 736))
    enemyY.append(0)
    enemyY_move.append(random() * 0.25)

# Bullet
# Ready - can't see bullet on the screen
# Fire - bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_move = 0
bulletY_move = 0.6
bullet_state = "ready"
score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy_appear(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(X1, Y1, X2, Y2):
    distance = math.sqrt((X1 - X2) ** 2 + (Y1 - Y2) ** 2)
    if distance < 27:
        return True
    else:
        return False

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
                playerX_move = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_move = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
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
    for i in range(num_of_enemies):
        enemyY[i] += enemyY_move[i]        
        if enemyY[i] >= 500:
            enemyX[i] = randint(0, 736)
            enemyY[i] = 0

    # Movement Range Setting About Bullet
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_move

    for i in range(num_of_enemies):
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score = str(int(score) + 100)
            print(score)
            enemyX[i] = randint(0, 736)
            enemyY[i] = 0
        enemy_appear(enemyX[i], enemyY[i], i)
    for i in range(num_of_enemies):
        fin_collision = isCollision(enemyX[i], enemyY[i], playerX, playerY)
        if fin_collision:
            messagebox.showinfo("Game Over!", "Your Score is " + score)

    player(playerX, playerY)
    pygame.display.update()