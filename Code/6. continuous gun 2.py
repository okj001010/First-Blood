import pygame, sys, random
from pygame.locals import *

# pygame set up
pygame.init()
mainClock = pygame.time.Clock()

# window set up
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Input')

# 색 정리
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# set up the player and food data structure
BULLETSIZE = 30
SPEED = 50
player1 = pygame.Rect(200, 100, 50, 50)
playerImage1 = pygame.image.load('ezreal.png')
playerStretchedImage1 = pygame.transform.scale(playerImage1, (50, 50))
bulletImage11 = pygame.image.load('qleft.png')
bulletStretchedImage11 = pygame.transform.scale(bulletImage11, (BULLETSIZE, BULLETSIZE))
bulletImage12 = pygame.image.load('qright.png')
bulletStretchedImage12 = pygame.transform.scale(bulletImage12, (BULLETSIZE, BULLETSIZE))
bulletImage13 = pygame.image.load('qdown.png')
bulletStretchedImage13 = pygame.transform.scale(bulletImage13, (BULLETSIZE, BULLETSIZE))
bulletImage14 = pygame.image.load('qup.png')
bulletStretchedImage14 = pygame.transform.scale(bulletImage14, (BULLETSIZE, BULLETSIZE))
player2 = pygame.Rect(400, 100, 50, 50)
playerImage2 = pygame.image.load('ezreal.png')
playerStretchedImage2 = pygame.transform.scale(playerImage2, (50, 50))
bulletImage21 = pygame.image.load('qleft.png')
bulletStretchedImage21 = pygame.transform.scale(bulletImage21, (BULLETSIZE, BULLETSIZE))
bulletImage22 = pygame.image.load('qright.png')
bulletStretchedImage22 = pygame.transform.scale(bulletImage22, (BULLETSIZE, BULLETSIZE))
bulletImage23 = pygame.image.load('qdown.png')
bulletStretchedImage23 = pygame.transform.scale(bulletImage23, (BULLETSIZE, BULLETSIZE))
bulletImage24 = pygame.image.load('qup.png')
bulletStretchedImage24 = pygame.transform.scale(bulletImage24, (BULLETSIZE, BULLETSIZE))

