from cmu_graphics import*
import os, pathlib
import math
import random
from block import block
from obstacles import obstacle



def loadSound(relativePath):
    # Convert to absolute path (because pathlib.Path only takes absolute paths)
    absolutePath = os.path.abspath(relativePath)
    # Get local file URL
    url = pathlib.Path(absolutePath).as_uri()
    # Load Sound file from local URL
    return Sound(url)



#obstacles
floor = obstacle('floor', 150, 225, 800, 200)
spike = obstacle('spike', 30, 237.5, 800, 224.5)
doubleSpike = obstacle ('doubleSpike', 30, 237.5, 800, 224.5)
tripleSpike = obstacle ('tripleSpike', 30, 237.5, 800, 224.5)
topSpike = obstacle('topSpike',30, 800, random.randrange(100, 150), 150)

#features and power ups
invincible = obstacle('invincible', 30, 800,random.randrange(150,175), 150)
jetpack = obstacle('jetpack', 30, 800, random.randrange(150,175), 150)

#player Block
playerBlock =  block('purple', 150, 225, 50, 0, 15)



def onAppStart(app):
    app.width = 800
    app.height = 400
    app.titleScreen = True
    app.difficultySetting = False
    app.stepsPerSecond = 30
    app.obstacleX = 800
    app.obstacleY = 200
    app.jumping = False
    app.falling = False
    app.blockAngle = 0
    app.obstacles = [floor.shape,spike.shape, doubleSpike.shape, tripleSpike.shape, topSpike.shape] 
    app.powerups = [jetpack.shape,invincible.shape]
    app.currentPowerup = app.powerups[random.randrange(0,2)]
    app.backgroundX = 0
    app.horizontalTrail = True
    app.mapSpeed = -5
    app.jumpMax = 125
    app.countdown = 3
    app.relativeCount = 0
    app.playScreen = False
    app.mainFloorY = 250
    app.floorObstacle = False
    app.currentObstacle1 = app.obstacles[1]
    app.floorY = 250
    app.pauseScreen = False
    app.gameover = False
    app.obstacleXHolder = 800
    app.scoreCount= 0
    app.scoreCountRelative = 0
    app.time = 0
    app.startVelocity = 10
    app.CountRelative = 0
    app.jetpack = False
    app.invincible = False
    app.deleteInvincible = False
    app.invincibleCount = 0
    app.jetpackCount = 0
    app.slow = True
    app.moderate = False
    app.fast = False
    app.slowHighScore = 0
    app.moderateHighScore = 0
    app.fastHighScore = 0
    app.jetpack = False
    app.deleteJetpack = False
    app.jetpackJumping = False
    app.jetpackFalling = False
    app.powerupX = random.randrange(1600,2000)
    app.verticalTrail = False
    app.collision = False
    app.deleteBlock = False
    app.collisionTimer = 5
    #Geometry sounds downloaded from https://downloads.khinsider.com/game-soundtracks/album/geometry-dash
    #deathSound is taken from the bullet sound demo from piazza
    app.deathSound = loadSound("sounds/bulletSound.mp3")
    app.mainMenuMusic = loadSound("sounds/mainMenu.mp3")
    app.hexagonForceMusic = loadSound("sounds/hexagonForce.mp3")



def redrawAll(app):
    #title screen 
    if app.titleScreen == True:
        app.mainMenuMusic.play(loop = True)
        drawTitleScreen(app)
    #speed/difficulty screen
    elif app.difficultySetting == True and app.titleScreen == False:
        app.mainMenuMusic.play(loop = True)
        drawDifficultyScreen(app)
    #play screen 
    elif app.titleScreen == False and app.difficultySetting == False and app.gameover == False:
        app.mainMenuMusic.pause()
        app.hexagonForceMusic.play(loop = True)
        drawPlayScreen(app)
    #gameover screen
    elif app.titleScreen == False and app.difficultySetting == False and app.gameover == True:
        app.mainMenuMusic.play(loop = True)
        drawGameoverScreen(app)
#-------------------------------------------------------------------------------
def drawTitleScreen(app):
    #background color
    for i in range(-800, app.width, 50):
        drawRect(app.backgroundX + i, 0, 800, app.height, fill='lightblue', opacity=80)
        drawRect(app.backgroundX + i, 0, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 50, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 100, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 150, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 200, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 250, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 300, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 350, 50, 50, fill='blue', opacity=10, border='white')
    #drawing for the title screen
    drawLabel('Geometry Dash Mini', 400, 50, size=50, font='orbitron', bold=True, fill='lightgreen', border= 'black', borderWidth=2,opacity=100)
    #play button
    drawRect(400, 200, 100, 100, fill='cyan', align = 'center', border = 'black')
    drawRegularPolygon(395,200, 50, 3, fill = 'yellow', border = 'black', rotateAngle = 90, align = 'center')
    #speed/difficulty setting
    drawRect(400, 325, 200, 100, fill = 'cyan', align = 'center', border = 'black')
    drawLabel('Select Difficulty', 400, 325, fill = 'lightgreen', font = 'orbitron', size = 27.5, border = 'black')
#-------------------------------------------------------------------------------

