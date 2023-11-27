from cmu_graphics import*
import math
import random

#seperate into class file
class block:
    def __init__(self, color, centerX, centerY, sideLength, angle):
        self.color = color
        self.centerX = centerX
        self.centerY = centerY
        self.sideLength = sideLength
        self.angle = angle

playerBlock =  block('purple', 150, 225, 50, 0)

#seperate into class file
class obstacle:
    def __init__(self, shape, centerX, centerY):
        self.shape = shape
        self.centerX = centerX
        self.centerY = centerY






def onAppStart(app):
    app.width = 800
    app.height = 400
    app.titleScreen = True
    app.difficultySetting = False
    app.stepsPerSecond = 30
    app.obstacleX = 800
    app.jumping = False
    app.falling = False
    app.blockAngle = 0
    app.obstancles = set()
    app.backgroundX = 0
    app.trail = True
    app.MapSpeed = 0




def redrawAll(app):
    #title screen 
    if app.titleScreen == True:
        drawTitleScreen(app)
    #speed/difficulty screen
    elif app.difficultySetting == True and app.titleScreen == False:
        drawDifficultyScreen(app)
    #play screen 
    elif app.titleScreen == False and app.difficultySetting == False:
        drawPlayScreen(app)



def drawDifficultyScreen(app):
    #background color
    drawRect(0,0,800,400,fill = 'lightblue', opacity = 80)
    #different speeds
    drawRect(150, 200, 200, 100, align = 'center', fill = 'cyan', border = 'black')
    drawRect(400, 200, 200, 100, align = 'center', fill = 'cyan', border = 'black')
    drawRect(650, 200, 200, 100, align = 'center', fill = 'cyan', border = 'black')
    drawLabel('Slow', 150, 200, fill = 'lightgreen', border = 'black', font = 'orbitron', size = 45)
    drawLabel('Moderate', 400, 200, fill = 'lightgreen', border = 'black', font = 'orbitron', size = 45)
    drawLabel('Fast', 650, 200, fill = 'lightgreen', border = 'black', font = 'orbitron', size = 45)

def drawTitleScreen(app):
    #background color
    drawRect(0,0,800,400,fill = 'lightblue', opacity = 80)
    #drawing for the title screen
    drawLabel('Geometry Dash Mini', 400, 50, size=50, font='orbitron', bold=True, fill='lightgreen', border= 'black', borderWidth=2,opacity=100)
    #play button
    drawRect(400, 200, 100, 100, fill='cyan', align = 'center', border = 'black')
    drawRegularPolygon(395,200, 50, 3, fill = 'yellow', border = 'black', rotateAngle = 90, align = 'center')
    #speed/difficulty setting
    drawRect(400, 325, 200, 100, fill = 'cyan', align = 'center', border = 'black')
    drawLabel('Select Difficulty', 400, 325, fill = 'lightgreen', font = 'orbitron', size = 27.5, border = 'black')


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
    drawRect(0,250,800, 250, fill = 'blue', border = 'black', opacity = 90, borderWidth = 5)
    #obstacle
    drawRegularPolygon(app.obstacleX, 237.5, 30, 3, fill='red', border = 'black', borderWidth = 2) 
    #player block
    drawRect(playerBlock.centerX, playerBlock.centerY, playerBlock.sideLength, playerBlock.sideLength, fill = 'purple', border = 'white', align = 'center', rotateAngle = playerBlock.angle)
    drawRect(playerBlock.centerX, playerBlock.centerY, playerBlock.sideLength-10, playerBlock.sideLength-10, fill = 'blue', border = 'white', align = 'center', rotateAngle = playerBlock.angle)
    drawRect(playerBlock.centerX, playerBlock.centerY, playerBlock.sideLength-20, playerBlock.sideLength-20, fill = 'purple', border = 'white', align = 'center', rotateAngle = playerBlock.angle)
    drawRect(playerBlock.centerX, playerBlock.centerY, playerBlock.sideLength-30, playerBlock.sideLength-30, fill = 'black', border = 'white', align = 'center', rotateAngle = playerBlock.angle)
    #player block trail
    if app.trail == True:
        for i in range(playerBlock.centerX - 75, playerBlock.centerX-25, 5):
            drawCircle(i, playerBlock.centerY + random.randrange(0,15), 2, fill = 'purple')
            drawCircle(i-5, playerBlock.centerY + random.randrange(0,15), 2, fill = 'white')
            drawCircle(i-10, playerBlock.centerY + random.randrange(0,15), 2, fill = 'blue')



def onKeyPress(app, key):
    #jump mechanics
    if key == 'space' and playerBlock.centerY == 225:
        app.jumping = True




def onStep(app):
    app.obstacleX -= 10
    if app.obstacleX + 50 <= 0:
        app.obstacleX = 800 #move obstacle back to the beginning
    app.backgroundX -= 2 
    if app.backgroundX <= 0:
        app.backgroundX = 800
    if app.jumping == True and playerBlock.centerY >= 125:
        playerBlock.centerY -= 10
        playerBlock.angle += 4.5
        app.trail = False
        if playerBlock.centerY == 125:
            app.jumping = False
            app.falling = True
    if app.falling == True and playerBlock.centerY <= 225:
        playerBlock.centerY += 10
        playerBlock.angle += 4.5
        if playerBlock.centerY == 225:
            app.falling = False
            app.trail = True




def onMousePress(app, mouseX, mouseY):
    #title screen options
    if app.titleScreen == True and (mouseX >= 350 and mouseX <= 450) and (mouseY >= 150 and mouseY <= 250):
        app.titleScreen = False
    elif app.titleScreen == True and (mouseX >=200 and mouseX <= 600) and (mouseY >= 225 and mouseY <= 425):
        app.titleScreen = False
        app.difficultySetting = True
    #difficulty options
    if app.difficultySetting == True and (mouseX >= 50 and mouseX <= 250) and (mouseY >= 150 and mouseY <= 250):
        app.stepsPerSecond = 10
        app.MapSpeed = -20
        app.difficultySetting = False
        app.titleScreen = True
    elif app.difficultySetting == True and (mouseX >= 300 and mouseX <= 500) and (mouseY >= 150 and mouseY <= 250):
        app.stepsPerSecond = 20
        app.difficultySetting = False
        app.titleScreen = True
        app.MapSpeed = 0
    elif app.difficultySetting == True and (mouseX >= 550 and mouseX <= 750) and (mouseY >= 150 and mouseY <= 250):
        app.stepsPerSecond = 30
        app.difficultySetting = False
        app.titleScreen = True
        app.MapSpeed = 20
    



def distance(x1, y1, x2, y2):
    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) )
    return distance


#def isValid(app, playerBlock, obstacle):
    

def main():
    runApp()

main()