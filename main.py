### Building a Game - Culminating Activity ###
### U.F.O Conqueror: by John Brennan ###



### Background ###
app.background = 'black'




### Title Screen ###



titlelabel1 = Label('U.F.O', 200, 75, fill='white', size= 45, font='monospace', visible=True)
    
titlelabel2 = Label('Conqueror', 200, 133, fill='white', size= 45, font='monospace', visible=True)
    
titlelabel3 = Label('U.F.O', 200, 80, fill='magenta', size= 45, font='monospace', visible=True)
    
titlelabel4 = Label('Conqueror', 200, 130, fill='magenta', size= 45, font='monospace', visible=True)
    
    
    
newGameTitle = Label('New game', 200, 220, font='monospace', fill='magenta', size=26, visible=True)
helpGameTitle = Label('Controls', 200, 255, font='monospace', fill='magenta', size=26, visible=True)
quitGameTitle = Label('Quit', 200, 290, font='monospace', fill='magenta', size=26, visible=True)
    
    
animationarrow1 = Line(120, 220, 122, 220, arrowEnd=True, fill='White', visible=True)
animationarrow2 = Line(279, 221, 277, 221, arrowEnd=True, fill='White', visible=True)



ufo = Group(Circle(329, 80, 10, fill='white', border='lime'), 
    Rect(311.5, 80, 35, 2, fill='lime'), 
    Line(312, 80, 329, 97, fill='lime'), 
    Line(347, 80, 329, 97, fill='lime'), 
    Star(312, 80, 5, 3, fill='lime'),
    Star(347, 80, 5, 3, fill='lime'),
    Star(329, 97, 5, 3, fill='lime'))
    


stageEarthShip = Group(Line(61, 318, 61, 345, fill='white', lineWidth=3), 
        Rect(40, 341, 40, 4, fill='white'), 
        Line(40, 345, 40, 333, fill='cyan'), 
        Line(80, 345, 80, 333, fill='cyan'), 
        Rect(46, 337, 29, 11, fill='white', border='cyan'),
        Rect(59, 345, 5, 7, fill='white'),
        Line(47, 337, 47, 328, fill='cyan'), 
        Line(74, 340, 74, 328, fill='cyan'),
        Star(61, 335, 10, 3, fill='white'))

stageEarthShip.visible = False



### Game Components ###



star = Group(Circle(200, 150, 2, fill='white'), Star(53, 112, 3, 4, fill='white'), Circle(314, 35, 2, fill='white'), Circle(246, 388, 2, fill='white'), 
    Circle(366, 364, 2, fill='white'), Circle(114, 219, 2, fill='white'), Circle(170, 350, 2, fill='white'), Circle(262, 5, 2, fill='white'), Circle(204, 390, 2, fill='white'),
     Circle(377, 19, 2, fill='white'), Circle(40, 360, 2, fill='white'), Circle(108, 150, 2, fill='white'), Circle(110, 1, 2, fill='white'), Circle(375, 389, 2, fill='white'))
     
     
star2 = Group(Circle(200, 150, 2, fill='white'), Star(53, 112, 3, 4, fill='white'), Circle(314, 35, 2, fill='white'), Circle(246, 388, 2, fill='white'), 
    Circle(366, 364, 2, fill='white'), Circle(114, 219, 2, fill='white'), Circle(170, 350, 2, fill='white'), Circle(262, 5, 2, fill='white'), Circle(204, 390, 2, fill='white'),
     Circle(377, 19, 2, fill='white'), Circle(40, 360, 2, fill='white'), Circle(108, 150, 2, fill='white'), Circle(110, 1, 2, fill='white'), Circle(375, 389, 2, fill='white'), 
     Circle(333, 234, 2, fill='white'), Circle(335, 169, 2, fill='white'), Circle(348, 371, 2, fill='white'), Circle(315, 187, 2, fill='white'))
     
     
star3 = Group(Circle(200, 150, 2, fill='white'), Star(53, 112, 3, 4, fill='white'), Circle(314, 35, 2, fill='white'), Circle(246, 388, 2, fill='white'), 
    Circle(366, 364, 2, fill='white'), Circle(114, 219, 2, fill='white'), Circle(170, 350, 2, fill='white'), Circle(262, 5, 2, fill='white'), Circle(204, 390, 2, fill='white'),
     Circle(377, 19, 2, fill='white'), Circle(40, 360, 2, fill='white'), Circle(108, 150, 2, fill='white'), Circle(110, 1, 2, fill='white'), Circle(375, 389, 2, fill='white'), 
     Circle(333, 234, 2, fill='white'), Circle(335, 169, 2, fill='white'), Circle(348, 371, 2, fill='white'), Circle(315, 187, 2, fill='white'))