def drawDifficultyScreen(app):
    #background color
    drawRect(0,0,800,400,fill = 'lightblue', opacity = 80)
    #background color
    for i in range(-800, app.width, 50):
        drawRect(app.backgroundX + i, 0, 800, app.height, fill='lightblue', opacity=80)
        drawRect(app.backgroundX + i, 0, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 50, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 100, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 150, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 200, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 250, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 300, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 350, 50, 50, fill='blue', opacity=10, border='white')
    #different speeds
    drawRect(150, 200, 200, 100, align = 'center', fill = 'cyan', border = 'black')
    drawRect(400, 200, 200, 100, align = 'center', fill = 'cyan', border = 'black')
    drawRect(650, 200, 200, 100, align = 'center', fill = 'cyan', border = 'black')
    drawLabel('Slow', 150, 200, fill = 'lightgreen', border = 'black', font = 'orbitron', size = 45)
    drawLabel('Moderate', 400, 200, fill = 'lightgreen', border = 'black', font = 'orbitron', size = 45)
    drawLabel('Fast', 650, 200, fill = 'lightgreen', border = 'black', font = 'orbitron', size = 45)
    #highscores
    drawLabel(f'Score: {app.slowHighScore}', 150, 125, fill = 'purple', font = 'orbitron', size = 30)
    drawLabel(f'Score: {app.moderateHighScore}', 400, 125, fill = 'purple', font = 'orbitron', size = 30)
    drawLabel(f'Score: {app.fastHighScore}', 650, 125, fill = 'purple', font = 'orbitron', size = 30)
#-------------------------------------------------------------------------------

def drawPlayScreen(app):
    #background color and background sqaures
    for i in range(-800, app.width, 50):
        drawRect(app.backgroundX + i, 0, 800, app.height, fill='lightblue', opacity=80)
        drawRect(app.backgroundX + i, 0, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 50, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 100, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 150, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 200, 50, 50, fill='blue', opacity=10, border='white')
    #floor
    drawRect(0,250,800, 250, fill = 'blue', border = 'black', opacity = 50, borderWidth = 5)
    #Countdown
    #obstacle load
    if app.countdown != 0:
        drawLabel(f'{app.countdown}', 400, 200, size=50, font='orbitron', bold=True, fill='lightgreen', border= 'black', borderWidth=2,opacity=100)
    else:
        #obstacle drawings
        if app.currentObstacle1 == 'floor':
            drawRect(app.obstacleX,app.obstacleY,150, 50, fill = 'blue', border = 'black', opacity = 50, borderWidth = 5)
        elif app.currentObstacle1 == 'spike':
            drawRegularPolygon(app.obstacleX, 237.5, 30, 3, fill='red', border = 'black', borderWidth = 2) 
        elif app.currentObstacle1 == 'doubleSpike':
            drawRegularPolygon(app.obstacleX, 237.5, 30, 3, fill='red', border = 'black', borderWidth = 2) 
            drawRegularPolygon(app.obstacleX+45, 237.5, 30, 3, fill='red', border = 'black', borderWidth = 2) 
        elif app.currentObstacle1 == 'tripleSpike':
            drawRegularPolygon(app.obstacleX, 237.5, 30, 3, fill='red', border = 'black', borderWidth = 2) 
            drawRegularPolygon(app.obstacleX+45, 237.5, 30, 3, fill='red', border = 'black', borderWidth = 2) 
            drawRegularPolygon(app.obstacleX+90, 237.5, 30, 3, fill='red', border = 'black', borderWidth = 2) 
        elif app.currentObstacle1 == 'topSpike':
            drawRect(app.obstacleX, topSpike.centerY-25, 100,25, fill = 'red', border = 'black', borderWidth = 2, align = 'center')
            drawRegularPolygon(app.obstacleX, topSpike.centerY, 30, 3, fill='red', border = 'black', borderWidth = 2, rotateAngle = 180) 
        #powerup drawings
        if app.currentPowerup == 'jetpack' and app.deleteJetpack == False:
            drawRegularPolygon(app.powerupX, jetpack.centerY, 30, 6, fill='purple', border = 'black', borderWidth = 2)
            drawRegularPolygon(app.powerupX, jetpack.centerY, 30, 3, fill='cyan', border = 'black', borderWidth = 2) 
        elif app.currentPowerup == 'invincible' and app.deleteInvincible == False:
            drawCircle(app.powerupX, invincible.centerY, invincible.width, fill = 'purple', border = 'black', borderWidth = 2)
            drawCircle(app.powerupX, invincible.centerY, invincible.width-10, fill = None, border = 'cyan', borderWidth = 3)

    #player block
    if app.deleteBlock == False:
        drawRect(playerBlock.centerX, playerBlock.centerY, playerBlock.sideLength, playerBlock.sideLength, fill = 'purple', border = 'white', align = 'center', rotateAngle = playerBlock.angle)
        drawRect(playerBlock.centerX, playerBlock.centerY, playerBlock.sideLength-10, playerBlock.sideLength-10, fill = 'blue', border = 'white', align = 'center', rotateAngle = playerBlock.angle)
        drawRect(playerBlock.centerX, playerBlock.centerY, playerBlock.sideLength-20, playerBlock.sideLength-20, fill = 'purple', border = 'white', align = 'center', rotateAngle = playerBlock.angle)
        drawRect(playerBlock.centerX, playerBlock.centerY, playerBlock.sideLength-30, playerBlock.sideLength-30, fill = 'black', border = 'white', align = 'center', rotateAngle = playerBlock.angle)
    #player block trail
    if app.horizontalTrail == True and app.deleteBlock == False:
        for i in range(playerBlock.centerX - 75, playerBlock.centerX-25, 5):
            drawCircle(i, playerBlock.centerY + 25 - random.randrange(0,15), 2, fill = 'purple')
            drawCircle(i-5, playerBlock.centerY + 25 - random.randrange(0,15), 2, fill = 'white')
            drawCircle(i-10, playerBlock.centerY + 25 - random.randrange(0,15), 2, fill = 'blue')
    if app.verticalTrail == True and app.deleteBlock == False: 
        for i in range(int(playerBlock.centerY + 25), int(playerBlock.centerY + 75), 5):
            drawCircle(playerBlock.centerX + random.randrange(-5,5), i, 2, fill = 'lightgreen')
            drawCircle(playerBlock.centerX + randrange(-5,5), i+5, 2, fill = 'white')
            drawCircle(playerBlock.centerX + random.randrange(-5,5), i+10, 2, fill = 'yellow')
    #if invincible
    if app.invincible == True:
        drawCircle(playerBlock.centerX,playerBlock.centerY, 60, fill = None, border = 'cyan', borderWidth = 2)
        drawLabel(f'Invincibility : [{app.invincibleCount}]', 400, 100, size=25, font='orbitron', bold=True, fill='cyan', border= 'black', borderWidth=2,opacity=100)
    if app.jetpack == True:
        drawLabel(f'Jetpack : [{app.jetpackCount}]', 400, 150, size=25, font='orbitron', bold=True, fill='cyan', border= 'black', borderWidth=2,opacity=100)
    
    #collision animation
    if app.collision == True:
        app.hexagonForceMusic.pause()
        app.deathSound.play()
        for time in range(app.collisionTimer):
            drawCircle(playerBlock.centerX + random.randrange(-playerBlock.sideLength/2,playerBlock.sideLength/2)-time, random.randrange(playerBlock.centerY-25, playerBlock.centerY+25)-time, 2, fill = 'purple')
            drawCircle(playerBlock.centerX + random.randrange(-playerBlock.sideLength/2,playerBlock.sideLength/2)-time, random.randrange(playerBlock.centerY-25, playerBlock.centerY+25)-time, 2, fill = 'blue')
            drawCircle(playerBlock.centerX + random.randrange(-playerBlock.sideLength/2,playerBlock.sideLength/2)-time, random.randrange(playerBlock.centerY-25, playerBlock.centerY+25)-time, 2, fill = 'black')
            drawCircle(playerBlock.centerX + random.randrange(-playerBlock.sideLength/2,playerBlock.sideLength/2)-time, random.randrange(playerBlock.centerY-25, playerBlock.centerY+25)-time, 2, fill = 'white')
        
    #ScoreBoard
    drawLabel(f'Score: [{app.scoreCount}]', 400, 50, size=25, font='orbitron', bold=True, fill='lightgreen', border= 'black', borderWidth=2,opacity=100)
