import turtle

t = turtle.Turtle()


def drawpizzaslice(radius, n_slices, slice_colour):
    t.color(slice_colour)
    t.begin_fill()
    t.forward(radius)
    t.left(90)
    t.circle(radius, 360 / n_slices)
    t.left(90)
    t.forward(radius)
    t.end_fill()
    t.left(180)


for colour in ['red', 'blue', 'green', 'purple']:
    drawpizzaslice(100, 8, colour)