ufo2 = Group(Circle(329, 80, 10, fill='white', border='lime', visible = False), 
    Rect(311.5, 80, 35, 2, fill='lime', visible = False), 
    Line(312, 80, 329, 97, fill='lime', visible = False), 
    Line(347, 80, 329, 97, fill='lime', visible = False), 
    Star(312, 80, 5, 3, fill='lime', visible = False),
    Star(347, 80, 5, 3, fill='lime', visible = False),
    Star(329, 97, 5, 3, fill='lime', visible = False))
    
ufo2.visible = False
ufo2.centerX = 80
ufo2.centerY = 30

    
ufo3 = Group(Circle(329, 80, 10, fill='white', border='lime', visible = False), 
    Rect(311.5, 80, 35, 2, fill='lime', visible = False), 
    Line(312, 80, 329, 97, fill='lime', visible = False), 
    Line(347, 80, 329, 97, fill='lime', visible = False), 
    Star(312, 80, 5, 3, fill='lime', visible = False),
    Star(347, 80, 5, 3, fill='lime', visible = False),
    Star(329, 97, 5, 3, fill='lime', visible = False))
    
ufo3.visible = False
ufo3.centerX = 320
ufo3.centerY = 30
    
    
ufo4 = Group(Circle(329, 80, 10, fill='white', border='lime', visible = False), 
    Rect(311.5, 80, 35, 2, fill='lime', visible = False), 
    Line(312, 80, 329, 97, fill='lime', visible = False), 
    Line(347, 80, 329, 97, fill='lime', visible = False), 
    Star(312, 80, 5, 3, fill='lime', visible = False),
    Star(347, 80, 5, 3, fill='lime', visible = False),
    Star(329, 97, 5, 3, fill='lime', visible = False))
    
ufo4.visible = False
ufo4.centerX = 200
ufo4.centerY = 100



star.dy = 15
star2.dy = 5
star3.dy = 10
ufo2.dx = 3
ufo3.dx = 3
ufo4.dx = 3



laserBeam = Line(200, 370, 200, 310, fill='cyan', lineWidth= 3)


EarthShip = Group(Line(61, 318, 61, 345, fill='white', lineWidth=3), 
        Rect(40, 341, 40, 4, fill='white'), 
        Line(40, 345, 40, 333, fill='cyan'), 
        Line(80, 345, 80, 333, fill='cyan'), 
        Rect(46, 337, 29, 11, fill='white', border='cyan'),
        Rect(59, 345, 5, 7, fill='white'),
        Line(47, 337, 47, 328, fill='cyan'), 
        Line(74, 340, 74, 328, fill='cyan'),
        Star(61, 335, 10, 3, fill='white'))
        
EarthShip.centerX = 200
EarthShip.centerY = 360


EarthShip.dx = 5 # move right to start


ufoBlasterShot = Line(80, 45, 80, 59, fill='crimson', lineWidth=3, visible = False)
ufoBlasterShot2 = Line(80, 45, 80, 59, fill='crimson', lineWidth=3, visible = False)
ufoBlasterShot3 = Line(80, 45, 80, 59, fill='crimson', lineWidth=3, visible = False)

gameStartCounter = Label(0, 0, 0, fill=None)



bossBlasterShot = Line(80, 45, 80, 59, fill='magenta', lineWidth=3, visible = False)
bossBlasterShot2 = Line(80, 45, 80, 59, fill='magenta', lineWidth=3, visible = False)
bossBlasterShot3 = Line(80, 45, 80, 59, fill='magenta', lineWidth=3, visible = False)



stageBoss = Group(RegularPolygon(329, 75, 15, 4, fill='white', border='red', visible = False), 
    Rect(310, 80, 40, 2, fill='red', visible = False), 
    Line(312, 80, 329, 97, fill='red', visible = False), 
    Line(347, 80, 329, 97, fill='red', visible = False), 
    Star(312, 80, 5, 3, fill='red', visible = False),
    Star(347, 80, 5, 3, fill='red', visible = False),
    RegularPolygon(313, 85, 10, 3, fill='white', border='red', visible = False),
    RegularPolygon(346, 85, 10, 3, fill='white', border='red', visible = False),
    Star(329, 97, 6, 3, fill='red', visible = False))

