import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
def drawSineCurve(dart):
  for x in range(-360,361):
    y = math.sin(math.radians(x))
    dart.goto(x,y)
def setupWindow(wn):
  wn.bgcolor("light blue")
  wn.setworldcoordinates(-360,-1,360,1)
def setupAxis(dart):
  dart.up()
  dart.goto(0,10)
  dart.down()
  dart.goto(0,-10)
  dart.up()
  dart.goto(-500,0)
  dart.down()
  dart.goto(500,0)
  dart.up
  dart.goto(-360,0)
  dart.down
def drawCosineCurve(dart):
  dart.up()
  dart.goto(-360,1)
  dart.down()
  for x in range(-360,361):
    y = math.cos(math.radians(x))
    dart.goto(x,y)
def drawTangentCurve(dart):
  dart.up()
  dart.goto(-360,0)
  dart.down()
  for x in range(-360,361):
    y = math.tan(math.radians(x))
    dart.goto(x,y)
    














##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)
    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
  
    wn.exitonclick()

   
main()