down1 = []
up1 = []
right1 = []
left1 = []
direction1 = 'right'
down2 = []
up2 = []
right2 = []
left2 = []
direction2 = 'left'
backgroundImage = pygame.image.load('brickTile.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))

# set up movement variables
moveLeft1 = False
moveRight1 = False
moveUp1 = False
moveDown1 = False
moveLeft2 = False
moveRight2 = False
moveUp2 = False
moveDown2 = False
fireGun1 = False
fireGun2 = False

MOVESPEED = 6
BULLETSPEED = 5
BULLETGAP = 15
BULLETINTERVAL1 = BULLETGAP-1
BULLETINTERVAL2 = BULLETGAP-1
FIREBUGINTERVAL = BULLETGAP
FIREBUG1 = FIREBUGINTERVAL
FIREBUG2 = FIREBUGINTERVAL
FIREBUGTRUE1 = False
FIREBUGTRUE2 = False

# run the game loop
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == ord('a'):
                moveRight1 = False
                moveLeft1 = True
                direction1 = 'left'
                FIREBUGTRUE1 = False
                FIREBUGTRUE2 = False
                FIREBUG1 = FIREBUGINTERVAL
                FIREBUG2 = FIREBUGINTERVAL
            if event.key == K_LEFT:
                moveRight2 = False
                moveLeft2 = True
                direction2 = 'left'
                FIREBUGTRUE1 = False
                FIREBUGTRUE2 = False
                FIREBUG1 = FIREBUGINTERVAL
                FIREBUG2 = FIREBUGINTERVAL
            if event.key == ord('d'):
                moveLeft1 = False
                moveRight1 = True
                direction1 = 'right'
                FIREBUGTRUE1 = False
                FIREBUGTRUE2 = False
                FIREBUG1 = FIREBUGINTERVAL
                FIREBUG2 = FIREBUGINTERVAL
            if event.key == K_RIGHT:
                moveLeft2 = False
                moveRight2 = True
                direction2 = 'right'
                FIREBUGTRUE1 = False
                FIREBUGTRUE2 = False
                FIREBUG1 = FIREBUGINTERVAL
                FIREBUG2 = FIREBUGINTERVAL
            if event.key == ord('w'):
                moveDown1 = False
                moveUp1 = True
                direction1 = 'up'
                FIREBUGTRUE1 = False
                FIREBUGTRUE2 = False
                FIREBUG1 = FIREBUGINTERVAL
                FIREBUG2 = FIREBUGINTERVAL
            if event.key == K_UP :
                moveDown2 = False
                moveUp2 = True
                direction2 = 'up'
                FIREBUGTRUE1 = False
                FIREBUGTRUE2 = False
                FIREBUG1 = FIREBUGINTERVAL
                FIREBUG2 = FIREBUGINTERVAL
            if event.key == ord('s'):
                moveUp1 = False
                moveDown1 = True
                direction1 = 'down'
                FIREBUGTRUE1 = False
                FIREBUGTRUE2 = False
                FIREBUG1 = FIREBUGINTERVAL
                FIREBUG2 = FIREBUGINTERVAL
            if event.key == K_DOWN :
                moveUp2 = False
                moveDown2 = True
                direction2 = 'down'
                FIREBUGTRUE1 = False
                FIREBUGTRUE2 = False
                FIREBUG1 = FIREBUGINTERVAL
                FIREBUG2 = FIREBUGINTERVAL
            if event.key == ord(' ') and FIREBUG1 >= FIREBUGINTERVAL:
                fireGun1 = True
                FIREBUG1 = 0
                FIREBUGTRUE1 = True
                FIREBUGTRUE2 = False
            if event.key == ord('/') and FIREBUG2 >= FIREBUGINTERVAL:
                fireGun2 = True
                FIREBUG2 = 0
                FIREBUGTRUE2 = True
                FIREBUGTRUE1 = False
                
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == ord('a'):
                moveLeft1 = False
            if event.key == K_LEFT :
                moveLeft2 = False
            if event.key == ord('d'):
                moveRight1 = False
            if event.key == K_RIGHT:
                moveRight2 = False
            if event.key == ord('w'):
                moveUp1 = False
            if event.key == K_UP : 
                moveUp2 = False
            if event.key == ord('s'):
                moveDown1 = False
            if event.key == K_DOWN : 
                moveDown2 = False
            if event.key == ord(' '):
                fireGun1 = False
                BULLETINTERVAL1 = BULLETGAP-1
            if event.key == ord('/'):
                fireGun2 = False
                BULLETINTERVAL2 = BULLETGAP-1
            if event.key == ord('q'):
                player1.top = random.randint(0, WINDOWHEIGHT - player1.height)
                player1.left = random.randint(0, WINDOWWIDTH - player1.width)
            if event.key == ord('l'):
                player2.top = random.randint(0, WINDOWHEIGHT - player2.height)
                player2.left = random.randint(0, WINDOWWIDTH - player2.width)

    if FIREBUGTRUE1 and FIREBUG1 < FIREBUGINTERVAL+10:
        FIREBUG1 +=1
    if FIREBUGTRUE2 and FIREBUG2 < FIREBUGINTERVAL+10:
        FIREBUG2 +=1

    # draw the black background onto the surface
    windowSurface.blit(backgroundStretchedImage, (0,0))
    if len(down1) > 0:
        if down1[0].bottom > WINDOWHEIGHT:
            down1.remove(down1[0])
    for i in range(len(down1)):
        down1[i].bottom += BULLETSPEED    
    if len(up1) > 0:
        if up1[0].top < 0:
            up1.remove(up1[0])
    for i in range(len(up1)):
        up1[i].top -= BULLETSPEED
    if len(left1) > 0:
        if left1[0].left < 0:
            left1.remove(left1[0])
    for i in range(len(left1)):
        left1[i].left -= BULLETSPEED
    if len(right1) > 0:
        if right1[0].left > WINDOWWIDTH:
            right1.remove(right1[0])
    for i in range(len(right1)):
        right1[i].right += BULLETSPEED
    if len(down2) > 0:
        if down2[0].bottom > WINDOWHEIGHT:
            down2.remove(down2[0])
    for i in range(len(down2)):
        down2[i].bottom += BULLETSPEED
    if len(up2) > 0:
        if up2[0].top < 0:
            up2.remove(up2[0])
    for i in range(len(up2)):
        up2[i].top -= BULLETSPEED
    if len(left2) > 0:
        if left2[0].left < 0:
            left2.remove(left2[0])
    for i in range(len(left2)):
        left2[i].left -= BULLETSPEED 
    if len(right2) > 0:
        if right2[0].left > WINDOWWIDTH:
            right2.remove(right2[0])
    for i in range(len(right2)):
        right2[i].right += BULLETSPEED

    if(fireGun1):
        BULLETINTERVAL1 += 1
    if(fireGun2):
        BULLETINTERVAL2 += 1

    # fire gun
    if fireGun1 and BULLETINTERVAL1 == BULLETGAP:
        if direction1 == 'left':
            left1.append(pygame.Rect(player1.left-BULLETSIZE, player1.centery-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
        if direction1 == 'right':
            right1.append(pygame.Rect(player1.right, player1.centery-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
        if direction1 == 'up':
            up1.append(pygame.Rect(player1.centerx-(BULLETSIZE/2), player1.top-BULLETSIZE, BULLETSIZE, BULLETSIZE))
        if direction1 == 'down':
            down1.append(pygame.Rect(player1.centerx-(BULLETSIZE/2), player1.bottom, BULLETSIZE, BULLETSIZE))
        BULLETINTERVAL1 = 0
    if fireGun2 and BULLETINTERVAL2 == BULLETGAP:
        if direction2 == 'left':
            left2.append(pygame.Rect(player2.left-BULLETSIZE, player2.centery-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
        if direction2 == 'right':
            right2.append(pygame.Rect(player2.right, player2.centery-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
        if direction2 == 'up':
            up2.append(pygame.Rect(player2.centerx-(BULLETSIZE/2), player2.top-BULLETSIZE, BULLETSIZE, BULLETSIZE))
        if direction2 == 'down':
            down2.append(pygame.Rect(player2.centerx-(BULLETSIZE/2), player2.bottom, BULLETSIZE, BULLETSIZE))
        BULLETINTERVAL2 = 0
    
    # move the player
    if moveDown1 and player1.bottom < WINDOWHEIGHT:
        player1.top += MOVESPEED
    if moveUp1 and player1.top > 0:
        player1.top -= MOVESPEED
    if moveLeft1 and player1.left > 0:
        player1.left -= MOVESPEED
    if moveRight1 and player1.right < WINDOWWIDTH:
        player1.right += MOVESPEED
    if moveDown2 and player2.bottom < WINDOWHEIGHT:
        player2.top += MOVESPEED
    if moveUp2 and player2.top > 0:
        player2.top -= MOVESPEED
    if moveLeft2 and player2.left > 0:
        player2.left -= MOVESPEED
    if moveRight2 and player2.right < WINDOWWIDTH:
        player2.right += MOVESPEED
    
    # draw the player onto the surface
    windowSurface.blit(playerStretchedImage1, player1)
    windowSurface.blit(playerStretchedImage2, player2)

    # draw the food
    for i in range(len(down1)):
        windowSurface.blit(bulletStretchedImage13, down1[i])
    for i in range(len(up1)):
        windowSurface.blit(bulletStretchedImage14, up1[i])
    for i in range(len(left1)):
        windowSurface.blit(bulletStretchedImage11, left1[i])
    for i in range(len(right1)):
        windowSurface.blit(bulletStretchedImage12, right1[i])
    for i in range(len(down2)):
        windowSurface.blit(bulletStretchedImage23, down2[i])
    for i in range(len(up2)):
        windowSurface.blit(bulletStretchedImage24, up2[i])
    for i in range(len(left2)):
        windowSurface.blit(bulletStretchedImage21, left2[i])
    for i in range(len(right2)):
        windowSurface.blit(bulletStretchedImage22, right2[i])

    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(SPEED)