stageBoss.visible = True
stageBoss.centerX = 65
stageBoss.centerY = 65



boss = Group(RegularPolygon(329, 75, 15, 4, fill='white', border='red', visible = False), 
    Rect(310, 80, 40, 2, fill='red', visible = False), 
    Line(312, 80, 329, 97, fill='red', visible = False), 
    Line(347, 80, 329, 97, fill='red', visible = False), 
    Star(312, 80, 5, 3, fill='red', visible = False),
    Star(347, 80, 5, 3, fill='red', visible = False),
    RegularPolygon(313, 85, 10, 3, fill='white', border='red', visible = False),
    RegularPolygon(346, 85, 10, 3, fill='white', border='red', visible = False),
    Star(329, 97, 6, 3, fill='red', visible = False))
    
    
boss.visible = False
boss.centerX = 200
boss.centerY = -50
boss.dx = 5

#Counter to flush out the Boss
bossCounter = Label(0, 200, 200, fill=None)
bossReturnCounter = Label(1, 200, 200, fill=None)


#Health
playerHealthLabel = Label('Health:', 122, 385, fill='cyan', font='monoSpace', size=15, visible = False, bold=True)
playerHealth = Label(10, 166, 385, fill='cyan', font='monoSpace', size=15, visible = False, bold=True)
healthCounter = Label(0, 200, 200, fill=None)

# Number Seperator
seperator1 = Line(190, 378, 190, 395, fill='magenta', lineWidth = 2, visible = False)
seperator2 = Line(210, 378, 210, 395, fill='magenta', lineWidth = 2, visible = False)
seperator3 = Line(73, 378, 73, 395, fill='magenta', lineWidth = 2, visible = False)
seperator4 = Line(340, 378, 340, 395, fill='magenta', lineWidth = 2, visible = False)


#Point Algorithm
pointLabel = Label('Points:', 250, 385, fill='cyan', font='monoSpace', size=15, visible = False, bold=True)
pointTitle = Label(0, 315, 385, fill='cyan', font='monoSpace', size=15, visible = False, bold=True)
pointCounter = Label(0, 200, 200, fill=None)

# Booster and Speed power ups
boosterFrame = Rect(18, 376, 43, 20, fill=None, border='cyan', visible = False)
speedFrame = Rect(350, 376, 43, 20, fill=None, border='cyan', visible = False)
boosterTitle = Label('Boost',40, 385, fill='magenta', font='monospace', bold = True, size=12, visible = False)
speedTitle = Label('Speed', 372, 385, fill='magenta', font='monospace', bold = True, size=12, visible = False)


#Point System 
moneyBoosterCounter = Label(10, 200, 200, fill=None)
moneySpeedCounter = Label(0, 200, 200, fill=None)

#author Variable
author = Group(Label('John Brennan', 200, 385, fill='magenta', size= 20, font='monospace', visible=True, bold=True),
    Label('John Brennan', 200, 383, fill='white', size= 20, font='monospace', visible=True, bold=True))
 



### Game Start ###

def gameStart():
    author.visible = False
    pointLabel.visible = True
    pointTitle.visible = True
    titlelabel1.visible = False
    titlelabel2.visible = False 
    titlelabel3.visible = False 
    titlelabel4.visible = False 
    newGameTitle.visible = False 
    helpGameTitle.visible = False 
    quitGameTitle.visible = False
    animationarrow1.visible = False
    animationarrow2.visible = False
    ufo.visible = False
    ufo2.visible = True
    ufo3.visible = True
    ufo4.visible = True
    stageEarthShip.visible = False
    ufoBlasterShot.visible = False
    ufoBlasterShot2.visible = False
    ufoBlasterShot3.visible = False
    gameStartCounter.value += 1
    playerHealthLabel.visible = True
    playerHealth.visible = True
    healthCounter.value += 1
    EarthShip.visible = True
    laserBeam.visible = True
    loseScreen1.visible = False
    loseScreen2.visible = False
    loseScreen3.visible = False
    loseScreen4.visible = False
    helpScreen1.visible = False
    helpScreen2.visible = False
    helpScreen3.visible = False 
    helpScreen4.visible = False
    wbox.visible = False
    sbox.visible = False
    abox.visible = False
    dbox.visible = False
    vbox.visible = False
    wlabel.visible = False 
    slabel.visible = False
    alabel.visible = False
    dlabel.visible = False
    vlabel.visible = False
    bossBlasterShot.visible = False 
    bossBlasterShot2.visible = False 
    bossBlasterShot3.visible = False
    stageBoss.visible = False
    seperator1.visible = True
    seperator2.visible = True
    seperator3.visible = True 
    seperator4.visible = True
    boosterFrame.visible = True 
    speedFrame.visible = True 
    boosterTitle.visible = True 
    speedTitle.visible = True
    seperator1.visible = True
    seperator2.visible = True
    seperator3.visible = True
    seperator4.visible = True


