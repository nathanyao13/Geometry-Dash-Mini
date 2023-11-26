from cmu_graphics import*

def onAppStart(app):
    app.width = 800
    app.length = 1000
    app.titlescreen = False 
    app.stepsPerSecond = 5
    app.squareX = app.width

def redrawAll(app):
    if app.titlescreen == True:
        drawLabel('Geometry Dash Mini', 400, 50, size=50, font='orbitron', bold=True, fill='lightgreen', border= 'black', borderWidth=2,opacity=100)
        #drawing for the title screen
    else:
        drawRect(app.squareX, 200, 50, 50, fill='red') 
        drawRect(0,250,800, 250, fill = 'blue', border = 'black', opacity = 90)

def onKeyPress(app, key):
    # this is for the player to choose the difficulty/speed of the round
    if key == 'f':
        app.speed = 'fast'
        app.stepsPerSecond = 50
    elif key == 'm':
        app.speed = 'moderate'
        app.stepsPerSecond = 30
    elif key == 's':
        app.speed = 'slow'
        app.stepsPerSecond = 2

def onStep(app):
    app.squareX -= 10
    if app.squareX + 50 <= 0:
        app.squareX = app.width #move obstacle back to the beginning

def main():
    runApp()

main()