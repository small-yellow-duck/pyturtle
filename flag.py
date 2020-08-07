import turtle

t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.bgcolor('grey')

def draw_rect(x_left, y_lower, width, height, colour):
  t.color(colour)
  t.up()
  t.goto(x_left, y_lower) #goto lower left corner
  t.down()
  t.begin_fill()

  t.goto(x_left+width, y_lower) #goto lower right corner
  t.goto(x_left+width, y_lower+height)#goto upper right corner
  t.goto(x_left, y_lower+height)#goto upper left corner
  t.goto(x_left, y_lower)#goto lower left corner

  t.end_fill()
  t.up


def draw_horizontal_tricolor(list_of_colours):
  #code to draw three rectangles with colours given by values in list_of_colours
  None



'''
draw flags
https://3.bp.blogspot.com/-sCTPmY04Ft0/W0ENi2S6d5I/AAAAAAAApBg/T-c6c4j8AvAB3iKm5oMfdsk6LYnoI5TuQCLcBGAs/s1600/all_country_flags_with_names.jpg
'''

#draw_rect(x_left, y_lower, width, height, colour)

#Ukraine
draw_rect(-150, 0, 300, 100, 'blue')
draw_rect(-150, -100, 300, 100, 'yellow')