#Counter so the Earth Ship can move forward
pushCounter = Label(0, 200, 200, fill=None)


### Help Screen ###

helpScreen1 = RegularPolygon(200, 200, 150, 6, fill='turquoise', visible = False)
helpScreen2 = RegularPolygon(200, 200, 170, 6, fill=None, border='turquoise', borderWidth = 4, visible = False)
helpScreen3 = Label("Controls:", 200, 120, size=25, font='monospace', visible = False, fill='white', bold=True)
helpScreen4 = Label("Press 'm' to return to Menu", 200, 275, size=12, font='monospace', visible = False, fill='white', bold=True)
wbox = Rect(145, 165, 35, 35, fill=None, border='white', visible = False)
sbox = Rect(145, 210, 35, 35, fill=None, border='white', visible = False)
abox = Rect(100, 210, 35, 35, fill=None, border='white', visible = False)
dbox = Rect(190, 210, 35, 35, fill=None, border='white', visible = False)
vbox = Rect(250, 185, 35, 35, fill=None, border='white', visible = False)
wlabel = Label('W',162, 183, fill='white', font='monospace', bold = True, size=30, visible = False)
slabel = Label('S',162, 228, fill='white', font='monospace', bold = True, size=30, visible = False) 
alabel = Label('A',118, 228, fill='white', font='monospace', bold = True, size=30, visible = False)
dlabel = Label('D',207, 228, fill='white', font='monospace', bold = True, size=30, visible = False)
vlabel = Label('V',267, 202, fill='white', font='monospace', bold = True, size=30, visible = False)



def helpScreen():
    author.visible = True
    EarthShip.visible = False
    laserBeam.visible = False
    titlelabel1.visible = False
    titlelabel2.visible = False 
    titlelabel3.visible = False 
    titlelabel4.visible = False 
    newGameTitle.visible = False 
    helpGameTitle.visible = False 
    quitGameTitle.visible = False
    animationarrow1.visible = False
    animationarrow2.visible = False
    ufo.visible = False
    ufo2.visible = False
    ufo3.visible = False
    ufo4.visible = False
    stageEarthShip.visible = False
    ufoBlasterShot.visible = False
    ufoBlasterShot2.visible = False
    ufoBlasterShot3.visible = False
    playerHealthLabel.visible = False
    playerHealth.visible = False
    helpScreen1.visible = True
    helpScreen2.visible = True
    helpScreen3.visible = True
    helpScreen3.visible = True
    wbox.visible = True
    sbox.visible = True
    abox.visible = True
    dbox.visible = True
    vbox.visible = True
    wlabel.visible = True 
    slabel.visible = True
    alabel.visible = True
    dlabel.visible = True
    vlabel.visible = True
    helpScreen4.visible = True
    stageBoss.visible = False
    seperator1.visible = False
    seperator2.visible = False
    seperator3.visible = False
    seperator4.visible = False
    
    


### Menu Return Function ###

