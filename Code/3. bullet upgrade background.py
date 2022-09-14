import pygame, sys, random
from pygame.locals import *

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# set up the window
WINDOWWIDTH = 512
WINDOWHEIGHT = 512
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Input')

# set up the colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# set up the player and food data structure
BULLETSIZE = 30
SPEED = 50
player = pygame.Rect(300, 100, 50, 50)
playerImage = pygame.image.load('ezreal.png')
playerStretchedImage = pygame.transform.scale(playerImage, (50, 50))
bulletImage1 = pygame.image.load('qleft.png')
bulletStretchedImage1 = pygame.transform.scale(bulletImage1, (BULLETSIZE, BULLETSIZE))
bulletImage2 = pygame.image.load('qright.png')
bulletStretchedImage2 = pygame.transform.scale(bulletImage2, (BULLETSIZE, BULLETSIZE))
bulletImage3 = pygame.image.load('qdown.png')
bulletStretchedImage3 = pygame.transform.scale(bulletImage3, (BULLETSIZE, BULLETSIZE))
bulletImage4 = pygame.image.load('qup.png')
bulletStretchedImage4 = pygame.transform.scale(bulletImage4, (BULLETSIZE, BULLETSIZE))

down = []
up = []
right = []
left = []
direction = 'left'

backgroundImage = pygame.image.load('brickTile.jpg')

# set up movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6
BULLETSPEED = 5


# run the game loop
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == K_LEFT or event.key == ord('a'):
                moveRight = False
                moveLeft = True
                direction = 'left'
            if event.key == K_RIGHT or event.key == ord('d'):
                moveLeft = False
                moveRight = True
                direction = 'right'
            if event.key == K_UP or event.key == ord('w'):
                moveDown = False
                moveUp = True
                direction = 'up'
            if event.key == K_DOWN or event.key == ord('s'):
                moveUp = False
                moveDown = True
                direction = 'down'                
            if event.key == ord(' '):
                if direction == 'left':
                    left.append(pygame.Rect(player.left-BULLETSIZE, player.centery-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
                if direction == 'right':
                    right.append(pygame.Rect(player.right, player.centery-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
                if direction == 'up':
                    up.append(pygame.Rect(player.centerx-(BULLETSIZE/2), player.top-BULLETSIZE, BULLETSIZE, BULLETSIZE))
                if direction == 'down':
                    down.append(pygame.Rect(player.centerx-(BULLETSIZE/2), player.bottom, BULLETSIZE, BULLETSIZE))
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False
            if event.key == ord('x'):
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)

    # draw the black background onto the surface
    windowSurface.blit(backgroundImage, (0,0))

    for i in range(len(down)):
        down[i].bottom += BULLETSPEED
    for i in range(len(up)):
        up[i].top -= BULLETSPEED
    for i in range(len(left)):
        left[i].left -= BULLETSPEED
    for i in range(len(right)):
        right[i].right += BULLETSPEED
    
    # move the player
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED
    
    # draw the player onto the surface
    windowSurface.blit(playerStretchedImage, player)

    # draw the food
    for i in range(len(down)):
        windowSurface.blit(bulletStretchedImage3, down[i])
    for i in range(len(up)):
        windowSurface.blit(bulletStretchedImage4, up[i])
    for i in range(len(left)):
        windowSurface.blit(bulletStretchedImage1, left[i])
    for i in range(len(right)):
        windowSurface.blit(bulletStretchedImage2, right[i])

    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(SPEED)