#-------------------------------------------------------------------------------
#gameover screen
def drawGameoverScreen(app):
    #background color
    drawRect(0,0,800,400,fill = 'lightblue', opacity = 80)
    #background color
    for i in range(-800, app.width, 50):
        drawRect(app.backgroundX + i, 0, 800, app.height, fill='lightblue', opacity=80)
        drawRect(app.backgroundX + i, 0, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 50, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 100, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 150, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 200, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 250, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 300, 50, 50, fill='blue', opacity=10, border='white')
        drawRect(app.backgroundX + i, 350, 50, 50, fill='blue', opacity=10, border='white')
    #ScoreBoard
    drawLabel(f'Final Score: [{app.scoreCount}]', 400, 150, size=50, font='orbitron', bold=True, fill='lightgreen', border= 'black', borderWidth=2,opacity=100)
    drawLabel(f"Click 'm' to go back to the MENU", 400, 200, size=25, font='orbitron', bold=True, fill='lightgreen', border= 'black', borderWidth=2,opacity=100)
    


def onKeyPress(app, key):
    #jump mechanics
    if key == 'space' and app.jumping == False and app.falling == False and app.jetpack == False:
        app.jumping = True
    if key == 'm' and app.titleScreen == False and app.difficultySetting == False and app.gameover == True:
        app.width = 800
        app.height = 400
        app.titleScreen = True
        app.difficultySetting = False
        app.stepsPerSecond = 30
        app.obstacleX = 800
        app.obstacleY = 200
        app.jumping = False
        app.falling = False
        app.blockAngle = 0
        app.obstacles = [floor.shape,spike.shape, doubleSpike.shape, tripleSpike.shape, topSpike.shape] 
        app.powerups = [jetpack.shape,invincible.shape]
        app.currentPowerup = app.powerups[random.randrange(0,2)]
        app.backgroundX = 0
        app.horizontalTrail = True
        app.mapSpeed = -5
        app.jumpMax = 125
        app.countdown = 3
        app.relativeCount = 0
        app.playScreen = False
        app.mainFloorY = 250
        app.floorObstacle = False
        app.currentObstacle1 = app.obstacles[1]
        app.floorY = 250
        app.pauseScreen = False
        app.gameover = False
        app.obstacleXHolder = 800
        app.scoreCount= 0
        app.scoreCountRelative = 0
        app.time = 0
        app.startVelocity = 10
        app.CountRelative = 0
        app.jetpack = False
        app.invincible = False
        app.deleteInvincible = False
        app.invincibleCount = 0
        app.jetpackCount = 0
        app.jetpack = False
        app.deleteJetpack = False
        app.jetpackJumping = False
        app.jetpackFalling = False
        app.powerupX = random.randrange(1600,2000)
        app.verticalTrail = False
        app.collision = False
        app.deleteBlock = False
        app.collisionTimer = 0

def onKeyHold(app,keys):
    if app.jetpack == True:
        if 'space' in keys and playerBlock.centerY + 100 >= 0:
            app.jetpackJumping = True
            app.jetpackFalling = False

            


def onKeyRelease(app,key):
    if app.jetpack == True:
        app.jetpackJumping = False
        app.jetpackFalling = True
            
        




