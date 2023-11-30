import math
class block:
    def __init__(self, color, centerX, centerY, sideLength, angle, upVelocity):
        self.color = color
        self.centerX = centerX
        self.centerY = centerY
        self.sideLength = sideLength
        self.angle = angle
        self.upVelocity = upVelocity
        self.rightValue = self.centerX + (self.sideLength/2)
        self.leftValue = self.centerX - (self.sideLength/2)
        self.topValue = self.centerY - (self.sideLength/2)
        self.bottomValue = self.centerY + (self.sideLength/2)
        self.topRight = (self.rightValue, self.topValue)
        self.topLeft = (self.leftValue, self.topValue)
        self.bottomRight = (self.rightValue, self.bottomValue)
        self.bottomLeft = (self.leftValue, self.bottomValue)










