from cmu_graphics import*
import math

def onAppStart(app):
    app.width = 800
    app.height = 400
    app.titleScreen = True
    app.difficultySetting = False
    app.stepsPerSecond = 10
    app.obstacleX = 800
    app.blockX = 150
    app.blockY = 225
    app.jumping = False
    app.falling = False
    app.blockAngle = 0

def redrawAll(app):
    #title screen 
    if app.titleScreen == True:
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
    #speed/difficulty screen
    elif app.difficultySetting == True and app.titleScreen == False:
        #background color
        drawRect(0,0,800,400,fill = 'lightblue', opacity = 80)
        #different speeds
        drawRect(150, 200, 200, 100, align = 'center', fill = 'cyan', border = 'black')
        drawRect(400, 200, 200, 100, align = 'center', fill = 'cyan', border = 'black')
        drawRect(650, 200, 200, 100, align = 'center', fill = 'cyan', border = 'black')
        drawLabel('Slow', 150, 200, fill = 'lightgreen', border = 'black', font = 'orbitron', size = 45)
        drawLabel('Moderate', 400, 200, fill = 'lightgreen', border = 'black', font = 'orbitron', size = 45)
        drawLabel('Fast', 650, 200, fill = 'lightgreen', border = 'black', font = 'orbitron', size = 45)
    #play screen 
    elif app.titleScreen == False and app.difficultySetting == False:
        #background color
        drawRect(0,0,800,400,fill = 'lightblue', opacity = 80)
        #floor
        drawRect(0,250,800, 250, fill = 'blue', border = 'black', opacity = 90, borderWidth = 5)
        #obstacle
        drawRegularPolygon(app.obstacleX, 237.5, 30, 3, fill='red', border = 'black', borderWidth = 2) 
        #player block
        drawRect(app.blockX, app.blockY, 50, 50, fill = 'purple', border = 'white', align = 'center', rotateAngle = app.blockAngle)

def onKeyPress(app, key):
    #jump mechanics
    if key == 'space' and app.blockY == 225:
        app.jumping = True

def onStep(app):
    app.obstacleX -= 10
    if app.obstacleX + 50 <= 0:
        app.obstacleX = 800 #move obstacle back to the beginning
    if app.jumping == True and app.blockY >= 125:
        app.blockY -= 10
        app.blockAngle += 4.5
        if app.blockY == 125:
            app.jumping = False
            app.falling = True
    if app.falling == True and app.blockY <= 225:
        app.blockY += 10
        app.blockAngle += 4.5
        if app.blockY == 225:
            app.falling = False

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
        app.difficultySetting = False
        app.titleScreen = True
    elif app.difficultySetting == True and (mouseX >= 300 and mouseX <= 500) and (mouseY >= 150 and mouseY <= 250):
        app.stepsPerSecond = 20
        app.difficultySetting = False
        app.titleScreen = True
    elif app.difficultySetting == True and (mouseX >= 550 and mouseX <= 750) and (mouseY >= 150 and mouseY <= 250):
        app.stepsPerSecond = 30
        app.difficultySetting = False
        app.titleScreen = True
    
def distance(x1, y1, x2, y2):
    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) )
    return distance

def main():
    runApp()

main()