def menu():
    author.visible = True
    EarthShip.visible = True
    laserBeam.visible = False
    titlelabel1.visible = True
    titlelabel2.visible = True 
    titlelabel3.visible = True 
    titlelabel4.visible = True 
    newGameTitle.visible = True 
    helpGameTitle.visible = True 
    quitGameTitle.visible = True
    animationarrow1.visible = True
    animationarrow2.visible = True
    ufo.visible = True
    ufo2.visible = False
    ufo3.visible = False
    ufo4.visible = False
    stageEarthShip.visible = False
    ufoBlasterShot.visible = False
    ufoBlasterShot2.visible = False
    ufoBlasterShot3.visible = False
    playerHealthLabel.visible = False
    playerHealth.visible = False
    helpScreen1.visible = False
    helpScreen2.visible = False
    helpScreen3.visible = False
    helpScreen4.visible = False
    wbox.visible = False
    sbox.visible = False
    abox.visible = False
    dbox.visible = False
    vbox.visible = False
    wlabel.visible = False 
    slabel.visible = False
    alabel.visible = False
    dlabel.visible = False
    vlabel.visible = False
    stageBoss.visible = True
    boosterFrame.visible = True 
    speedFrame.visible = True 
    boosterTitle.visible = True 
    speedTitle.visible = True
    boosterFrame.visible = False
    speedFrame.visible = False 
    boosterTitle.visible = False 
    speedTitle.visible = False
    seperator1.visible = False
    seperator2.visible = False
    seperator3.visible = False
    seperator4.visible = False 



### On-Step Functions ###


animationCounter = Label(0, 0, 0)



