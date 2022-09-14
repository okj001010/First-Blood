import pygame, sys, random
from pygame.locals import *

# pygame set up
pygame.init()
mainClock = pygame.time.Clock()

# window set up
WINDOWWIDTH = 700
WINDOWHEIGHT = 700
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Input')
basicFont1 = pygame.font.SysFont('Agency FB', 60)
basicFont2 = pygame.font.SysFont('Arial', 30)

# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)

# set up the player and bullet data structure
SPEED = 75
SIZE1 = 50
SIZE2 = 50
ITEMSIZE = 40
ITEMCOUNTER = 0
ITEMTIME = SPEED*5
SELECTITEM = 0
BULLETSIZE = 30
startbutton = pygame.Rect(WINDOWWIDTH/2-100, WINDOWHEIGHT/2-30, 200, 60)
player1 = pygame.Rect(int(WINDOWWIDTH/4)-25, int(WINDOWHEIGHT/2)-25, SIZE1, SIZE1)
player2 = pygame.Rect(int(WINDOWWIDTH/4*3)-25, int(WINDOWHEIGHT/2)-25, SIZE2, SIZE2)

playerImage1ou = pygame.image.load('icon1_open(u).png')
playerImage1od = pygame.image.load('icon1_open(d).png')
playerImage1or = pygame.image.load('icon1_open(r).png')
playerImage1ol = pygame.image.load('icon1_open(l).png')

playerImage1cu = pygame.image.load('icon1_close(u).png')
playerImage1cd = pygame.image.load('icon1_close(d).png')
playerImage1cr = pygame.image.load('icon1_close(r).png')
playerImage1cl = pygame.image.load('icon1_close(l).png')

playerImage2ou = pygame.image.load('icon2_open(u).png')
playerImage2od = pygame.image.load('icon2_open(d).png')
playerImage2or = pygame.image.load('icon2_open(r).png')
playerImage2ol = pygame.image.load('icon2_open(l).png')

playerImage2cu = pygame.image.load('icon2_close(u).png')
playerImage2cd = pygame.image.load('icon2_close(d).png')
playerImage2cr = pygame.image.load('icon2_close(r).png')
playerImage2cl = pygame.image.load('icon2_close(l).png')

bulletImagei = pygame.image.load('ice_magic.png')
bulletStretchedImagei = pygame.transform.scale(bulletImagei, (BULLETSIZE, BULLETSIZE))

bulletImage11 = pygame.image.load('bulletup3.png')
bulletStretchedImage11 = pygame.transform.scale(bulletImage11, (int(BULLETSIZE*2/3),BULLETSIZE))
bulletImage12 = pygame.image.load('bulletdown3.png')
bulletStretchedImage12 = pygame.transform.scale(bulletImage12, (int(BULLETSIZE*2/3),BULLETSIZE))
bulletImage13 = pygame.image.load('bulletleft3.png')
bulletStretchedImage13 = pygame.transform.scale(bulletImage13, (BULLETSIZE,int(BULLETSIZE*2/3)))
bulletImage14 = pygame.image.load('bulletright3.png')
bulletStretchedImage14 = pygame.transform.scale(bulletImage14, (BULLETSIZE,int(BULLETSIZE*2/3)))

bulletImage21 = pygame.image.load('bulletup2.png')
bulletStretchedImage21 = pygame.transform.scale(bulletImage21, (int(BULLETSIZE*2/3),BULLETSIZE))
bulletImage22 = pygame.image.load('bulletdown2.png')
bulletStretchedImage22 = pygame.transform.scale(bulletImage22, (int(BULLETSIZE*2/3),BULLETSIZE))
bulletImage23 = pygame.image.load('bulletleft2.png')
bulletStretchedImage23 = pygame.transform.scale(bulletImage23, (BULLETSIZE,int(BULLETSIZE*2/3)))
bulletImage24 = pygame.image.load('bulletright2.png')
bulletStretchedImage24 = pygame.transform.scale(bulletImage24, (BULLETSIZE,int(BULLETSIZE*2/3)))

bulletImagec11 = pygame.image.load('firecrashup1.png')
bulletStretchedImagec11 = pygame.transform.scale(bulletImagec11, (BULLETSIZE, BULLETSIZE))
bulletImagec12 = pygame.image.load('firecrashdown1.png')
bulletStretchedImagec12 = pygame.transform.scale(bulletImagec12, (BULLETSIZE, BULLETSIZE))
bulletImagec13 = pygame.image.load('firecrashleft1.png')
bulletStretchedImagec13 = pygame.transform.scale(bulletImagec13, (BULLETSIZE, BULLETSIZE))
bulletImagec14 = pygame.image.load('firecrashright1.png')
bulletStretchedImagec14 = pygame.transform.scale(bulletImagec14, (BULLETSIZE, BULLETSIZE))

bulletImagec21 = pygame.image.load('firecrashup2.png')
bulletStretchedImagec21 = pygame.transform.scale(bulletImagec21, (int(BULLETSIZE*2/3),BULLETSIZE))
bulletImagec22 = pygame.image.load('firecrashdown2.png')
bulletStretchedImagec22 = pygame.transform.scale(bulletImagec22, (int(BULLETSIZE*2/3),BULLETSIZE))
bulletImagec23 = pygame.image.load('firecrashleft2.png')
bulletStretchedImagec23 = pygame.transform.scale(bulletImagec23, (BULLETSIZE,int(BULLETSIZE*2/3)))
bulletImagec24 = pygame.image.load('firecrashright2.png')
bulletStretchedImagec24 = pygame.transform.scale(bulletImagec24, (BULLETSIZE,int(BULLETSIZE*2/3)))

laserImage1 = pygame.image.load('Laser.png')
laserImage2 = pygame.image.load('Laser.png')
laserImage3 = pygame.image.load('Laser2.png')
laserImage4 = pygame.image.load('Laser2.png')

itemImage0 = pygame.image.load('item0.png')
itemImage1 = pygame.image.load('item1.png')
itemImage2 = pygame.image.load('item2.png')
itemImage3 = pygame.image.load('item3.png')
itemImage4 = pygame.image.load('item4.png')
itemImage5 = pygame.image.load('item5.png')
itemImage6 = pygame.image.load('item6.png')
itemImage7 = pygame.image.load('item7.png')
itemStretchedImage0 = pygame.transform.scale(itemImage0, (ITEMSIZE, ITEMSIZE))
itemStretchedImage1 = pygame.transform.scale(itemImage1, (ITEMSIZE, ITEMSIZE))
itemStretchedImage2 = pygame.transform.scale(itemImage2, (ITEMSIZE, ITEMSIZE))
itemStretchedImage3 = pygame.transform.scale(itemImage3, (ITEMSIZE, ITEMSIZE))
itemStretchedImage4 = pygame.transform.scale(itemImage4, (ITEMSIZE, ITEMSIZE))
itemStretchedImage5 = pygame.transform.scale(itemImage5, (ITEMSIZE, ITEMSIZE))
itemStretchedImage6 = pygame.transform.scale(itemImage6, (ITEMSIZE, ITEMSIZE))
itemStretchedImage7 = pygame.transform.scale(itemImage7, (ITEMSIZE, ITEMSIZE))

