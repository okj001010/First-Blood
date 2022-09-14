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
basicFont1 = pygame.font.SysFont('Arial', 48)
basicFont2 = pygame.font.SysFont('Arial', 30)

# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)

# set up the player and bullet data structure
BULLETSIZE = 30
SPEED = 75
startbutton = pygame.Rect(WINDOWWIDTH/2-100, WINDOWHEIGHT/2-30, 200, 60)
player1 = pygame.Rect(int(WINDOWWIDTH/4)-25, int(WINDOWHEIGHT/2)-25, 100, 100)
player2 = pygame.Rect(int(WINDOWWIDTH/4*3)-25, int(WINDOWHEIGHT/2)-25, 50, 50)

playerImage1or = pygame.image.load('icon1_open(r).png')
playerStretchedImage1or = pygame.transform.scale(playerImage1or, (50, 50))
playerImage1ol = pygame.image.load('icon1_open(l).png')
playerStretchedImage1ol = pygame.transform.scale(playerImage1ol, (50, 50))
playerImage1ou = pygame.image.load('icon1_open(u).png')
playerStretchedImage1ou = pygame.transform.scale(playerImage1ou, (50, 50))
playerImage1od = pygame.image.load('icon1_open(d).png')
playerStretchedImage1od = pygame.transform.scale(playerImage1od, (50, 50))

playerImage1cr = pygame.image.load('icon1_close(r).png')
playerStretchedImage1cr = pygame.transform.scale(playerImage1cr, (50, 50))
playerImage1cl = pygame.image.load('icon1_close(l).png')
playerStretchedImage1cl = pygame.transform.scale(playerImage1cl, (50, 50))
playerImage1cu = pygame.image.load('icon1_close(u).png')
playerStretchedImage1cu = pygame.transform.scale(playerImage1cu, (50, 50))
playerImage1cd = pygame.image.load('icon1_close(d).png')
playerStretchedImage1cd = pygame.transform.scale(playerImage1cd, (50, 50))

playerImage2or = pygame.image.load('icon2_open(r).png')
playerStretchedImage2or = pygame.transform.scale(playerImage2or, (50, 50))
playerImage2ol = pygame.image.load('icon2_open(l).png')
playerStretchedImage2ol = pygame.transform.scale(playerImage2ol, (50, 50))
playerImage2ou = pygame.image.load('icon2_open(u).png')
playerStretchedImage2ou = pygame.transform.scale(playerImage2ou, (50, 50))
playerImage2od = pygame.image.load('icon2_open(d).png')
playerStretchedImage2od = pygame.transform.scale(playerImage2od, (50, 50))

playerImage2cr = pygame.image.load('icon2_close(r).png')
playerStretchedImage2cr = pygame.transform.scale(playerImage2cr, (50, 50))
playerImage2cl = pygame.image.load('icon2_close(l).png')
playerStretchedImage2cl = pygame.transform.scale(playerImage2cl, (50, 50))
playerImage2cu = pygame.image.load('icon2_close(u).png')
playerStretchedImage2cu = pygame.transform.scale(playerImage2cu, (50, 50))
playerImage2cd = pygame.image.load('icon2_close(d).png')
playerStretchedImage2cd = pygame.transform.scale(playerImage2cd, (50, 50))

bulletImage11 = pygame.image.load('qleft.png')
bulletStretchedImage11 = pygame.transform.scale(bulletImage11, (BULLETSIZE, BULLETSIZE))
bulletImage12 = pygame.image.load('qright.png')
bulletStretchedImage12 = pygame.transform.scale(bulletImage12, (BULLETSIZE, BULLETSIZE))
bulletImage13 = pygame.image.load('qdown.png')
bulletStretchedImage13 = pygame.transform.scale(bulletImage13, (BULLETSIZE, BULLETSIZE))
bulletImage14 = pygame.image.load('qup.png')
bulletStretchedImage14 = pygame.transform.scale(bulletImage14, (BULLETSIZE, BULLETSIZE))

bulletImage21 = pygame.image.load('fireleft2.png')
bulletStretchedImage21 = pygame.transform.scale(bulletImage21, (BULLETSIZE,int(BULLETSIZE*2/3)))
bulletImage22 = pygame.image.load('fireright2.png')
bulletStretchedImage22 = pygame.transform.scale(bulletImage22, (BULLETSIZE,int(BULLETSIZE*2/3)))
bulletImage23 = pygame.image.load('firedown2.png')
bulletStretchedImage23 = pygame.transform.scale(bulletImage23, (int(BULLETSIZE*2/3),BULLETSIZE))
bulletImage24 = pygame.image.load('fireup2.png')
bulletStretchedImage24 = pygame.transform.scale(bulletImage24, (int(BULLETSIZE*2/3),BULLETSIZE))