def onStep():

    laserBeam.centerX = EarthShip.centerX 
    ufoBlasterShot.centerX = ufo2.centerX
    
    bossBlasterShot.centerX = boss.centerX
    bossBlasterShot2.centerX = boss.centerX
    bossBlasterShot3.centerX = boss.centerX
    
    app.stepspersecond = 1
    animationCounter.value += 1
    if (animationCounter.value % 2) == 1:
        animationarrow1.fill = 'magenta'
        animationarrow2.fill = 'magenta'


    
    else: 
        animationarrow1.fill = 'white'
        animationarrow2.fill = 'white'



    ##Animation on The Start Screen ### 
    ufo.rotateAngle += 3
    stageEarthShip.rotateAngle -= 3
    
    
    #Boss animation on the start Screen
    stageBoss.rotateAngle -= 3


    
    star.centerY += star.dy
    
    if (star.top > 400):
        star.bottom = 0
        
    
    star2.centerY += star2.dy
    
    if (star2.top > 400):
        star2.bottom = 0


    star3.centerY += star3.dy
    
    if (star3.top > 400):
        star3.bottom = 0
        

        
    ufo2.centerX += ufo2.dx
    if ((ufo2.left < 0) or (ufo2.right > 400)):
        ufo2.dx = -ufo2.dx
            
            
    ufo3.centerX += ufo3.dx
    if ((ufo3.left < 0) or (ufo3.right > 400)):
        ufo3.dx = -ufo3.dx
            
            
    ufo4.centerX += ufo4.dx
    if ((ufo4.left < 0) or (ufo4.right > 400)):
        ufo4.dx = -ufo4.dx
        
        
        
        
    #Boss moving back and forth
    if boss.centerY > 100:
        boss.centerX += boss.dx
        if ((boss.left < 0) or (boss.right > 400)):
            boss.dx = -boss.dx
            

    
    
    EarthShip.centerX += EarthShip.dx
    
    if ((EarthShip.left < 0) or (EarthShip.right > 400)):
        # we went off the left edge or the right edge,
        # so reverse our direction ('bounce')
        EarthShip.dx = -EarthShip.dx
    
    
    
    
    ufoBlasterShot.dy = 13
    ufoBlasterShot.centerX = ufo2.centerX
    if ufoBlasterShot.centerY < 65:
        ufoBlasterShot.visible = False
        ufoBlasterShot.centerX = ufo2.centerX
        
    if ufoBlasterShot.centerY > 70 and gameStartCounter.value == 1:
        ufoBlasterShot.visible = True
        
    ufoBlasterShot.centerY += ufoBlasterShot.dy
        
    if (ufoBlasterShot.top > 400):
        ufoBlasterShot.bottom = 55




    ufoBlasterShot2.dy = 13
    ufoBlasterShot2.centerX = ufo3.centerX
    if ufoBlasterShot2.centerY < 65:
        ufoBlasterShot2.visible = False
        ufoBlasterShot2.centerX = ufo3.centerX
        
    if ufoBlasterShot2.centerY > 70 and gameStartCounter.value == 1:
        ufoBlasterShot2.visible = True
        
    ufoBlasterShot2.centerY += ufoBlasterShot2.dy
        
    if (ufoBlasterShot2.top > 400):
        ufoBlasterShot2.bottom = 55
        
    
    
    ufoBlasterShot3.dy = 13
    ufoBlasterShot3.centerX = ufo4.centerX
    if ufoBlasterShot3.centerY < 45:
        ufoBlasterShot3.visible = False
        ufoBlasterShot3.centerX = ufo4.centerX
        
    if ufoBlasterShot3.centerY > 45 and gameStartCounter.value == 1:
        ufoBlasterShot3.visible = True
        
    ufoBlasterShot3.centerY += ufoBlasterShot3.dy
        
    if (ufoBlasterShot3.top > 400):
        ufoBlasterShot3.bottom = 95
        
    
    
    #Boss blasting projectiles
    bossBlasterShot.dy = 10
        
    if bossBlasterShot.centerY < 85:
        bossBlasterShot.visible = False
        bossBlasterShot.centerX = boss.centerX
        
    if bossBlasterShot.centerY > 85 and bossCounter.value == 1:
        bossBlasterShot.visible = True
        
    bossBlasterShot.centerY += bossBlasterShot.dy
        
    if (bossBlasterShot.top > 400):
        bossBlasterShot.bottom = 85
        
        
    
    bossBlasterShot2.dy = 13
        
    if bossBlasterShot2.centerY < 85:
        bossBlasterShot2.visible = False
        bossBlasterShot2.centerX = boss.centerX
        
    if bossBlasterShot2.centerY > 85 and bossCounter.value == 1:
        bossBlasterShot2.visible = True
        
    bossBlasterShot2.centerY += bossBlasterShot2.dy
        
    if (bossBlasterShot2.top > 400):
        bossBlasterShot2.bottom = 85
        
        
        
    bossBlasterShot3.dy = 17
        
    if bossBlasterShot3.centerY < 85:
        bossBlasterShot3.visible = False
        bossBlasterShot3.centerX = boss.centerX
        
    if bossBlasterShot3.centerY > 85 and bossCounter.value == 1:
        bossBlasterShot3.visible = True
        
    bossBlasterShot3.centerY += bossBlasterShot3.dy
        
    if (bossBlasterShot3.top > 400):
        bossBlasterShot3.bottom = 85
    
    
    

    if laserBeam.height > 15:
        laserBeam.y2 += 25
        
    if laserBeam.height < 7:
        laserBeam.visible = False
        
        
        
    #Laser Beam damaging the Ufo 
    if (ufo2.hitsShape(laserBeam) == True):
        if ufo2.opacity > 10:
            ufo2.opacity -= 0.75
            
    if (ufo3.hitsShape(laserBeam) == True):
        if ufo3.opacity > 10:
            ufo3.opacity -= 0.75
            
    if (ufo4.hitsShape(laserBeam) == True):
        if ufo4.opacity > 10:
            ufo4.opacity -= 0.75


    #Laser Beam damaging the Boss
    if (boss.hitsShape(laserBeam) == True):
        if boss.opacity > 10:
            boss.opacity -= 2
        

    # Ufo Blaster Shots damaging the Earth Ship
    if (EarthShip.hitsShape(ufoBlasterShot) == True) and healthCounter.value == 1 and ufo2.visible == True: 
        if playerHealth.value >= 1:
            playerHealth.value -= 1
    

    if (EarthShip.hitsShape(ufoBlasterShot2) == True) and healthCounter.value == 1 and ufo3.visible == True: 
        if playerHealth.value >= 1:
            playerHealth.value -= 1
            
            
    if (EarthShip.hitsShape(ufoBlasterShot3) == True) and healthCounter.value == 1 and ufo4.visible == True: 
        if playerHealth.value >= 1:
            playerHealth.value -= 1
            
            
    # Boss Blaster Shots damaging the Earth Ship
    if (EarthShip.hitsShape(bossBlasterShot) == True) and healthCounter.value == 1 and boss.visible == True: 
        if playerHealth.value >= 1:
            playerHealth.value -= 1
    

    if (EarthShip.hitsShape(bossBlasterShot2) == True) and healthCounter.value == 1 and boss.visible == True: 
        if playerHealth.value >= 1:
            playerHealth.value -= 1
            
            
    if (EarthShip.hitsShape(bossBlasterShot3) == True) and healthCounter.value == 1 and boss.visible == True: 
        if playerHealth.value >= 1:
            playerHealth.value -= 1    
        
            
    #Ufo being Destroyed and disabling attack
    if ufo2.opacity <= 12:
        ufo2.visible = False
        ufoBlasterShot.visible = False
        
        
    if ufo3.opacity <= 12:
        ufo3.visible = False
        ufoBlasterShot2.visible = False
        
    if ufo4.opacity <= 12:
        ufo4.visible = False
        ufoBlasterShot3.visible = False
        

    # Health of Ship
    if playerHealth.value <= 8 and playerHealth.value > 6:
        playerHealthLabel.fill = 'yellow'
        playerHealth.fill = 'yellow'
        
        
    elif playerHealth.value <= 5 and playerHealth.value > 3:
        playerHealthLabel.fill = 'darkOrange' 
        playerHealth.fill = 'darkOrange'
        
        
    elif playerHealth.value <= 3 and playerHealth.value > 1:
        playerHealthLabel.fill = 'red'
        playerHealth.fill = 'red'
        
        
    elif playerHealth.value == 0:
        loseScreen()
        
        
    if boss.opacity <= 11:
        winScreen()
    
        
        
    if bossCounter.value == 1 and boss.centerY <= 85:
        boss.centerY += 10
        
        
    # HighScore Algorithm
    pointCounter.value += 1
    pointCounter.value -= 0.5
    if pointTitle.value < pointCounter.value:
        pointTitle.value = pointCounter.value
        
        
        
        
    
    
 
 ### Win Screen ### 
 
