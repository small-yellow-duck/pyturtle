import turtle

'''
draw_diamond 
#TODO: draw a diamond centred at coords
(x_centre, y_centre), then return the turtle to
the coords where the turtle started out (currentx, currenty) 
'''
def drawdiamond(x_centre, y_centre, size):
  #keep track of the initial position
  initial_x, initial_y = t.position()
  initial_heading = t.heading()

  t.up() # pick the pen up (stop drawing)
  t.goto(x_centre, y_centre)
  t.down() # put the pen down (start drawing)

  #your code goes here!

  #go back to the initial position!
  t.up() # pick the pen up (stop drawing)
  t.goto(initial_x, initial_y)
  t.down()




t = turtle.Turtle()

print('heading: ', t.heading(), '(x,y): ', t.pos())
t.forward(75)
t.right(90)
print('heading: ', t.heading(), '(x,y): ', t.pos())

#draw a diamond with the centre at (20, 80)
drawdiamond(20, 80, 40)