def onStep(app):
    if app.gameover == True: 
        if app.slow == True and app.scoreCount >= app.slowHighScore:
            app.slowHighScore = app.scoreCount
        elif app.moderate == True and app.scoreCount >= app.moderateHighScore:
            app.moderateHighScore = app.scoreCount
        elif app.fast == True and app.scoreCount >= app.fastHighScore:
            app.fastHighScore = app.scoreCount
    #Count screen 
    if app.difficultySetting == False and app.titleScreen == False and app.playScreen == False:
        app.relativeCount += 30
    if app.relativeCount == 900:
        app.countdown = 2
    elif app.relativeCount == 1800:
        app.countdown = 1
    elif app.relativeCount == 2700:
        app.countdown = 0
    #making sure that the map speed is different from the block jump speed so it runs smoother
    if app.countdown == 0:
        app.scoreCountRelative += 0.033333333333333333
        if app.scoreCountRelative >= 1 and app.gameover == False:
            app.scoreCount += 1
            app.mapSpeed += 0.5
            app.scoreCountRelative = 0
            if app.scoreCount % 10 == 0 and app.invincible == True:
                app.invincible = False
                app.deleteInvincible = False
            else: 
                app.invincibleCount = abs(app.scoreCount % 10 - 10)
            if app.scoreCount % 15 == 0 and app.jetpack == True:
                app.jetpack = False
                app.deleteJetpack = False
            else: 
                app.jetpackCount = abs(app.scoreCount % 15 - 15)


        #obstacle generation
        if app.currentObstacle1 == 'floor' and app.obstacleX <= 0:
            app.obstacleXHolder = 150
        app.obstacleX -= (10 + app.mapSpeed)
        app.obstacleXHolder -= (10 + app.mapSpeed) 
        if app.currentObstacle1 == 'floor' and (app.obstacleXHolder + 150 <= 0 or app.obstacleX + 150 <= 0):
            app.obstacleX = 800 #move obstacle back to the beginning
            app.obstacleXHolder = 800
            if app.mapSpeed < 2:
                app.currentObstacle1 = app.obstacles[random.randrange(0,2)]
            else:
                app.currentObstacle1 = app.obstacles[random.randrange(0,5)]
        elif app.currentObstacle1 == 'spike' and app.obstacleX + 150 <= 0:
            app.obstacleX = 800 #move obstacle back to the beginning
            if app.mapSpeed < 2:
                app.currentObstacle1 = app.obstacles[random.randrange(0,2)]
            else:
                app.currentObstacle1 = app.obstacles[random.randrange(0,5)]
        elif app.currentObstacle1 == 'doubleSpike' and app.obstacleX + 100 <= 0:
            app.obstacleX = 800 #move obstacle back to the beginning
            if app.mapSpeed < 2:
                app.currentObstacle1 = app.obstacles[random.randrange(0,2)]
            else:
                app.currentObstacle1 = app.obstacles[random.randrange(0,5)]
        elif app.currentObstacle1 == 'tripleSpike' and app.obstacleX + 100 <= 0:
            app.obstacleX = 800 #move obstacle back to the beginning
            if app.mapSpeed < 2:
                app.currentObstacle1 = app.obstacles[random.randrange(0,2)]
            else:
                app.currentObstacle1 = app.obstacles[random.randrange(0,5)]
        elif app.currentObstacle1 == 'topSpike' and app.obstacleX + 100 <= 0:
            app.obstacleX = 800 #move obstacle back to the beginning
            if app.mapSpeed < 2:
                app.currentObstacle1 = app.obstacles[random.randrange(0,2)]
            else:
                app.currentObstacle1 = app.obstacles[random.randrange(0,5)]

        #powerup generation
        app.powerupX -= (10 + app.mapSpeed)
        if app.currentPowerup == 'invincible' and app.powerupX <= 0:
            app.powerupX = random.randrange(1600,2000)
            if app.invincible == True:
                app.currentPowerup = app.powerups[0]
            else:
                app.currentPowerup = app.powerups[random.randrange(0,2)]
        elif app.currentPowerup == 'jetpack' and app.powerupX <= 0:
            app.powerupX = random.randrange(1600,2000)
            if app.invincible == True:
                app.currentPowerup = app.powerups[1]
            else:
                app.currentPowerup = app.powerups[random.randrange(0,2)]
    
    app.backgroundX -= 2 
    if app.backgroundX <= 0:
        app.backgroundX = 800
    #updating imaginary block as the block goes up and down
    playerBlock.rightValue = playerBlock.centerX + (playerBlock.sideLength/2)
    playerBlock.leftValue = playerBlock.centerX - (playerBlock.sideLength/2)
    playerBlock.topValue = playerBlock.centerY - (playerBlock.sideLength/2)
    playerBlock.bottomValue = playerBlock.centerY + (playerBlock.sideLength/2)
    #changing app.floorY for the block to land on the floor obstacle
    if app.currentObstacle1 == 'floor' and (playerBlock.centerX >= app.obstacleX and playerBlock.centerX - 25 <= app.obstacleX + floor.width):
        app.floorY = floor.topY
    elif app.jetpack == False:
        app.floorY = app.mainFloorY
        app.falling = True
    #jumping and falling animation

    addAngle = (150/((app.floorY - app.jumpMax)/10))/2
    if app.jetpack == False and app.collision == False:
        app.verticalTrail = False
        if app.jumping == True:
            app.CountRelative += 0.05
            app.falling = False
            playerBlock.centerY -= 10
            #updating imaginary block as the block goes up and down
            playerBlock.topValue = playerBlock.centerY - (playerBlock.sideLength/2)
            playerBlock.bottomValue = playerBlock.centerY - (playerBlock.sideLength/2)
            playerBlock.angle += addAngle
            #finding a point after a rotation
            playerBlock.topRight = (playerBlock.topRight[0] * math.cos(math.degrees(playerBlock.angle)) - playerBlock.topRight[1] * math.sin(math.degrees(playerBlock.angle)), playerBlock.topRight[0] * math.sin(math.degrees(playerBlock.angle)) - playerBlock.topRight[1] * math.cos(math.degrees(playerBlock.angle))- (playerBlock.sideLength/2))
            playerBlock.topLeft = (playerBlock.topLeft[0] * math.cos(math.degrees(playerBlock.angle)) - playerBlock.topLeft[1] * math.sin(math.degrees(playerBlock.angle)), playerBlock.topLeft[0] * math.sin(math.degrees(playerBlock.angle)) - playerBlock.topLeft[1] * math.cos(math.degrees(playerBlock.angle))- (playerBlock.sideLength/2))
            playerBlock.bottomRight = (playerBlock.bottomRight[0] * math.cos(math.degrees(playerBlock.angle)) - playerBlock.bottomRight[1] * math.sin(math.degrees(playerBlock.angle)), playerBlock.bottomRight[0] * math.sin(math.degrees(playerBlock.angle)) - playerBlock.bottomRight[1] * math.cos(math.degrees(playerBlock.angle))- (playerBlock.sideLength/2))
            playerBlock.bottomLeft = (playerBlock.bottomLeft[0] * math.cos(math.degrees(playerBlock.angle)) - playerBlock.bottomLeft[1] * math.sin(math.degrees(playerBlock.angle)), playerBlock.bottomLeft[0] * math.sin(math.degrees(playerBlock.angle)) - playerBlock.bottomLeft[1] * math.cos(math.degrees(playerBlock.angle))- (playerBlock.sideLength/2))
            app.horizontalTrail = False
            if app.CountRelative >= 0.5:
                app.jumping = False
                app.falling = True

        if app.falling == True and playerBlock.centerY+25 <= app.floorY:
            if playerBlock.centerY+25 < app.floorY:
                app.CountRelative += 0.033333333333333333
                if app.CountRelative >= 1 and app.gameover == False:
                    app.time += 1
                    app.CountRelative = 0
                changeX = app.startVelocity + (0.5*(15)*((app.time)**2))
                playerBlock.centerY += changeX
                playerBlock.angle += addAngle
                app.horizontalTrail = False
                #updating imaginary block as the block goes up and down
                playerBlock.topValue = playerBlock.centerY - (playerBlock.sideLength/2)
                playerBlock.bottomValue = playerBlock.centerY - (playerBlock.sideLength/2)
                playerBlock.angle += addAngle
                #finding a point after a rotation
                playerBlock.topRight = (playerBlock.topRight[0] * math.cos(math.degrees(playerBlock.angle)) - playerBlock.topRight[1] * math.sin(math.degrees(playerBlock.angle)), playerBlock.topRight[0] * math.sin(math.degrees(playerBlock.angle)) - playerBlock.topRight[1] * math.cos(math.degrees(playerBlock.angle))- (playerBlock.sideLength/2))
                playerBlock.topLeft = (playerBlock.topLeft[0] * math.cos(math.degrees(playerBlock.angle)) - playerBlock.topLeft[1] * math.sin(math.degrees(playerBlock.angle)), playerBlock.topLeft[0] * math.sin(math.degrees(playerBlock.angle)) - playerBlock.topLeft[1] * math.cos(math.degrees(playerBlock.angle))- (playerBlock.sideLength/2))
                playerBlock.bottomRight = (playerBlock.bottomRight[0] * math.cos(math.degrees(playerBlock.angle)) - playerBlock.bottomRight[1] * math.sin(math.degrees(playerBlock.angle)), playerBlock.bottomRight[0] * math.sin(math.degrees(playerBlock.angle)) - playerBlock.bottomRight[1] * math.cos(math.degrees(playerBlock.angle))- (playerBlock.sideLength/2))
                playerBlock.bottomLeft = (playerBlock.bottomLeft[0] * math.cos(math.degrees(playerBlock.angle)) - playerBlock.bottomLeft[1] * math.sin(math.degrees(playerBlock.angle)), playerBlock.bottomLeft[0] * math.sin(math.degrees(playerBlock.angle)) - playerBlock.bottomLeft[1] * math.cos(math.degrees(playerBlock.angle))- (playerBlock.sideLength/2))
            if playerBlock.centerY + 25 >= app.floorY:
                app.time = 0
                app.CountRelative = 0
                playerBlock.centerY = app.floorY - 25
                playerBlock.angle = 0
                playerBlock.topRight = (playerBlock.rightValue, playerBlock.topValue)
                playerBlock.topLeft = (playerBlock.leftValue, playerBlock.topValue)
                playerBlock.bottomRight = (playerBlock.rightValue, playerBlock.bottomValue)
                playerBlock.bottomLeft = (playerBlock.leftValue, playerBlock.bottomValue)
                app.horizontalTrail = True
                app.falling = False
    elif app.jetpack == True and app.collision == False:
        if app.currentObstacle1 == 'floor' and (playerBlock.centerX >= app.obstacleX and playerBlock.centerX - 25 <= app.obstacleX + floor.width):
            app.floorY = floor.topY
        else:
            app.floorY = app.mainFloorY
            app.jetpackFalling = True
        app.horizontalTrail = False
        playerBlock.angle = 0
        app.jumping = False
        app.falling = False
        if app.jetpackJumping == True and playerBlock.centerY + 50 >= 50: 
            app.verticalTrail = True
            playerBlock.centerY -= 10
            playerBlock.topValue = playerBlock.centerY - (playerBlock.sideLength/2)
            playerBlock.bottomValue = playerBlock.centerY - (playerBlock.sideLength/2)
            playerBlock.topRight = (playerBlock.rightValue, playerBlock.topValue)
            playerBlock.topLeft = (playerBlock.leftValue, playerBlock.topValue)
            playerBlock.bottomRight = (playerBlock.rightValue, playerBlock.bottomValue)
            playerBlock.bottomLeft = (playerBlock.leftValue, playerBlock.bottomValue)
        elif app.jetpackJumping == False and app.jetpackFalling == True:
            app.verticalTrail = False
            app.CountRelative += 0.033333333333333333
            if app.CountRelative >= 1 and app.gameover == False:
                app.time += 1
                app.CountRelative = 0
            if playerBlock.centerY+25 < app.floorY:
                changeY = app.startVelocity + (0.5*(15)*((app.time)**2))
                playerBlock.centerY += changeY
            if playerBlock.centerY + 25 >= app.floorY:
                app.time = 0
                app.CountRelative = 0
                playerBlock.centerY = app.floorY - 25
                playerBlock.angle = 0
                playerBlock.topRight = (playerBlock.rightValue, playerBlock.topValue)
                playerBlock.topLeft = (playerBlock.leftValue, playerBlock.topValue)
                playerBlock.bottomRight = (playerBlock.rightValue, playerBlock.bottomValue)
                playerBlock.bottomLeft = (playerBlock.leftValue, playerBlock.bottomValue)
                app.horizontalTrail = True
                app.jetpackFalling = False





    #check collision
    if app.invincible == False and isValidObstacle(app,playerBlock) == True:
        app.collision = True
        app.deleteBlock = True
    if app.collision == True:
        if app.collisionTimer <= 50:
            app.collisionTimer += 2
        else:
            app.collision == False
            app.gameover = True
            
        
    isValidPowerup(app, playerBlock)





