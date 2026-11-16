import turtle
tim = turtle.Turtle()
sz=90
flip = 180
right_ang = 90
origin_x= -0
origin_y= 180
x=origin_x
y=origin_y
trap_angle=120
L=sz/5 # This makes the trapezoid line length scale, relative to the sz
tim.speed(0)

'''Creating a square with the turtle function, with a passed in variable  by the user. '''
def square(t,side):
    #tim.speed(0)
    t.pendown()
    '''Draw one square of side length side with turtle t'''
    for x in range(4):
        t.forward(side)
        t.right(right_ang)

def cubeTab(t,sz,L):
    #tim.speed(0)
    '''This function creates a trapezoid of length sz, in height of L.'''
    t.pendown()
    t.forward(sz)
    t.left(trap_angle)
    t.forward(L)
    t.left(60)
    t.forward(sz-(2*(L/2)))
    t.left(60)
    t.forward(L)
    t.left(trap_angle)

def B_with_tabs(t,sz,L):
    t.left(right_ang)
    cubeTab(tim,sz,L)
    t.forward(sz)
    t.right(right_ang)
    square(t,sz)
    t.forward(sz)
    t.right(right_ang)
    cubeTab(tim,sz,L)
    #print(x,y)
    
def CAC_with_tabs(t,sz,L):
    square(tim,sz)
    cubeTab(tim,sz,L)
    tim.penup()
    tim.forward(sz)
    tim.right(right_ang)
    tim.forward(sz)
    tim.pendown()
    square(tim,sz)
    tim.penup()
    tim.forward(2*sz)
    tim.right(right_ang)
    tim.pendown()
    square(tim,sz)
    cubeTab(tim,sz,L)


tim.penup()
tim.goto(origin_x,origin_y)
tim.pendown()
square(tim,sz)
cubeTab(tim,sz,L) #This is the topmost square and trapezoid
tim.penup()

x=origin_x
y=origin_y-(sz*2)
tim.goto(x,y)

B_with_tabs(tim,sz,L)
x-=sz
y-=sz
tim.penup()
tim.goto(x,y)
tim.left(flip)

CAC_with_tabs(tim,sz,L)
tim.penup()
tim.right(right_ang)
tim.forward(2*sz)

tim.left(right_ang)
tim.forward(2*sz)
tim.left(right_ang)
B_with_tabs(tim,sz,L)


