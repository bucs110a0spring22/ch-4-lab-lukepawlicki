import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
def drawSineCurve(dart):
  '''
  Plots the sin curve
  (args): x- x values on the graph
          y- y values on the graph
  '''
  for x in range(-360,361):
    y = math.sin(math.radians(x))
    dart.goto(x,y)
def setupWindow(wn):
  '''
  Sets the background color of the screen, sets the size of the screen
  '''
  wn.bgcolor("light blue")
  wn.setworldcoordinates(-360,-1,360,1)
def setupAxis(dart):
  '''
  Creates the x and y axes of the graph
  '''
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
  '''
  Resets dart to the left hand side of the graph, then plots the cos curve
  (args): same as sin curve
  '''
  dart.up()
  dart.goto(-360,1)
  dart.down()
  for x in range(-360,361):
    y = math.cos(math.radians(x))
    dart.goto(x,y)
def drawTangentCurve(dart):
  '''
  Plots the tan curve
  (args): same as sin and cos curves
  '''
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