turretImage11 = pygame.image.load('tankup1.png')
turretStretchedImage11 = pygame.transform.scale(turretImage11, (ITEMSIZE, ITEMSIZE))
turretImage12 = pygame.image.load('tankdown1.png')
turretStretchedImage12 = pygame.transform.scale(turretImage12, (ITEMSIZE, ITEMSIZE))
turretImage13 = pygame.image.load('tankleft1.png')
turretStretchedImage13 = pygame.transform.scale(turretImage13, (ITEMSIZE, ITEMSIZE))
turretImage14 = pygame.image.load('tankright1.png')
turretStretchedImage14 = pygame.transform.scale(turretImage14, (ITEMSIZE, ITEMSIZE))

turretImage21 = pygame.image.load('tankup1.png')
turretStretchedImage21 = pygame.transform.scale(turretImage21, (ITEMSIZE, ITEMSIZE))
turretImage22 = pygame.image.load('tankdown1.png')
turretStretchedImage22 = pygame.transform.scale(turretImage22, (ITEMSIZE, ITEMSIZE))
turretImage23 = pygame.image.load('tankleft1.png')
turretStretchedImage23 = pygame.transform.scale(turretImage23, (ITEMSIZE, ITEMSIZE))
turretImage24 = pygame.image.load('tankright1.png')
turretStretchedImage24 = pygame.transform.scale(turretImage24, (ITEMSIZE, ITEMSIZE))

skullImage = pygame.image.load('skull.png')
mineImage = pygame.image.load('mine.png')
mineStretchedImage = pygame.transform.scale(mineImage, (ITEMSIZE, ITEMSIZE))