def onMousePress(app, mouseX, mouseY):
    #title screen options
    if app.titleScreen == True and (mouseX >= 350 and mouseX <= 450) and (mouseY >= 150 and mouseY <= 250):
        app.titleScreen = False
    elif app.titleScreen == True and (mouseX >=200 and mouseX <= 600) and (mouseY >= 225 and mouseY <= 425):
        app.titleScreen = False
        app.difficultySetting = True
    #difficulty options
    if app.difficultySetting == True and (mouseX >= 50 and mouseX <= 250) and (mouseY >= 150 and mouseY <= 250):
        app.slow = True
        app.moderate = False
        app.fast = False
        app.mapSpeed = -5
        app.difficultySetting = False
        app.titleScreen = True
    elif app.difficultySetting == True and (mouseX >= 300 and mouseX <= 500) and (mouseY >= 150 and mouseY <= 250):
        app.moderate = True
        app.slow = False
        app.fast = False
        app.difficultySetting = False
        app.titleScreen = True
        app.mapSpeed = 0
    elif app.difficultySetting == True and (mouseX >= 550 and mouseX <= 750) and (mouseY >= 150 and mouseY <= 250):
        app.fast = True
        app.slow = False
        app.moderate = False
        app.difficultySetting = False
        app.titleScreen = True
        app.mapSpeed = 5
    