winScreen1 = RegularPolygon(200, 200, 150, 6, fill='magenta', visible = False)
winScreen2 = RegularPolygon(200, 200, 170, 6, fill=None, border='magenta', borderWidth = 4, visible = False)
winScreen3 = Label("You Win!", 200, 160, size=30, font='monospace', visible = False, fill='white', bold=True)
winScreen4 = Label("Congratulations, however", 200, 225, size=14.5, font='monospace', visible = False, fill='white', bold=True)
winScreen5 = Label("your journey has just begun", 200, 250, size=14.5, font='monospace', visible = False, fill='white', bold=True)
 
 
def winScreen():
    author.visible = False
    winScreen1.visible = True
    winScreen2.visible = True
    winScreen3.visible = True
    winScreen4.visible = True
    winScreen5.visible = True
    EarthShip.visible = False
    laserBeam.visible = False
    titlelabel1.visible = False
    titlelabel2.visible = False
    titlelabel3.visible = False
    titlelabel4.visible = False
    newGameTitle.visible = False 
    helpGameTitle.visible = False 
    quitGameTitle.visible = False
    animationarrow1.visible = False
    animationarrow2.visible = False
    ufo.visible = False
    ufo2.visible = False
    ufo3.visible = False
    ufo4.visible = False
    stageEarthShip.visible = False
    ufoBlasterShot.visible = False
    ufoBlasterShot2.visible = False
    ufoBlasterShot3.visible = False
    playerHealthLabel.visible = False
    playerHealth.visible = False
    helpScreen1.visible = False
    helpScreen2.visible = False
    helpScreen3.visible = False
    helpScreen4.visible = False
    wbox.visible = False
    sbox.visible = False
    abox.visible = False
    dbox.visible = False
    vbox.visible = False
    wlabel.visible = False 
    slabel.visible = False
    alabel.visible = False
    dlabel.visible = False
    vlabel.visible = False
    stageBoss.visible = False
    ufoBlasterShot.visible = False
    ufoBlasterShot2.visible = False
    ufoBlasterShot3.visible = False
    boss.visible = False
    boosterFrame.visible = False
    speedFrame.visible = False 
    boosterTitle.visible = False 
    speedTitle.visible = False
    seperator1.visible = False
    seperator2.visible = False
    seperator3.visible = False
    seperator4.visible = False 
    pointLabel.visible = False
    pointTitle.visible = False
 


### Lose Screen ###

loseScreen1 = RegularPolygon(200, 200, 150, 6, fill='red', visible = False)
loseScreen2 = RegularPolygon(200, 200, 170, 6, fill=None, border='red', borderWidth = 4, visible = False)
loseScreen3 = Label("Game Over!", 200, 160, size=30, font='monospace', visible = False, fill='white', bold=True)
loseScreen4 = Label("Maybe gaming isn't for you", 200, 225, size=14.5, font='monospace', visible = False, fill='white', bold=True)


