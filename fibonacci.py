import turtle

t = turtle.Turtle()
t.speed(0) #make the turtle go fast


def square(r):
    for i in range(4):
        t.left(90)
        t.forward(r)

draw_square = False
draw_circle = False

r = 1
r_next = 1

for i in range(12):
    print(r, r_next, 1.0 * r / r_next)

    if draw_circle == True:
        arc_angle = 90
        t.circle(r, arc_angle)
    else:
        t.forward(r)
        t.left(90)
        t.forward(r)

    if draw_square == True:
        square(r)

    #one way to calculate the next two values in the series
    r_old = r
    r = r_next
    r_next = r_next + r_old

    #efficient way to calculate the next two values in the series
    # r, r_next = r_next, r_next+r