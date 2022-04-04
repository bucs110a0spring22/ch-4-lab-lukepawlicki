import turtle
import math
import time
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
def drawSineCurve(myturtle=None):
  '''
  Plots the sin curve
  (args): myturtle- class, turtle that draws the sine curve
  (return): none
  '''
  for x in range(-360,361):
    y = math.sin(math.radians(x))
    myturtle.goto(x,y)
def setupWindow(window=None):
  '''
  Sets the background color of the screen, sets the size of the screen
  (args): window- class, screen that shows what the turtle is doing
  (return): none
  '''
  window.bgcolor("light blue")
  window.setworldcoordinates(-360,-1,360,1)
def setupAxis(myturtle=None):
  '''
  Creates the x and y axes of the graph
  (args): myturtle- class, turtle that draws the axes of the graph
  (return): none
  '''
  myturtle.up()
  myturtle.goto(0,1)
  myturtle.down()
  myturtle.goto(0,-1)
  myturtle.up()
  myturtle.goto(-360,0)
  myturtle.down()
  myturtle.goto(360,0)
  myturtle.up()
  myturtle.goto(-360,0)
  myturtle.down()
def drawCosineCurve(myturtle=None):
  '''
  Resets dart to the left hand side of the graph, then plots the cosine curve
  (args): myturtle- class, draws the cosine curve
  (return): none
  '''
  myturtle.up()
  myturtle.goto(-360,1)
  myturtle.down()
  for x in range(-360,361):
    y = math.cos(math.radians(x))
    myturtle.goto(x,y)
def drawTangentCurve(myturtle=None):
  '''
  Plots the tangent curve
  (args): myturtle- class, draws the tangent curve
  (return): none
  '''
  myturtle.up()
  myturtle.goto(-360,0)
  myturtle.down()
  for x in range(-360,361):
    y = math.tan(math.radians(x))
    myturtle.goto(x,y)
def title(myturtle=None,window=None, title=None):
  '''
  Add a title to the top of the graph
  Increase the world coordinates to make room for the title
  Put a box around the existing coordinate size to isolate the     graph
  (args): myturtle- class, used to write the title and surround the graph in a box
          window- class, shows the graph
          title- str, graph title that appears at the top of the screen
  (return): graph_title- str, title of the graph
  '''
  myturtle.up()
  myturtle.goto(-360,-1)
  myturtle.down()
  for i in range(2):
    myturtle.forward(720)
    myturtle.left(90)
    myturtle.forward(2)
    myturtle.left(90)
  window.setworldcoordinates(-500,-2,500,2)
  myturtle.up()
  myturtle.goto(0,1.5)
  graph_title = title
  myturtle.write(graph_title, align='center', font=('arial', 12, 'bold'))
  return graph_title
  

  
                      

  
    
  
    
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
    time.sleep(5)
    wn.clear()
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    graph_title = title(dart,wn, title='Sine and Cosine Graph')
    print('This is the',graph_title, 'with x values ranging from -360 to +360 degrees.' )
    wn.exitonclick()
main()




