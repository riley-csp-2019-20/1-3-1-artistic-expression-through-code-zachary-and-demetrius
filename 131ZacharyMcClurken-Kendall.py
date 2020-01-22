# Import turtle
import turtle as trtl

# Make the screen
wn = trtl.Screen()
wn.bgcolor("purple")


# Make a turtle that draws half the board
tic = trtl.Turtle()
tic.speed(0)
tic.color("green")
tic.pensize(2)

# Make the turtle that draws the other half
tac = trtl.Turtle()
tac.speed(0)
tac.color("green")
tac.pensize(2)

# Change turtle settings
tic.penup()
tic.goto(160, 0)
tic.pendown()
tic.setheading(90)

tac.penup()
tac.goto(80, 0)
tac.pendown()
tac.setheading(90)

tic.goto(160, 240)

tac.goto(80, 240)

tic.penup()
tic.goto(0, 80)
tic.pendown()
tic.setheading(0)

tac.penup()
tac.goto(0, 160)
tac.pendown()
tac.setheading(0)

tic.goto(240, 80)

tac.goto(240, 160)

# Make a turtle for x
cross = trtl.Turtle()

# Make a turtle for o
circle = trtl.Turtle()

# Make a variable that draws x
def drawX(x,y):
    cross.pensize(3)
    cross.ht()
    cross.penup()
    cross.goto(x,y)
    cross.pendown()
    cross.setheading(315)
    cross.forward(30)
    cross.penup()
    cross.goto(x+20,y+1.5)
    cross.pendown()
    cross.setheading(225)
    cross.forward(30)

# Make a variable that draws o
def drawO(x,y):
    circle.ht()
    circle.pensize(3)
    circle.penup()
    circle.goto(x,y)
    circle.pendown()
    circle.circle(15)


if (x > 1 and x < 80 and y > 80 and y < 240):

elif (x > 80 and x < 160 and y > 160 and < 240):

elif (x > 160 and x < 240 and y > 160 and < 240):

elif (x > 1 and x < 80 and y > 160 and < 240):

elif (x > 80 and x < 160 and y > 80 and < 160):

elif (x > 160 and x < 240 and y > 80 and < 160):

elif (x > 1 and x < 80 and y > 1 and < 80):

elif (x > 80 and x < 160 and y > 1 and < _80_):

elif (x > 160 and x < 240 and y > 1 and < 80): 
    



# Bind the right click and left click to the x and o variable.
wn.onclick(drawX, btn=1)
wn.onclick(drawO, btn=3)
wn.listen()
wn.mainloop()