def loseScreen():
    author.visible = False
    loseScreen1.visible = True
    loseScreen2.visible = True
    loseScreen3.visible = True
    loseScreen4.visible = True
    EarthShip.visible = False
    laserBeam.visible = False
    titlelabel1.visible = False
    titlelabel2.visible = False 
    titlelabel3.visible = False 
    titlelabel4.visible = False 
    newGameTitle.visible = False 
    helpGameTitle.visible = False 
    quitGameTitle.visible = False
    animationarrow1.visible = False
    animationarrow2.visible = False
    ufo.visible = False
    ufo2.visible = False
    ufo3.visible = False
    ufo4.visible = False
    stageEarthShip.visible = False
    ufoBlasterShot.visible = False
    ufoBlasterShot2.visible = False
    ufoBlasterShot3.visible = False
    playerHealthLabel.visible = False
    playerHealth.visible = False
    helpScreen1.visible = False
    helpScreen2.visible = False
    helpScreen3.visible = False 
    helpScreen4.visible = False
    wbox.visible = False
    sbox.visible = False
    abox.visible = False
    dbox.visible = False
    vbox.visible = False
    wlabel.visible = False 
    slabel.visible = False
    alabel.visible = False
    dlabel.visible = False
    vlabel.visible = False
    stageBoss.visible = False
    boosterFrame.visible = False
    speedFrame.visible = False 
    boosterTitle.visible = False 
    speedTitle.visible = False
    seperator1.visible = False
    seperator2.visible = False
    seperator3.visible = False
    seperator4.visible = False
    pointLabel.visible = False
    pointTitle.visible = False
 




### Booster ###

def booster():
    playerHealth.value += moneyBoosterCounter.value




### Speed ###

speedCounter = Label(0, 200, 200, fill=None)

def speed():
    speedCounter.value = 1
    moneySpeedCounter.value == 1
    
    
    
        
### Mouse Controls ###

def onMousePress(mouseX, mouseY):
    if pointCounter.value >= 100 and (boosterFrame.hits(mouseX, mouseY) == True) and moneyBoosterCounter.value > 1:
        booster()
        moneyBoosterCounter.value -= 10
        pointTitle.value -= 100
        
    if pointCounter.value >= 150 and (speedTitle.hits(mouseX, mouseY) == True):
        speed()
        pointTitle.value -= 150
        





### Key Controls ###


def onKeyPress(key):
    
    #Boss being enabled
    if ufo2.opacity <= 12 and ufo3.opacity <= 12 and ufo4.opacity <= 12:
        boss.visible = True
        bossCounter.value = bossReturnCounter.value 
    
    if animationarrow1.centerY <= 260:
        
        if key == "s" or key == "down":
            animationarrow1.centerY += 35
            animationarrow2.centerY += 35
            
    
    if animationarrow1.centerY >= 225:
            
        if key == "w" or key == "up":
            animationarrow1.centerY -= 35
            animationarrow2.centerY -= 35
            
    
    
    if animationarrow1.centerY == 220 and key == "enter":
        gameStart()



    if animationarrow1.centerY == 255 and key == "enter":
        helpScreen()
    
    
    if animationarrow1.centerY == 290 and key == "enter":
        exitScreen()
        app.stop()

    
    
    if (key == 's'):
        if speedCounter.value == 0:
            EarthShip.dx = 0  
        elif speedCounter.value == 1:
            EarthShip.dx = 0
    elif (key == 'd'):
        if speedCounter.value == 0:
            EarthShip.dx = 7    
        elif speedCounter.value == 1:
            EarthShip.dx = 10
    elif (key == 'a'):
        if speedCounter.value == 0:
            EarthShip.dx = -7    
        elif speedCounter.value == 1:
            EarthShip.dx = -10
        
    

    #To play again from the Lose Screen
    if key == 'm':
        menu()
        
        

def onKeyRelease(key):
    if key == 'w' and titlelabel1.visible == False:
        laserBeam.centerY += pushCounter.value
        EarthShip.centerY += pushCounter.value
        pushCounter.value = 0



def onKeyHold(keys):
    if ('v' in keys):
        if laserBeam.y2 > 1:
            laserBeam.visible = True
            laserBeam.y2 -= 45
            
    if ('w' in keys) and EarthShip.centerY > 310 and titlelabel1.visible == False:
        EarthShip.centerY -= 5
        laserBeam.centerY -= 5
        pushCounter.value += 5

    


### Exit Screen ###

def exitScreen():
    Rect(0, 0, 400, 400)



