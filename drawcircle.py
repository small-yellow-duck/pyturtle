import turtle

'''
Can you use the drawcircle command to draw a suprised face? :-o
Can you modify the drawcircle command to draw a rainbow?
'''

t = turtle.Turtle()


def drawcircle(x_centre, y_centre, r, colour):
    currentx, currenty = t.position()
    t.up()
    t.goto(x_centre, y_centre - r)
    t.setheading(0)
    t.down()
    t.color(colour)
    t.begin_fill()
    t.circle(r, 360)
    t.end_fill()
    t.up()
    t.goto(currentx, currenty)
    t.down()


drawcircle(0, 0, 60, 'black')