bulletImagec11 = pygame.image.load('firecrashleft.png')
bulletStretchedImagec11 = pygame.transform.scale(bulletImagec11, (BULLETSIZE, BULLETSIZE))
bulletImagec12 = pygame.image.load('firecrashright.png')
bulletStretchedImagec12 = pygame.transform.scale(bulletImagec12, (BULLETSIZE, BULLETSIZE))
bulletImagec13 = pygame.image.load('firecrashdown.png')
bulletStretchedImagec13 = pygame.transform.scale(bulletImagec13, (BULLETSIZE, BULLETSIZE))
bulletImagec14 = pygame.image.load('firecrashup.png')
bulletStretchedImagec14 = pygame.transform.scale(bulletImagec14, (BULLETSIZE, BULLETSIZE))

bulletImagec21 = pygame.image.load('firecrashleft2.png')
bulletStretchedImagec21 = pygame.transform.scale(bulletImagec21, (BULLETSIZE,int(BULLETSIZE*2/3)))
bulletImagec22 = pygame.image.load('firecrashright2.png')
bulletStretchedImagec22 = pygame.transform.scale(bulletImagec22, (BULLETSIZE,int(BULLETSIZE*2/3)))
bulletImagec23 = pygame.image.load('firecrashdown2.png')
bulletStretchedImagec23 = pygame.transform.scale(bulletImagec23, (int(BULLETSIZE*2/3),BULLETSIZE))
bulletImagec24 = pygame.image.load('firecrashup2.png')
bulletStretchedImagec24 = pygame.transform.scale(bulletImagec24, (int(BULLETSIZE*2/3),BULLETSIZE))

down1 = []
up1 = []
right1 = []
left1 = []
direction1 = 'right'
down2 = []
up2 = []
right2 = []
left2 = []
down2crash = []
up2crash = []
left2crash = []
right2crash = []
down2c = []
up2c = []
left2c = []
right2c = []