#collision between rectangle and triangle algorithm: https://seblee.me/2009/05/super-fast-trianglerectangle-intersection-test/#:~:text=So%20how%20do%20you%20accurately,yes%20then%20intersection%20is%20true.

def isValidObstacle(app,playerBlock):
    if app.currentObstacle1 == 'spike':
        if app.obstacleX >= playerBlock.leftValue and app.obstacleX <= playerBlock.rightValue and 224.5 <= playerBlock.bottomValue and 224.5 >= playerBlock.topValue:
            return True
        elif app.obstacleX + 15 >= playerBlock.leftValue and app.obstacleX + 15 <= playerBlock.rightValue and 249 <= playerBlock.bottomValue and 249 >= playerBlock.topValue:
            return True
        elif app.obstacleX - 15 >= playerBlock.leftValue and app.obstacleX - 15 <= playerBlock.rightValue and 249 <= playerBlock.bottomValue and 249 >= playerBlock.topValue:
            return True
        else:
            #line intersection
            blockList = [((playerBlock.topRight),(playerBlock.topLeft)), ((playerBlock.bottomRight),(playerBlock.bottomLeft)), ((playerBlock.topRight),(playerBlock.bottomRight)), ((playerBlock.topLeft),(playerBlock.bottomLeft))]
            spikeList1 = [(app.obstacleX, 224.5), (app.obstacleX+15, 249), (app.obstacleX-15, 249)]
            for aLine in blockList:
                if intersect(aLine[0], aLine[1], (app.obstacleX, 224.5), (app.obstacleX+15, 249)) == True:
                    return True
                elif intersect(aLine[0], aLine[1], (app.obstacleX+15, 249), (app.obstacleX-15, 249)) == True:
                    return True
                elif intersect(aLine[0], aLine[1], (app.obstacleX, 224.5), (app.obstacleX-15, 249)) == True:
                    return True
            if rectanglesOverlap(playerBlock.leftValue, playerBlock.topValue, playerBlock.sideLength, playerBlock.sideLength, app.obstacleX - 15, 224.5, 30, 25.5):
                return True
    if app.currentObstacle1 == 'doubleSpike': 
        if app.obstacleX >= playerBlock.leftValue and app.obstacleX <= playerBlock.rightValue and 224.5 <= playerBlock.bottomValue and 224.5 >= playerBlock.topValue:
            return True
        elif app.obstacleX + 15 >= playerBlock.leftValue and app.obstacleX + 15 <= playerBlock.rightValue and 249 <= playerBlock.bottomValue and 249 >= playerBlock.topValue:
            return True
        elif app.obstacleX - 15 >= playerBlock.leftValue and app.obstacleX - 15 <= playerBlock.rightValue and 249 <= playerBlock.bottomValue and 249 >= playerBlock.topValue:
            return True
        elif app.obstacleX + 45 >= playerBlock.leftValue and app.obstacleX + 45 <= playerBlock.rightValue and 224.5 <= playerBlock.bottomValue and 224.5 >= playerBlock.topValue:
            return True 
        elif app.obstacleX + 45 + 15 >= playerBlock.leftValue and app.obstacleX + 45 + 15 <= playerBlock.rightValue and 249 <= playerBlock.bottomValue and 249 >= playerBlock.topValue:
            return True
        elif app.obstacleX + 45 - 15 >= playerBlock.leftValue and app.obstacleX + 45 - 15 <= playerBlock.rightValue and 249 <= playerBlock.bottomValue and 249 >= playerBlock.topValue:
            return True
        else:
            #line intersection of first spike
            blockList = [((playerBlock.topRight),(playerBlock.topLeft)), ((playerBlock.bottomRight),(playerBlock.bottomLeft)), ((playerBlock.topRight),(playerBlock.bottomRight)), ((playerBlock.topLeft),(playerBlock.bottomLeft))]
            spikeList1 = [(app.obstacleX, 224.5), (app.obstacleX+15, 249), (app.obstacleX-15, 249)]
            for aLine in blockList:
                if intersect(aLine[0], aLine[1], (app.obstacleX, 224.5), (app.obstacleX+15, 249)) == True:
                    return True
                elif intersect(aLine[0], aLine[1], (app.obstacleX+15, 249), (app.obstacleX-15, 249)) == True:
                    return True
                elif intersect(aLine[0], aLine[1], (app.obstacleX, 224.5), (app.obstacleX-15, 249)) == True:
                    return True
            #line intersection of first spike
            blockList = [((playerBlock.topRight),(playerBlock.topLeft)), ((playerBlock.bottomRight),(playerBlock.bottomLeft)), ((playerBlock.topRight),(playerBlock.bottomRight)), ((playerBlock.topLeft),(playerBlock.bottomLeft))]
            spikeList2 = [(app.obstacleX+45, 224.5), (app.obstacleX+45+15, 249), (app.obstacleX+45-15, 249)]
            for aLine in blockList:
                if intersect(aLine[0], aLine[1], (app.obstacleX+45, 224.5), (app.obstacleX+45+15, 249)) == True:
                    return True
                elif intersect(aLine[0], aLine[1], (app.obstacleX+45+15, 249), (app.obstacleX+45-15, 249)) == True:
                    return True
                elif intersect(aLine[0], aLine[1], (app.obstacleX+45, 224.5), (app.obstacleX+45+15, 249)) == True:
                    return True
            if rectanglesOverlap(playerBlock.leftValue, playerBlock.topValue, playerBlock.sideLength, playerBlock.sideLength, app.obstacleX - 15, 224.5, 30, 25.5):
                return True
            if rectanglesOverlap(playerBlock.leftValue, playerBlock.topValue, playerBlock.sideLength, playerBlock.sideLength, app.obstacleX + 45 - 15, 224.5, 30, 25.5):
                return True
            
    if app.currentObstacle1 == 'tripleSpike': 
        if app.obstacleX >= playerBlock.leftValue and app.obstacleX <= playerBlock.rightValue and 224.5 <= playerBlock.bottomValue and 224.5 >= playerBlock.topValue:
            return True
        elif app.obstacleX + 15 >= playerBlock.leftValue and app.obstacleX + 15 <= playerBlock.rightValue and 249 <= playerBlock.bottomValue and 249 >= playerBlock.topValue:
            return True
        elif app.obstacleX - 15 >= playerBlock.leftValue and app.obstacleX - 15 <= playerBlock.rightValue and 249 <= playerBlock.bottomValue and 249 >= playerBlock.topValue:
            return True
        elif app.obstacleX + 45 >= playerBlock.leftValue and app.obstacleX + 45 <= playerBlock.rightValue and 224.5 <= playerBlock.bottomValue and 224.5 >= playerBlock.topValue:
            return True
        elif app.obstacleX + 45 + 15 >= playerBlock.leftValue and app.obstacleX + 45 + 15 <= playerBlock.rightValue and 249 <= playerBlock.bottomValue and 249 >= playerBlock.topValue:
            return True
        elif app.obstacleX + 45 - 15 >= playerBlock.leftValue and app.obstacleX + 45 - 15 <= playerBlock.rightValue and 249 <= playerBlock.bottomValue and 249 >= playerBlock.topValue:
            return True
        elif app.obstacleX + 90 >= playerBlock.leftValue and app.obstacleX + 90 <= playerBlock.rightValue and 224.5 <= playerBlock.bottomValue and 224.5 >= playerBlock.topValue:
            return True
        elif app.obstacleX + 90 + 15 >= playerBlock.leftValue and app.obstacleX + 90 + 15 <= playerBlock.rightValue and 249 <= playerBlock.bottomValue and 249 >= playerBlock.topValue:
            return True
        elif app.obstacleX + 90 - 15 >= playerBlock.leftValue and app.obstacleX + 90 - 15 <= playerBlock.rightValue and 249 <= playerBlock.bottomValue and 249 >= playerBlock.topValue:
            return True
        else:
            #line intersection of first spike
            blockList = [((playerBlock.topRight),(playerBlock.topLeft)), ((playerBlock.bottomRight),(playerBlock.bottomLeft)), ((playerBlock.topRight),(playerBlock.bottomRight)), ((playerBlock.topLeft),(playerBlock.bottomLeft))]
            spikeList1 = [(app.obstacleX, 224.5), (app.obstacleX+15, 249), (app.obstacleX-15, 249)]
            for aLine in blockList:
                if intersect(aLine[0], aLine[1], (app.obstacleX, 224.5), (app.obstacleX+15, 249)) == True:
                    return True
                elif intersect(aLine[0], aLine[1], (app.obstacleX+15, 249), (app.obstacleX-15, 249)) == True:
                    return True
                elif intersect(aLine[0], aLine[1], (app.obstacleX, 224.5), (app.obstacleX-15, 249)) == True:
                    return True
            #line intersection of first spike
            blockList = [((playerBlock.topRight),(playerBlock.topLeft)), ((playerBlock.bottomRight),(playerBlock.bottomLeft)), ((playerBlock.topRight),(playerBlock.bottomRight)), ((playerBlock.topLeft),(playerBlock.bottomLeft))]
            spikeList2 = [(app.obstacleX+45, 224.5), (app.obstacleX+45+15, 249), (app.obstacleX+45-15, 249)]
            for aLine in blockList:
                if intersect(aLine[0], aLine[1], (app.obstacleX+45, 224.5), (app.obstacleX+45+15, 249)) == True:
                    return True
                elif intersect(aLine[0], aLine[1], (app.obstacleX+45+15, 249), (app.obstacleX+45-15, 249)) == True:
                    return True
                elif intersect(aLine[0], aLine[1], (app.obstacleX+45, 224.5), (app.obstacleX+45+15, 249)) == True:
                    return True
            #line intersection of third spike
            blockList = [((playerBlock.topRight),(playerBlock.topLeft)), ((playerBlock.bottomRight),(playerBlock.bottomLeft)), ((playerBlock.topRight),(playerBlock.bottomRight)), ((playerBlock.topLeft),(playerBlock.bottomLeft))]
            spikeList3 = [(app.obstacleX+90, 224.5), (app.obstacleX+90+15, 249), (app.obstacleX+90-15, 249)]
            for aLine in blockList:
                if intersect(aLine[0], aLine[1], (app.obstacleX+90, 224.5), (app.obstacleX+90+15, 249)) == True:
                    return True
                elif intersect(aLine[0], aLine[1], (app.obstacleX+90+15, 249), (app.obstacleX+90-15, 249)) == True:
                    return True
                elif intersect(aLine[0], aLine[1], (app.obstacleX+90, 224.5), (app.obstacleX+90+15, 249)) == True:
                    return True
            if rectanglesOverlap(playerBlock.leftValue, playerBlock.topValue, playerBlock.sideLength, playerBlock.sideLength, app.obstacleX - 15, 224.5, 30, 25.5):
                return True
            if rectanglesOverlap(playerBlock.leftValue, playerBlock.topValue, playerBlock.sideLength, playerBlock.sideLength, app.obstacleX + 45 - 15, 224.5, 30, 25.5):
                return True
            if rectanglesOverlap(playerBlock.leftValue, playerBlock.topValue, playerBlock.sideLength, playerBlock.sideLength, app.obstacleX + 90 - 15, 224.5, 30, 25.5):
                return True
    if app.currentObstacle1 == 'floor':
        if rectanglesOverlap(playerBlock.leftValue, playerBlock.topValue, playerBlock.sideLength, playerBlock.sideLength,app.obstacleX, app.obstacleY, 150, 50) == True and app.floorY != floor.topY:
            return True
    if app.currentObstacle1 == 'topSpike':
        if rectanglesOverlap(playerBlock.leftValue, playerBlock.topValue, playerBlock.sideLength, playerBlock.sideLength, app.obstacleX-15, topSpike.centerY - 12, 30, 25.5):
            return True
        elif rectanglesOverlap(playerBlock.leftValue, playerBlock.topValue, playerBlock.sideLength, playerBlock.sideLength, app.obstacleX-15, topSpike.centerY - 25, 100, 25):
            return True


def isValidPowerup(app, playerBlock):
    if app.currentPowerup == 'invincible':
        if distance(playerBlock.leftValue + 25, playerBlock.centerY, app.powerupX, invincible.centerY) <= invincible.width:
            app.deleteInvincible = True
            app.invincible = True
    elif app.currentPowerup == 'jetpack':
        if distance(playerBlock.leftValue + 25, playerBlock.centerY, app.powerupX, jetpack.centerY) <= jetpack.width:
            app.deleteJetpack = True
            app.jetpack = True




#extra side functions used in collisions
def distance(x1, y1, x2, y2):
    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) )
    return distance


def rectanglesOverlap(left1, top1, width1, height1,
                      left2, top2, width2, height2):
    bottom1 = top1 + height1
    bottom2 = top2 + height2
    right1 = left1 + width1 
    right2 = left2 + width2
    return (bottom1 >= top2 and bottom2 >= top1 and right1  >= left2 and right2 >= left1)


#intersection of a line (ccw and intersection)--> code/algorithm of line intersection from https://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/ 
def ccw(A,B,C):
    return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])

def intersect(A,B,C,D):
        return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
    

def main():
    runApp()

main()