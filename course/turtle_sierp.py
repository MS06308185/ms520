import turtle

def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()

def getMid(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

always_show = False

def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', \
            'violet', 'orage']
    if degree == 0 or always_show:
        drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0], \
                getMid(points[0], points[1]), \
                getMid(points[0], points[2])], \
                degree-1, myTurtle)
        sierpinski([points[1], \
                getMid(points[1], points[0]), \
                getMid(points[1], points[2])], \
                degree-1, myTurtle)
        sierpinski([points[2], \
                getMid(points[2], points[1]), \
                getMid(points[2], points[0])], \
                degree-1, myTurtle)

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--as":
        always_show = True
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [[-200, -100], [0, 200], [200, -100]]
    sierpinski(myPoints, 4, myTurtle)
    myWin.exitonclick()