direction2 = 'left'
backgroundImage = pygame.image.load('brickTile.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
text1 = basicFont2.render('Player1 WIN!', True, BLACK, WHITE)
text2 = basicFont2.render('Player2 WIN!', True, BLACK, WHITE)
textstart = basicFont1.render('GAME START', True, WHITE, BLACK)

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

GAMESTART = 1
WINNER = 1
GAMEEND = 1
RESTART = 1
WHO = 0
mousex = 0
mousey = 0
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
HP1 = player1.width
HP2 = player2.width
ascore = 0
bscore = 0
    
while RESTART:
    player1 = pygame.Rect(int(WINDOWWIDTH/4)-25, int(WINDOWHEIGHT/2)-25, 50, 50)
    player2 = pygame.Rect(int(WINDOWWIDTH/4*3)-25, int(WINDOWHEIGHT/2)-25, 50, 50)
    HP1 = player1.width
    HP2 = player2.width
    GAMEEND = 1
    down1 = []
    up1 = []
    right1 = []
    left1 = []
    direction1 = 'right'
    down2 = []
    up2 = []
    right2 = []
    left2 = []
    down2c = []
    up2c = []
    left2c = []
    right2c = []
    down2crash = []
    up2crash = []
    left2crash = []
    right2crash = []
    direction2 = 'left'
    FIREBUGTRUE1 = False
    FIREBUGTRUE2 = False
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

    while GAMESTART:
        windowSurface.fill(BLACK)
        textstartRect = textstart.get_rect()
        textstartRect.centerx = windowSurface.get_rect().centerx
        textstartRect.centery = windowSurface.get_rect().centery
        windowSurface.blit(textstart, textstartRect)
        mousex = 0
        mousey = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
        if mousex > startbutton.left and mousex < startbutton.right and mousey > startbutton.top and mousey < startbutton.bottom:
            GAMESTART = 0
            WINNER = 1

        # draw the window onto the screen
        pygame.display.update()
        mainClock.tick(SPEED)

    # run the game loop
    while WINNER:
        # check for events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                # change the keyboard variables
                if event.key == ord('a'):
                    moveLeft1 = True
                    direction1 = 'left'
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == K_LEFT:
                    moveLeft2 = True
                    direction2 = 'left'
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == ord('d'):
                    moveRight1 = True
                    direction1 = 'right'
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == K_RIGHT:
                    moveRight2 = True
                    direction2 = 'right'
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == ord('w'):
                    moveUp1 = True
                    direction1 = 'up'
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == K_UP :
                    moveUp2 = True
                    direction2 = 'up'
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == ord('s'):
                    moveDown1 = True
                    direction1 = 'down'
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == K_DOWN :
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

        # don't fire the gun 1
        if FIREBUGTRUE1 and FIREBUG1 < FIREBUGINTERVAL+10:
            FIREBUG1 +=1
        if FIREBUGTRUE2 and FIREBUG2 < FIREBUGINTERVAL+10:
            FIREBUG2 +=1
    
        # draw the background onto the surface
        windowSurface.blit(backgroundStretchedImage, (0,0))

        # remove the bullet
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
                down2crash.append(pygame.Rect(down2[0].left, down2[0].top, BULLETSIZE, BULLETSIZE))              
                down2.remove(down2[0])
                down2c.append(0)
        for i in range(len(down2)):
            down2[i].bottom += BULLETSPEED
        if len(up2) > 0:
            if up2[0].top < 0:
                up2crash.append(pygame.Rect(up2[0].left, up2[0].top, BULLETSIZE, BULLETSIZE))              
                up2.remove(up2[0])
                up2c.append(0)
        for i in range(len(up2)):
            up2[i].top -= BULLETSPEED
        if len(left2) > 0:
            if left2[0].left < 0:
                left2crash.append(pygame.Rect(left2[0].left, left2[0].top, BULLETSIZE, BULLETSIZE))              
                left2.remove(left2[0])
                left2c.append(0)
        for i in range(len(left2)):
            left2[i].left -= BULLETSPEED 
        if len(right2) > 0:
            if right2[0].right > WINDOWWIDTH:
                right2crash.append(pygame.Rect(right2[0].left, right2[0].top, BULLETSIZE, BULLETSIZE))              
                right2.remove(right2[0])
                right2c.append(0)
        for i in range(len(right2)):
            right2[i].right += BULLETSPEED

        # don't fire the gun 2
        if(fireGun1):
            BULLETINTERVAL1 += 1
        if(fireGun2):
            BULLETINTERVAL2 += 1

        # fire gun
        if fireGun1 and BULLETINTERVAL1 == BULLETGAP:
            if direction1 == 'left':
                left1.append(pygame.Rect(player1.left+25-BULLETSIZE, player1.centery-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
            if direction1 == 'right':
                right1.append(pygame.Rect(player1.right-25, player1.centery-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
            if direction1 == 'up':
                up1.append(pygame.Rect(player1.centerx-(BULLETSIZE/2), player1.top+25-BULLETSIZE, BULLETSIZE, BULLETSIZE))
            if direction1 == 'down':
                down1.append(pygame.Rect(player1.centerx-(BULLETSIZE/2), player1.bottom-25, BULLETSIZE, BULLETSIZE))
            BULLETINTERVAL1 = 0
        if fireGun2 and BULLETINTERVAL2 == BULLETGAP:
            if direction2 == 'left':
                left2.append(pygame.Rect(player2.left+25-BULLETSIZE, player2.centery+5-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
            if direction2 == 'right':
                right2.append(pygame.Rect(player2.right-25, player2.centery+5-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
            if direction2 == 'up':
                up2.append(pygame.Rect(player2.centerx+5-(BULLETSIZE/2), player2.top+25-BULLETSIZE, BULLETSIZE, BULLETSIZE))
            if direction2 == 'down':
                down2.append(pygame.Rect(player2.centerx+5-(BULLETSIZE/2), player2.bottom-25, BULLETSIZE, BULLETSIZE))
            BULLETINTERVAL2 = 0

        # Ouch!!!
        for i in left1[:]:
            if player2.colliderect(i):
                #left1crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))
                left1.remove(i)
                HP2 -= 10
        for i in right1[:]:
            if player2.colliderect(i):
                #right1crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))                          
                right1.remove(i)
                HP2 -= 10
        for i in up1[:]:
            if player2.colliderect(i):
                #up1crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))              
                up1.remove(i)
                HP2 -= 10
        for i in down1[:]:
            if player2.colliderect(i):
                #down1crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))
                down1.remove(i)
                HP2 -= 10
        for i in left2[:]:
            if player1.colliderect(i):
                left2crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))
                left2c.append(0)
                left2.remove(i)
                HP1 -= 10
        for i in right2[:]:
            if player1.colliderect(i):
                right2crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))              
                right2c.append(0)
                right2.remove(i)
                HP1 -= 10
        for i in up2[:]:
            if player1.colliderect(i):
                up2crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))              
                up2c.append(0)
                up2.remove(i)
                HP1 -= 10
        for i in down2[:]:
            if player1.colliderect(i):
                down2crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))                
                down2c.append(0)
                down2.remove(i)
                HP1 -= 10
        if HP1 < 0:
            HP1 += 10
            WINNER = 0
            WHO = 1
            bscore += 1
        if HP2 < 0:
            HP2 += 10
            WINNER = 0
            WHO = 2
            ascore +=1
        
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
    
        if direction1 == 'right' and not fireGun1:
            windowSurface.blit(playerStretchedImage1cr, player1)
        if direction1 == 'left' and not fireGun1:
            windowSurface.blit(playerStretchedImage1cl, player1)
        if direction1 == 'up' and not fireGun1:
            windowSurface.blit(playerStretchedImage1cu, player1)
        if direction1 == 'down' and not fireGun1:
            windowSurface.blit(playerStretchedImage1cd, player1)
        if direction1 == 'right' and fireGun1:
            windowSurface.blit(playerStretchedImage1or, player1)
        if direction1 == 'left' and fireGun1:
            windowSurface.blit(playerStretchedImage1ol, player1)
        if direction1 == 'up' and fireGun1:
            windowSurface.blit(playerStretchedImage1ou, player1)
        if direction1 == 'down' and fireGun1:
            windowSurface.blit(playerStretchedImage1od, player1)
        pygame.draw.rect(windowSurface, WHITE, (player1.left, player1.top - 10, player1.width, 5))
        pygame.draw.rect(windowSurface, RED, (player1.left, player1.top - 10, HP1, 5))

        if direction2 == 'right' and not fireGun2:
            windowSurface.blit(playerStretchedImage2cr, player2)
        if direction2 == 'left' and not fireGun2:
            windowSurface.blit(playerStretchedImage2cl, player2)
        if direction2 == 'up' and not fireGun2:
            windowSurface.blit(playerStretchedImage2cu, player2)
        if direction2 == 'down' and not fireGun2:
            windowSurface.blit(playerStretchedImage2cd, player2)
        if direction2 == 'right' and fireGun2:
            windowSurface.blit(playerStretchedImage2or, player2)
        if direction2 == 'left' and fireGun2:
            windowSurface.blit(playerStretchedImage2ol, player2)
        if direction2 == 'up' and fireGun2:
            windowSurface.blit(playerStretchedImage2ou, player2)
        if direction2 == 'down' and fireGun2:
            windowSurface.blit(playerStretchedImage2od, player2)
        pygame.draw.rect(windowSurface, WHITE, (player2.left, player2.top - 10, player2.width, 5))
        pygame.draw.rect(windowSurface, RED, (player2.left, player2.top - 10, HP2, 5))

        # draw the bullet
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

        for i in range(len(down2crash)):
            if down2c[i] < 10:
                windowSurface.blit(bulletStretchedImagec23, down2crash[i])
                down2c[i] += 1
            if down2c[i] == 0:
                down2c.remove(i)
                down2crash.remove(i)
        for i in range(len(up2crash)):
            if up2c[i] < 10:
                windowSurface.blit(bulletStretchedImagec24, up2crash[i])
                up2c[i] += 1
            if up2c[i] == 0:
                up2c.remove(i)
                up2crash.remove(i)
        for i in range(len(left2crash)):
            if left2c[i] < 10:
                windowSurface.blit(bulletStretchedImagec21, left2crash[i])
                left2c[i] += 1
            if left2c[i] == 0:
                left2c.remove(i)
                left2crash.remove(i)
        for i in range(len(right2crash)):
            if right2c[i] < 10:
                windowSurface.blit(bulletStretchedImagec22, right2crash[i])
                right2c[i] += 1
            if right2c[i] == 0:
                right2c.remove(i)
                right2crash.remove(i)
        textScore = basicFont1.render('%d : %d'%(ascore,bscore), True, BLACK, WHITE)    
        textScoreRect = textScore.get_rect()
        textScoreRect.centery = 30
        textScoreRect.centerx = int(WINDOWWIDTH/2)
        windowSurface.blit(textScore, textScoreRect)
        
        # draw the window onto the screen
        pygame.display.update()
        mainClock.tick(SPEED)

    while GAMEEND:
        windowSurface.fill(WHITE)
        mousex = 0
        text = basicFont1.render('press to play again', True, BLACK, WHITE)
        text1Rect = text1.get_rect()
        text2Rect = text2.get_rect()
        textRect = text.get_rect()
        text1Rect.centerx = windowSurface.get_rect().centerx
        text1Rect.centery = int(WINDOWHEIGHT/3)
        text2Rect.centerx = windowSurface.get_rect().centerx
        text2Rect.centery = int(WINDOWHEIGHT/3)
        textRect.centerx = windowSurface.get_rect().centerx
        textRect.centery = windowSurface.get_rect().centery
        if WHO == 1:
            windowSurface.blit(text2, text2Rect)
        if WHO == 2 :
            windowSurface.blit(text1, text1Rect)
        windowSurface.blit(text,textRect)
        mousey = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
        if mousex > textRect.left and mousex < textRect.right and mousey > startbutton.top and mousey < startbutton.bottom:
            GAMEEND = 0
            RESTART = 1
            GAMESTART = 1

        # draw the window onto the screen
        pygame.display.update()
        mainClock.tick(SPEED)

    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(SPEED)