backgroundImage = pygame.image.load('brickTile.jpg')
backgroundStretchedImage = pygame.transform.scale(backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
text1 = basicFont2.render('Player1 WIN!', True, BLACK, WHITE)
text2 = basicFont2.render('Player2 WIN!', True, BLACK, WHITE)
textstart = basicFont1.render('GAME START', True, WHITE, BLACK)

GAMESTART = 1
WINNER = 1
GAMEEND = 1
RESTART = 1
WHO = 0
mousex = 0
mousey = 0
BULLETSPEED = 4
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
    player1 = pygame.Rect(int(WINDOWWIDTH/4)-25, int(WINDOWHEIGHT/2)-25, SIZE1, SIZE1)
    player2 = pygame.Rect(int(WINDOWWIDTH/4*3)-25, int(WINDOWHEIGHT/2)-25, SIZE2, SIZE2)
    turret1 = pygame.Rect(0, 0, ITEMSIZE, ITEMSIZE)
    turret2 = pygame.Rect(0, 0, ITEMSIZE, ITEMSIZE)
    HP1 = player1.width
    HP2 = player2.width
    GAMEEND = 1
    up1 = []
    down1 = []
    left1 = []
    right1 = []
    up1c = []
    down1c = []
    left1c = []
    right1c = []
    up1crash = []
    down1crash = []
    left1crash = []
    right1crash = []
    direction1 = 'right'
    up2 = []
    down2 = []
    left2 = []
    right2 = []
    up2c = []
    down2c = []
    left2c = []
    right2c = []
    up2crash = []
    down2crash = []
    left2crash = []
    right2crash = []
    direction2 = 'left'
    FIREBUGTRUE1 = False
    FIREBUGTRUE2 = False
    moveUp1 = False
    moveDown1 = False
    moveLeft1 = False
    moveRight1 = False
    moveUp2 = False
    moveDown2 = False
    moveLeft2 = False
    moveRight2 = False
    fireGun1 = False
    fireGun2 = False
    ITEM0 = []
    ITEM1 = []
    ITEM2 = []
    ITEM3 = []
    ITEM4 = []
    ITEM5 = []
    ITEM6 = []
    ITEM7 = []
    SISE1 = 0
    SISE2 = 0
    SISE1_COUNTER = 0
    SISE2_COUNTER = 0
    SISETIME = SPEED*5
    ICE1 = 0
    ICE2 = 0
    ICE1_COUNTER = 0
    ICE2_COUNTER = 0
    ICETIME = SPEED*5
    LASER1 = 0
    LASER2 = 0
    LASER1_COUNTER = 0
    LASER2_COUNTER = 0
    LASERTIME = SPEED*2
    SHIELD1 = 0
    SHIELD2 = 0
    SHIELD1_COUNTER = 0
    SHIELD2_COUNTER = 0
    SHIELDTIME = SPEED*3
    TURRET1 = 0
    TURRET2 = 0
    TURRET_direction1 = "right"
    TURRET_direction2 = "right"
    TURRET1_COUNTER = 0
    TURRET2_COUNTER = 0
    TURRETTIME = SPEED*10
    SKULL1 = 0
    SKULL2 = 0
    SKULL_COUNTER = 0
    SKULLTIME = SPEED*3
    MINE1 = []
    MINE2 = []
    TRAPPED1 = 0
    TRAPPED2 = 0
    MINE1_COUNTER = 0
    MINE2_COUNTER = 0
    MINETIME = SPEED*2
    MOVESPEED1 = 3
    MOVESPEED2 = 3

    while GAMESTART:
        SIZE1 = 50
        SIZE2 = 50
        pplayer1 = pygame.Rect(player1.left, player1.top, SIZE1, SIZE1)
        pplayer2 = pygame.Rect(player2.left, player2.top, SIZE2, SIZE2)
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
        if mousey > startbutton.top and mousey < startbutton.bottom and mousex > startbutton.left and mousex < startbutton.right:
            GAMESTART = 0
            WINNER = 1

        # draw the window onto the screen
        pygame.display.update()
        mainClock.tick(SPEED)

    # run the game loop
    while WINNER:
        pplayer1 = pygame.Rect(pplayer1.left, pplayer1.top, SIZE1, SIZE1)
        pplayer2 = pygame.Rect(pplayer2.left, pplayer2.top, SIZE2, SIZE2)
        playerStretchedImage1ou = pygame.transform.scale(playerImage1ou, (SIZE1, SIZE1))
        playerStretchedImage1od = pygame.transform.scale(playerImage1od, (SIZE1, SIZE1))
        playerStretchedImage1ol = pygame.transform.scale(playerImage1ol, (SIZE1, SIZE1))
        playerStretchedImage1or = pygame.transform.scale(playerImage1or, (SIZE1, SIZE1))
        playerStretchedImage1cu = pygame.transform.scale(playerImage1cu, (SIZE1, SIZE1))
        playerStretchedImage1cd = pygame.transform.scale(playerImage1cd, (SIZE1, SIZE1))
        playerStretchedImage1cl = pygame.transform.scale(playerImage1cl, (SIZE1, SIZE1))
        playerStretchedImage1cr = pygame.transform.scale(playerImage1cr, (SIZE1, SIZE1))
        playerStretchedImage2ou = pygame.transform.scale(playerImage2ou, (SIZE2, SIZE2))
        playerStretchedImage2od = pygame.transform.scale(playerImage2od, (SIZE2, SIZE2))
        playerStretchedImage2ol = pygame.transform.scale(playerImage2ol, (SIZE2, SIZE2))
        playerStretchedImage2or = pygame.transform.scale(playerImage2or, (SIZE2, SIZE2))
        playerStretchedImage2cu = pygame.transform.scale(playerImage2cu, (SIZE2, SIZE2))
        playerStretchedImage2cd = pygame.transform.scale(playerImage2cd, (SIZE2, SIZE2))
        playerStretchedImage2cl = pygame.transform.scale(playerImage2cl, (SIZE2, SIZE2))
        playerStretchedImage2cr = pygame.transform.scale(playerImage2cr, (SIZE2, SIZE2))

        laserStretchedImage11 = pygame.transform.scale(laserImage1, (pplayer1.left+5, BULLETSIZE))
        laserStretchedImage12 = pygame.transform.scale(laserImage2, (WINDOWHEIGHT-pplayer1.right+5, BULLETSIZE))
        laserStretchedImage13 = pygame.transform.scale(laserImage3, (BULLETSIZE, pplayer1.top+5))
        laserStretchedImage14 = pygame.transform.scale(laserImage4, (BULLETSIZE, WINDOWWIDTH-pplayer1.bottom+5))
        laserStretchedImage21 = pygame.transform.scale(laserImage1, (pplayer2.left+5, BULLETSIZE))
        laserStretchedImage22 = pygame.transform.scale(laserImage2, (WINDOWHEIGHT-pplayer2.right+5, BULLETSIZE))
        laserStretchedImage23 = pygame.transform.scale(laserImage3, (BULLETSIZE, pplayer2.top+5))
        laserStretchedImage24 = pygame.transform.scale(laserImage4, (BULLETSIZE, WINDOWWIDTH-pplayer2.bottom+5))

        uplayer1 = pygame.Rect(pplayer1.centerx-(BULLETSIZE/2), 0, BULLETSIZE, pplayer1.top)
        dplayer1 = pygame.Rect(pplayer1.centerx-(BULLETSIZE/2), pplayer1.bottom, BULLETSIZE, WINDOWHEIGHT-pplayer1.bottom)
        lplayer1 = pygame.Rect(0, pplayer1.centery-(BULLETSIZE/2), pplayer1.left, BULLETSIZE)
        rplayer1 = pygame.Rect(pplayer1.right, pplayer1.centery-(BULLETSIZE/2), WINDOWWIDTH-pplayer1.right, BULLETSIZE)

        uplayer2 = pygame.Rect(pplayer2.centerx-(BULLETSIZE/2), 0, BULLETSIZE, pplayer2.top)
        dplayer2 = pygame.Rect(pplayer2.centerx-(BULLETSIZE/2), pplayer2.bottom, BULLETSIZE, WINDOWHEIGHT-pplayer2.bottom)
        lplayer2 = pygame.Rect(0, pplayer2.centery-(BULLETSIZE/2), pplayer2.left, BULLETSIZE)
        rplayer2 = pygame.Rect(pplayer2.right, pplayer2.centery-(BULLETSIZE/2), WINDOWWIDTH-pplayer2.right, BULLETSIZE)
        
        skullStretchedImage1 = pygame.transform.scale(skullImage, (SIZE1, SIZE1))
        skullStretchedImage2 = pygame.transform.scale(skullImage, (SIZE2, SIZE2))
        
        # check for events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                # change the keyboard variables
                if event.key == ord('w'):
                    if not SKULL1:
                        direction1 = 'up'
                        moveUp1 = True
                        moveDown1 = False
                    if SKULL1:
                        direction1 = 'down'
                        moveDown1 = True
                        moveUp1 = False
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == K_UP :
                    if not SKULL2:
                        direction2 = 'up'
                        moveUp2 = True
                        moveDown2 = False
                    if SKULL2:
                        direction2 = 'down'
                        moveDown2 = True
                        moveUp2 = False
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == ord('s'):
                    if not SKULL1:
                        direction1 = 'down'
                        moveDown1 = True
                        moveUp1 = False
                    if SKULL1:
                        direction1 = 'up'
                        moveUp1 = True
                        mvoeDown1 = False
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == K_DOWN :
                    if not SKULL2:
                        direction2 = 'down'
                        moveDown2 = True
                        moveUp2 = False
                    if SKULL2:
                        direction2 = 'up'
                        moveUp2 = True
                        moveDown2 = False
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == ord('a'):
                    if not SKULL1:
                        direction1 = 'left'
                        moveLeft1 = True
                        moveRight1 = False
                    if SKULL1:
                        direction1 = 'right'
                        moveRight1 = True
                        moveLeft1 = False
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == K_LEFT:
                    if not SKULL2:
                        direction2 = 'left'
                        moveLeft2 = True
                        moveRight2 = False
                    if SKULL2:
                        direction2 = 'right'
                        moveRight2 = True
                        moveLeft2 = False
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == ord('d'):
                    if not SKULL1:
                        direction1 = 'right'
                        moveRight1 = True
                        moveLeft1 = False
                    if SKULL1:
                        direction1 = 'left'
                        moveLeft1 = True
                        moveRight1 = False
                    FIREBUGTRUE1 = False
                    FIREBUGTRUE2 = False
                    FIREBUG1 = FIREBUGINTERVAL
                    FIREBUG2 = FIREBUGINTERVAL
                if event.key == K_RIGHT:
                    if not SKULL2:
                        direction2 = 'right'
                        moveRight2 = True
                        moveLeft2 = False
                    if SKULL2:
                        direction2 = 'left'
                        moveLeft2 = True
                        moveRight2 = False
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
                if event.key == ord('w'):
                    if not SKULL1:
                        moveUp1 = False
                    if SKULL1:
                        moveDown1 = False
                if event.key == K_UP :
                    if not SKULL2:
                        moveUp2 = False
                    if SKULL2:
                        moveDown2 = False
                if event.key == ord('s'):
                    if not SKULL1:
                        moveDown1 = False
                    if SKULL1:
                        moveUp1 = False
                if event.key == K_DOWN:
                    if not SKULL2:
                        moveDown2 = False
                    if SKULL2:
                        moveUp2 = False
                if event.key == ord('a'):
                    if not SKULL1:
                        moveLeft1 = False
                    if SKULL1:
                        moveRight1 = False
                if event.key == K_LEFT :
                    if not SKULL2:
                        moveLeft2 = False
                    if SKULL2:
                        moveRight2 = False
                if event.key == ord('d'):
                    if not SKULL1:
                        moveRight1 = False
                    if SKULL1:
                        moveLeft1 = False
                if event.key == K_RIGHT:
                    if not SKULL2:
                        moveRight2 = False
                    if SKULL2:
                        moveLeft2 = False
                if event.key == ord(' '):
                    fireGun1 = False
                    BULLETINTERVAL1 = BULLETGAP-1
                    if LASER1 == 1:
                        LASER1 = 0
                if event.key == ord('/'):
                    fireGun2 = False
                    BULLETINTERVAL2 = BULLETGAP-1
                    if LASER2 == 1:
                        LASER2 = 0


        # don't fire the gun 1
        if FIREBUGTRUE1 and FIREBUG1 < FIREBUGINTERVAL+10:
            FIREBUG1 +=1
        if FIREBUGTRUE2 and FIREBUG2 < FIREBUGINTERVAL+10:
            FIREBUG2 +=1
    
        # draw the background onto the surface
        windowSurface.blit(backgroundStretchedImage, (0,0))

        # remove the bullet
        if len(up1) > 0:
            if up1[0].top < 0:
                up1crash.append(pygame.Rect(up1[0].left, up1[0].top, BULLETSIZE, BULLETSIZE))              
                up1.remove(up1[0])
                up1c.append(0)
        for i in range(len(up1)):
            up1[i].top -= BULLETSPEED
        if len(down1) > 0:
            if down1[0].bottom > WINDOWHEIGHT:
                down1crash.append(pygame.Rect(down1[0].left, down1[0].top, BULLETSIZE, BULLETSIZE))              
                down1.remove(down1[0])
                down1c.append(0)
        for i in range(len(down1)):
            down1[i].bottom += BULLETSPEED    
        if len(left1) > 0:
            if left1[0].left < 0:
                left1crash.append(pygame.Rect(left1[0].left, left1[0].top, BULLETSIZE, BULLETSIZE))              
                left1.remove(left1[0])
                left1c.append(0)
        for i in range(len(left1)):
            left1[i].left -= BULLETSPEED
        if len(right1) > 0:
            if right1[0].right > WINDOWWIDTH:
                right1crash.append(pygame.Rect(right1[0].left, right1[0].top, BULLETSIZE, BULLETSIZE))              
                right1.remove(right1[0])
                right1c.append(0)
        for i in range(len(right1)):
            right1[i].right += BULLETSPEED
        if len(up2) > 0:
            if up2[0].top < 0:
                up2crash.append(pygame.Rect(up2[0].left, up2[0].top, BULLETSIZE, BULLETSIZE))              
                up2.remove(up2[0])
                up2c.append(0)
        for i in range(len(up2)):
            up2[i].top -= BULLETSPEED
        if len(down2) > 0:
            if down2[0].bottom > WINDOWHEIGHT:
                down2crash.append(pygame.Rect(down2[0].left, down2[0].top, BULLETSIZE, BULLETSIZE))              
                down2.remove(down2[0])
                down2c.append(0)
        for i in range(len(down2)):
            down2[i].bottom += BULLETSPEED
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
        if fireGun1 and BULLETINTERVAL1 == BULLETGAP and LASER1 == 0:
            if direction1 == 'up':
                up1.append(pygame.Rect(pplayer1.centerx+(SIZE2/10)-(BULLETSIZE/2)-(ICE1*5), pplayer1.top+(SIZE1/6)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
            if direction1 == 'down':
                down1.append(pygame.Rect(pplayer1.centerx+(SIZE1/10)-(BULLETSIZE/2)-(ICE1*5), pplayer1.bottom-(SIZE1/6)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
            if direction1 == 'left':
                left1.append(pygame.Rect(pplayer1.left+(SIZE1/6)-(BULLETSIZE/2), pplayer1.centery+(SIZE1/10)-(BULLETSIZE/2)-(ICE1*5), BULLETSIZE, BULLETSIZE))
            if direction1 == 'right':
                right1.append(pygame.Rect(pplayer1.right-(SIZE1/6)-(BULLETSIZE/2), pplayer1.centery+(SIZE2/10)-(BULLETSIZE/2)-(ICE1*5), BULLETSIZE, BULLETSIZE))
            BULLETINTERVAL1 = 0
        if fireGun2 and BULLETINTERVAL2 == BULLETGAP and LASER2 == 0:
            if direction2 == 'up':
                up2.append(pygame.Rect(pplayer2.centerx+(SIZE2/10)-(BULLETSIZE/2)-(ICE2*5), pplayer2.top+(SIZE1/6)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
            if direction2 == 'down':
                down2.append(pygame.Rect(pplayer2.centerx+(SIZE2/10)-(BULLETSIZE/2)-(ICE2*5), pplayer2.bottom-(SIZE1/6)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
            if direction2 == 'left':
                left2.append(pygame.Rect(pplayer2.left+(SIZE2/6)-(BULLETSIZE/2), pplayer2.centery+(SIZE2/10)-(BULLETSIZE/2)-(ICE2*5), BULLETSIZE, BULLETSIZE))
            if direction2 == 'right':
                right2.append(pygame.Rect(pplayer2.right-(SIZE2/6)-(BULLETSIZE/2), pplayer2.centery+(SIZE2/10)-(BULLETSIZE/2)-(ICE2*5), BULLETSIZE, BULLETSIZE))
            BULLETINTERVAL2 = 0

        if LASER1 and fireGun1:
            if direction1 == 'up':
                windowSurface.blit(laserStretchedImage13, uplayer1)
            if direction1 == 'down':
                windowSurface.blit(laserStretchedImage14, dplayer1)
            if direction1 == 'left':
                windowSurface.blit(laserStretchedImage11, lplayer1)
            if direction1 == 'right':
                windowSurface.blit(laserStretchedImage12, rplayer1)
        if LASER2 and fireGun2:
            if direction2 == 'up':
                windowSurface.blit(laserStretchedImage23, uplayer2)
            if direction2 == 'down':
                windowSurface.blit(laserStretchedImage24, dplayer2)
            if direction2 == 'left':
                windowSurface.blit(laserStretchedImage21, lplayer2)
            if direction2 == 'right':
                windowSurface.blit(laserStretchedImage22, rplayer2)
        
        # Ouch!!!
        for i in up1[:]:
            if pplayer2.colliderect(i):
                up1crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))              
                up1c.append(0)
                up1.remove(i)
                if not ICE1:
                    HP2 -= 10
                if ICE1:
                    HP2 -= 8
                    MOVESPEED2 = 1
        for i in down1[:]:
            if pplayer2.colliderect(i):
                down1crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))
                down1c.append(0)
                down1.remove(i)
                if not ICE1:
                    HP2 -= 10
                if ICE1:
                    HP2 -= 8
                    MOVESPEED2 = 1
        for i in left1[:]:
            if pplayer2.colliderect(i):
                left1crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))
                left1c.append(0)
                left1.remove(i)
                if not ICE1:
                    HP2 -= 10
                if ICE1:
                    HP2 -= 8
                    MOVESPEED2 = 1
        for i in right1[:]:
            if pplayer2.colliderect(i):
                right1crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))                          
                right1c.append(0)
                right1.remove(i)
                if not ICE1:
                    HP2 -= 10
                if ICE1:
                    HP2 -= 8
                    MOVESPEED2 = 1
        for i in up2[:]:
            if pplayer1.colliderect(i):
                up2crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))              
                up2c.append(0)
                up2.remove(i)
                if not ICE2:
                    HP1 -= 10
                if ICE2:
                    HP1 -= 8
                    MOVESPEED1 = 1
        for i in down2[:]:
            if pplayer1.colliderect(i):
                down2crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))                
                down2c.append(0)
                down2.remove(i)
                if not ICE2:
                    HP1 -= 10
                if ICE2:
                    HP1 -= 8
                    MOVESPEED1 = 1
        for i in left2[:]:
            if pplayer1.colliderect(i):
                left2crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))
                left2c.append(0)
                left2.remove(i)
                if not ICE2:
                    HP1 -= 10
                if ICE2:
                    HP1 -= 8
                    MOVESPEED1 = 1
        for i in right2[:]:
            if pplayer1.colliderect(i):
                right2crash.append(pygame.Rect(i.left, i.top, BULLETSIZE, BULLETSIZE))              
                right2c.append(0)
                right2.remove(i)
                if not ICE2:
                    HP1 -= 10
                if ICE2:
                    HP1 -= 8
                    MOVESPEED1 = 1

        if direction1 == 'up' and LASER1 and fireGun1 and pplayer2.colliderect(uplayer1):
            HP2 -= 1
        if direction1 == 'down' and LASER1 and fireGun1 and pplayer2.colliderect(dplayer1):
            HP2 -= 1
        if direction1 == 'left' and LASER1 and fireGun1 and pplayer2.colliderect(lplayer1):
            HP2 -= 1
        if direction1 == 'right' and LASER1 and fireGun1 and pplayer2.colliderect(rplayer1):
            HP2 -= 1
        if direction2 == 'up' and LASER2 and fireGun2 and pplayer1.colliderect(uplayer2):
            HP1 -= 1
        if direction2 == 'down' and LASER2 and fireGun2 and pplayer1.colliderect(dplayer2):
            HP1 -= 1
        if direction2 == 'left' and LASER2 and fireGun2 and pplayer1.colliderect(lplayer2):
            HP1 -= 1
        if direction2 == 'right' and LASER2 and fireGun2 and pplayer1.colliderect(rplayer2):
            HP1 -= 1
            
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

        #draw item
        ITEMCOUNTER += 1
        if ITEMCOUNTER >= ITEMTIME:
            ITEMCOUNTER = 0
            randem = random.randint(0,7)
            if randem == 4:
                randem1 = random.randint(80, WINDOWWIDTH-80-ITEMSIZE)
                randem2 = random.randint(80, WINDOWHEIGHT-80-ITEMSIZE)
            else:
                randem1= random.randint(0, WINDOWWIDTH - ITEMSIZE)
                randem2 = random.randint(0, WINDOWHEIGHT - ITEMSIZE)
            if randem == 0:
                ITEM0.append(pygame.Rect(randem1, randem2, ITEMSIZE, ITEMSIZE))
            if randem == 1:
                ITEM1.append(pygame.Rect(randem1, randem2, ITEMSIZE, ITEMSIZE))
            if randem == 2:
                ITEM2.append(pygame.Rect(randem1, randem2, ITEMSIZE, ITEMSIZE))
            if randem == 3:
                ITEM3.append(pygame.Rect(randem1, randem2, ITEMSIZE, ITEMSIZE))
            if randem == 4:
                ITEM4.append(pygame.Rect(randem1, randem2, ITEMSIZE, ITEMSIZE))
            if randem == 5:
                ITEM5.append(pygame.Rect(randem1, randem2, ITEMSIZE, ITEMSIZE))
            if randem == 6:
                ITEM6.append(pygame.Rect(randem1, randem2, ITEMSIZE, ITEMSIZE))
            if randem == 7:
                ITEM7.append(pygame.Rect(randem1, randem2, ITEMSIZE, ITEMSIZE))
            
        for i in range(len(ITEM0)):
            windowSurface.blit(itemStretchedImage0, ITEM0[i])
        for i in range(len(ITEM1)):
            windowSurface.blit(itemStretchedImage1, ITEM1[i])
        for i in range(len(ITEM2)):
            windowSurface.blit(itemStretchedImage2, ITEM2[i])
        for i in range(len(ITEM3)):
            windowSurface.blit(itemStretchedImage3, ITEM3[i])
        for i in range(len(ITEM4)):
            windowSurface.blit(itemStretchedImage4, ITEM4[i])
        for i in range(len(ITEM5)):
            windowSurface.blit(itemStretchedImage5, ITEM5[i])
        for i in range(len(ITEM6)):
            windowSurface.blit(itemStretchedImage6, ITEM6[i])
        for i in range(len(ITEM7)):
            windowSurface.blit(itemStretchedImage7, ITEM7[i])

        for i in range(len(MINE1)):
            if pplayer2.colliderect(MINE1[i]):
                TRAPPED2 = 1
                moveUp2 = False
                moveDown2 = False
                moveLeft2 = False
                moveRight2 = False
                windowSurface.blit(mineStretchedImage, MINE1[i])
                if MINE1_COUNTER == MINETIME:
                    TRAPPED2 = 0
                    MINE1_COUNTER = 0
                    MINE1.remove(MINE1[i])
                    break
                
        for i in range(len(MINE2)):
            if pplayer1.colliderect(MINE2[i]):
                TRAPPED1 = 1
                moveUp1 = False
                moveDown1 = False
                moveLeft1 = False
                moveRight1 = False
                windowSurface.blit(mineStretchedImage, MINE2[i])
                if MINE2_COUNTER == MINETIME:
                    TRAPPED1 = 0
                    MINE2_COUNTER = 0
                    MINE2.remove(MINE2[i])
                    break

        if TRAPPED1:
            MINE2_COUNTER += 1
        if TRAPPED2:
            MINE1_COUNTER += 1

        if moveUp1 and pplayer1.top > 0:
            pplayer1.top -= MOVESPEED1
        if moveDown1 and pplayer1.bottom < WINDOWHEIGHT:
            pplayer1.top += MOVESPEED1
        if moveLeft1 and pplayer1.left > 0:
            pplayer1.left -= MOVESPEED1
        if moveRight1 and pplayer1.right < WINDOWWIDTH:
            pplayer1.right += MOVESPEED1
        if moveUp2 and pplayer2.top > 0:
            pplayer2.top -= MOVESPEED2
        if moveDown2 and pplayer2.bottom < WINDOWHEIGHT:
            pplayer2.top += MOVESPEED2
        if moveLeft2 and pplayer2.left > 0:
            pplayer2.left -= MOVESPEED2
        if moveRight2 and pplayer2.right < WINDOWWIDTH:
            pplayer2.right += MOVESPEED2

        skull1 = pygame.Rect(pplayer1.left, pplayer1.top, SIZE1, SIZE1)
        skull2 = pygame.Rect(pplayer2.left, pplayer2.top, SIZE2, SIZE2)

        if direction1 == 'up' and not fireGun1:
            windowSurface.blit(playerStretchedImage1cu, pplayer1)
        if direction1 == 'down' and not fireGun1:
            windowSurface.blit(playerStretchedImage1cd, pplayer1)
        if direction1 == 'left' and not fireGun1:
            windowSurface.blit(playerStretchedImage1cl, pplayer1)
        if direction1 == 'right' and not fireGun1:
            windowSurface.blit(playerStretchedImage1cr, pplayer1)
        if direction1 == 'up' and fireGun1:
            windowSurface.blit(playerStretchedImage1ou, pplayer1)
        if direction1 == 'down' and fireGun1:
            windowSurface.blit(playerStretchedImage1od, pplayer1)
        if direction1 == 'left' and fireGun1:
            windowSurface.blit(playerStretchedImage1ol, pplayer1)
        if direction1 == 'right' and fireGun1:
            windowSurface.blit(playerStretchedImage1or, pplayer1)
        pygame.draw.rect(windowSurface, WHITE, (pplayer1.left, pplayer1.top - 10, pplayer1.width, 5))
        pygame.draw.rect(windowSurface, RED, (pplayer1.left, pplayer1.top - 10, HP1*pplayer1.width/player1.width, 5))

        if direction2 == 'up' and not fireGun2:
            windowSurface.blit(playerStretchedImage2cu, pplayer2)
        if direction2 == 'down' and not fireGun2:
            windowSurface.blit(playerStretchedImage2cd, pplayer2)
        if direction2 == 'left' and not fireGun2:
            windowSurface.blit(playerStretchedImage2cl, pplayer2)
        if direction2 == 'right' and not fireGun2:
            windowSurface.blit(playerStretchedImage2cr, pplayer2)
        if direction2 == 'up' and fireGun2:
            windowSurface.blit(playerStretchedImage2ou, pplayer2)
        if direction2 == 'down' and fireGun2:
            windowSurface.blit(playerStretchedImage2od, pplayer2)
        if direction2 == 'left' and fireGun2:
            windowSurface.blit(playerStretchedImage2ol, pplayer2)
        if direction2 == 'right' and fireGun2:
            windowSurface.blit(playerStretchedImage2or, pplayer2)
        pygame.draw.rect(windowSurface, WHITE, (pplayer2.left, pplayer2.top - 10, pplayer2.width, 5))
        pygame.draw.rect(windowSurface, RED, (pplayer2.left, pplayer2.top - 10, HP2*pplayer2.width/player2.width, 5))

        if SKULL1:
            windowSurface.blit(skullStretchedImage1, skull1)
        if SKULL2:
            windowSurface.blit(skullStretchedImage2, skull2)

        if SISE1:
            SISE1_COUNTER += 1
        if SISE1_COUNTER >= SISETIME:
            SISE1 = 0
            SISE1_COUNTER = 0
            SIZE2 -= 30
            pplayer2.left += 15
            pplayer2.top += 15
        if SISE2:
            SISE2_COUNTER += 1
        if SISE2_COUNTER >= SISETIME:
            SISE2 = 0
            SISE2_COUNTER = 0
            SIZE1 -= 30
            pplayer1.left += 15
            pplayer1.top += 15

        if ICE1:
            ICE1_COUNTER += 1
        if ICE1_COUNTER >= ICETIME:
            ICE1 = 0
            ICE1_COUNTER = 0
            MOVESPEED2 = 6
        if ICE2:
            ICE2_COUNTER += 1
        if ICE2_COUNTER >= ICETIME:
            ICE2 = 0
            ICE2_COUNTER = 0
            MOVESPEED1 = 6

        if LASER1:
            LASER1_COUNTER += 1
        if LASER1_COUNTER >= LASERTIME:
            LASER1 = 0
            LASER1_COUNTER = 0
        if LASER2:
            LASER2_COUNTER += 1
        if LASER2_COUNTER >= LASERTIME:
            LASER2 = 0
            LASER2_COUNTER = 0

        if SHIELD1:
            SHIELD1_COUNTER += 1
        if SHIELD1_COUNTER >= SHIELDTIME:
            SHIELD1 = 0
            SHIELD1_COUNTER = 0
        if SHIELD2:
            SHIELD2_COUNTER += 1
        if SHIELD2_COUNTER >= SHIELDTIME:
            SHIELD2 = 0
            SHIELD2_COUNTER = 0

        if TURRET1:
            TURRET1_COUNTER += 1
        if TURRET1_COUNTER >= TURRETTIME:
            TURRET1 = 0
            TURRET1_COUNTER = 0
        if TURRET2:
            TURRET2_COUNTER += 1
        if TURRET2_COUNTER >= TURRETTIME:
            TURRET2 = 0
            TURRET2_COUNTER = 0

        if SKULL1 or SKULL2:
            SKULL_COUNTER += 1
        if SKULL_COUNTER >= SKULLTIME:
            SKULL1 = 0
            SKULL2 = 0
            SKULL_COUNTER = 0
                
        if TURRET1:
            if TURRET_direction1 == 'up':
                windowSurface.blit(turretStretchedImage11, turret1)
            if TURRET_direction1 == 'down':
                windowSurface.blit(turretStretchedImage12, turret1)
            if TURRET_direction1 == 'left':
                windowSurface.blit(turretStretchedImage13, turret1)
            if TURRET_direction1 == 'right':
                windowSurface.blit(turretStretchedImage14, turret1)
            if TURRET1_COUNTER % 15 == 1:
                if TURRET_direction1 == 'up':
                    up1.append(pygame.Rect(turret1.centerx+(50/10)-(BULLETSIZE/2), turret1.top+(50/6)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
                if TURRET_direction1 == 'down':
                    down1.append(pygame.Rect(turret1.centerx+(50/10)-(BULLETSIZE/2), turret1.bottom-(50/6)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
                if TURRET_direction1 == 'left':
                    left1.append(pygame.Rect(turret1.left+(50/6)-(BULLETSIZE/2), turret1.centery+(50/10)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
                if TURRET_direction1 == 'right':
                    right1.append(pygame.Rect(turret1.right-(50/6)-(BULLETSIZE/2), turret1.centery+(50/10)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
        if TURRET2:
            if TURRET_direction2 == 'up':
                windowSurface.blit(turretStretchedImage21, turret2)
            if TURRET_direction2 == 'down':
                windowSurface.blit(turretStretchedImage22, turret2)
            if TURRET_direction2 == 'left':
                windowSurface.blit(turretStretchedImage23, turret2)
            if TURRET_direction2 == 'right':
                windowSurface.blit(turretStretchedImage24, turret2)
            if TURRET2_COUNTER % 15 == 1:
                if TURRET_direction2 == 'up':
                    up2.append(pygame.Rect(turret2.centerx+(50/10)-(BULLETSIZE/2), turret2.top+(50/6)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
                if TURRET_direction2 == 'down':
                    down2.append(pygame.Rect(turret2.centerx+(50/10)-(BULLETSIZE/2), turret2.bottom-(50/6)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
                if TURRET_direction2 == 'left':
                    left2.append(pygame.Rect(turret2.left+(50/6)-(BULLETSIZE/2), turret2.centery+(50/10)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
                if TURRET_direction2 == 'right':
                    right2.append(pygame.Rect(turret2.right-(50/6)-(BULLETSIZE/2), turret2.centery+(50/10)-(BULLETSIZE/2), BULLETSIZE, BULLETSIZE))
        
        # draw the bullet
        for i in range(len(up1)):
            if not ICE1:
                windowSurface.blit(bulletStretchedImage11, up1[i])
            if ICE1:
                windowSurface.blit(bulletStretchedImagei, up1[i])
        for i in range(len(down1)):
            if not ICE1:
                windowSurface.blit(bulletStretchedImage12, down1[i])
            if ICE1:
                windowSurface.blit(bulletStretchedImagei, down1[i])
        for i in range(len(left1)):
            if not ICE1:
                windowSurface.blit(bulletStretchedImage13, left1[i])
            if ICE1:
                windowSurface.blit(bulletStretchedImagei, left1[i])
        for i in range(len(right1)):
            if not ICE1:
                windowSurface.blit(bulletStretchedImage14, right1[i])
            if ICE1:
                windowSurface.blit(bulletStretchedImagei, right1[i])
        for i in range(len(up2)):
            if not ICE2:
                windowSurface.blit(bulletStretchedImage21, up2[i])
            if ICE2:
                windowSurface.blit(bulletStretchedImagei, up2[i])
        for i in range(len(down2)):
            if not ICE2:
                windowSurface.blit(bulletStretchedImage22, down2[i])
            if ICE2:
                windowSurface.blit(bulletStretchedImagei, down2[i])
        for i in range(len(left2)):
            if not ICE2:
                windowSurface.blit(bulletStretchedImage23, left2[i])
            if ICE2:
                windowSurface.blit(bulletStretchedImagei, left2[i])
        for i in range(len(right2)):
            if not ICE2:
                windowSurface.blit(bulletStretchedImage24, right2[i])
            if ICE2:
                windowSurface.blit(bulletStretchedImagei, right2[i])

        for i in range(len(up1crash)):
            if up1c[i] < 10:
                windowSurface.blit(bulletStretchedImagec21, up1crash[i])
                up1c[i] += 1
            if up1c[i] == 0:
                up1c.remove(i)
                up1crash.remove(i)
        for i in range(len(down1crash)):
            if down1c[i] < 10:
                windowSurface.blit(bulletStretchedImagec22, down1crash[i])
                down1c[i] += 1
            if down1c[i] == 0:
                down1c.remove(i)
                down1crash.remove(i)
        for i in range(len(left1crash)):
            if left1c[i] < 10:
                windowSurface.blit(bulletStretchedImagec23, left1crash[i])
                left1c[i] += 1
            if left1c[i] == 0:
                left1c.remove(i)
                left1crash.remove(i)
        for i in range(len(right1crash)):
            if right1c[i] < 10:
                windowSurface.blit(bulletStretchedImagec24, right1crash[i])
                right1c[i] += 1
            if right1c[i] == 0:
                right1c.remove(i)
                right1crash.remove(i)

        for i in range(len(up2crash)):
            if up2c[i] < 10:
                windowSurface.blit(bulletStretchedImagec21, up2crash[i])
                up2c[i] += 1
            if up2c[i] == 0:
                up2c.remove(i)
                up2crash.remove(i)
        for i in range(len(down2crash)):
            if down2c[i] < 10:
                windowSurface.blit(bulletStretchedImagec22, down2crash[i])
                down2c[i] += 1
            if down2c[i] == 0:
                down2c.remove(i)
                down2crash.remove(i)
        for i in range(len(left2crash)):
            if left2c[i] < 10:
                windowSurface.blit(bulletStretchedImagec23, left2crash[i])
                left2c[i] += 1
            if left2c[i] == 0:
                left2c.remove(i)
                left2crash.remove(i)
        for i in range(len(right2crash)):
            if right2c[i] < 10:
                windowSurface.blit(bulletStretchedImagec24, right2crash[i])
                right2c[i] += 1
            if right2c[i] == 0:
                right2c.remove(i)
                right2crash.remove(i)

        textScore = basicFont1.render('%d : %d'%(ascore,bscore), True, WHITE)    
        textScoreRect = textScore.get_rect()
        textScoreRect.centery = 30
        textScoreRect.centerx = int(WINDOWWIDTH/2)
        windowSurface.blit(textScore, textScoreRect)
        
        for i in ITEM0[:]:
            if pplayer1.colliderect(i) and not pplayer2.colliderect(i):
                SIZE2 += 30
                if pplayer2.top>15 and pplayer2.bottom<WINDOWHEIGHT-15:
                    pplayer2.top -= 15
                if pplayer2.bottom>WINDOWHEIGHT-15:
                    pplayer2.bottom -= 30
                if pplayer2.left>15 and pplayer2.right<WINDOWWIDTH-15:
                    pplayer2.left -= 15
                if pplayer2.right>WINDOWWIDTH-15:
                    pplayer2.left -= 30
                ITEM0.remove(i)
                SISE1 = 1
            if pplayer2.colliderect(i) and not pplayer1.colliderect(i):
                SIZE1 += 30
                if pplayer1.top>15 and pplayer1.bottom<WINDOWHEIGHT-15:
                    pplayer1.top -= 15
                if pplayer1.bottom>WINDOWHEIGHT-15:
                    pplayer1.bottom -= 30
                if pplayer1.left>15 and pplayer1.right<WINDOWWIDTH-15:
                    pplayer1.left -= 15
                if pplayer1.right>WINDOWWIDTH-15:
                    pplayer1.left -= 30
                ITEM0.remove(i)
                SISE2 = 1
            if pplayer1.colliderect(i) and pplayer2.colliderect(i):
                SIZE1 += 30
                SIZE2 += 30
                if pplayer2.top>15 and pplayer2.bottom<WINDOWHEIGHT-15:
                    pplayer2.top -= 15
                if pplayer2.bottom>WINDOWHEIGHT-15:
                    pplayer2.bottom -= 30
                if pplayer2.left>15 and pplayer2.right<WINDOWWIDTH-15:
                    pplayer2.left -= 15
                if pplayer2.right>WINDOWWIDTH-15:
                    pplayer2.left -= 30
                if pplayer1.top>15 and pplayer1.bottom<WINDOWHEIGHT-15:
                    pplayer1.top -= 15
                if pplayer1.bottom>WINDOWHEIGHT-15:
                    pplayer1.bottom -= 30
                if pplayer1.left>15 and pplayer1.right<WINDOWWIDTH-15:
                    pplayer1.left -= 15
                if pplayer1.right>WINDOWWIDTH-15:
                    pplayer1.left -= 30
                ITEM0.remove(i)
                SISE1 = 1
                SISE2 = 1
        for i in ITEM1[:]:
            if pplayer1.colliderect(i) and not pplayer2.colliderect(i):
                ICE1 = 1
                ITEM1.remove(i)
            if pplayer2.colliderect(i) and not pplayer1.colliderect(i):
                ICE2 = 1
                ITEM1.remove(i)
            if pplayer1.colliderect(i) and pplayer2.colliderect(i):
                ICE1 = 1
                ICE2 = 1
                ITEM1.remove(i)
        for i in ITEM2[:]:
            if pplayer1.colliderect(i) and not pplayer2.colliderect(i):
                LASER1 = 1
                ITEM2.remove(i)
            if pplayer2.colliderect(i) and not pplayer1.colliderect(i):
                LASER2 = 1
                ITEM2.remove(i)
            if pplayer1.colliderect(i) and pplayer2.colliderect(i):
                LASER1 = 1
                LASER2 = 1
                ITEM2.remove(i)
        for i in ITEM3[:]:
            if pplayer1.colliderect(i) and not pplayer2.colliderect(i):
                SHIELD1 = 1
                pplayer1.top = random.randint(pplayer2.top-100, pplayer2.bottom+50)
                pplayer1.left = random.randint(pplayer2.left-100, pplayer2.right+50)
                ITEM3.remove(i)
            if pplayer2.colliderect(i) and not pplayer1.colliderect(i):
                SHIELD2 = 1
                pplayer2.top = random.randint(pplayer1.top-100, pplayer1.bottom+50)
                pplayer2.left = random.randint(pplayer1.left-100, pplayer1.right+50)
                ITEM3.remove(i)
            if pplayer1.colliderect(i) and pplayer2.colliderect(i):
                SHIELD1 = 1
                SHIELD2 = 1
                pplayer1.top = random.randint(0, WINDOWHEIGHT - pplayer1.height)
                pplayer1.left = random.randint(0, WINDOWWIDTH - pplayer1.width)
                pplayer2.top = random.randint(0, WINDOWHEIGHT - pplayer1.height)
                pplayer2.left = random.randint(0, WINDOWWIDTH - pplayer1.width)
                ITEM3.remove(i)
        for i in ITEM4[:]:
            if pplayer1.colliderect(i) and not pplayer2.colliderect(i):
                TURRET1 = 1
                TURRET1_COUNTER = 0
                TURRET_direction1 = direction1
                turret1.left = i.left
                turret1.top = i.top
                ITEM4.remove(i)
            if pplayer2.colliderect(i) and not pplayer1.colliderect(i):
                TURRET2 = 1
                TURRET2_COUNTER = 0
                TURRET_direction2= direction2
                turret2.left = i.left
                turret2.top = i.top
                ITEM4.remove(i)
            if pplayer1.colliderect(i) and pplayer2.colliderect(i):
                TURRET1 = 1
                TURRET2 = 1
                TURRET1_COUNTER = 0
                TURRET2_COUNTER = 0
                TURRET_direction1 = direction1
                TURRET_direction2 = direction2
                turret1.left = i.left
                turret1.top = i.top
                turret2.left = i.left
                turret2.top = i.top
                ITEM4.remove(i)
        for i in ITEM5[:]:
            if pplayer1.colliderect(i) and not pplayer2.colliderect(i):
                if HP1 < player1.width:
                    HP1 += 10
                ITEM5.remove(i)
            if pplayer2.colliderect(i) and not pplayer1.colliderect(i):
                if HP2 < player2.width:
                    HP2 += 10
                ITEM5.remove(i)
            if pplayer1.colliderect(i) and pplayer2.colliderect(i):
                if HP1 < player1.width:
                    HP1 += 10
                if HP2 < player2.width:
                    HP2 += 10
                ITEM5.remove(i)
        for i in ITEM6[:]:
            if pplayer1.colliderect(i) and not pplayer2.colliderect(i):
                SKULL2 = 1
                ITEM6.remove(i)
            if pplayer2.colliderect(i) and not pplayer1.colliderect(i):
                SKULL1 = 1
                ITEM6.remove(i)
            if pplayer1.colliderect(i) and pplayer2.colliderect(i):
                SKULL1 = 1
                SKULL2 = 1
                ITEM6.remove(i)
        for i in ITEM7[:]:
            if pplayer1.colliderect(i) and not pplayer2.colliderect(i):
                MINE1.append(pygame.Rect(i.left, i.top, ITEMSIZE, ITEMSIZE))
                ITEM7.remove(i)
            if pplayer2.colliderect(i) and not pplayer1.colliderect(i):
                MINE2.append(pygame.Rect(i.left, i.top, ITEMSIZE, ITEMSIZE))
                ITEM7.remove(i)
            if pplayer1.colliderect(i) and pplayer2.colliderect(i):
                MINE1.append(pygame.Rect(i.left, i.top, ITEMSIZE, ITEMSIZE))
                MINE2.append(pygame.Rect(i.left, i.top, ITEMSIZE, ITEMSIZE))
                ITEM7.remove(i)

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
        if mousey > startbutton.top and mousey < startbutton.bottom and mousex > textRect.left and mousex < textRect.right:
            GAMEEND = 0
            RESTART = 1
            GAMESTART = 1

        # draw the window onto the screen
        pygame.display.update()
        mainClock.tick(SPEED)

    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(SPEED)
# ITEM: 0:상대 커짐, 1:아이스 총알, 2:레이저, 3:순간이동, 4:포탑, 5:회복, 6:해골, 7:지뢰
