import turtle
tim = turtle.Turtle()
sz=100
flip = 180
right_ang = 90
origin_x= float(-0.00)
origin_y= float(320.00)
x=origin_x
y=origin_y
trap_angle=120
L=20
horiz_x = float(-100.00)
horiz_y = float(120)

tim.speed(0)

'''Creating a square with the turtle function, with a passed in variable  by the user. '''
def square(t,side):
    '''Draw one square of side length side with turtle t'''
    for x in range(4):
        t.forward(side)
        t.right(right_ang)

def cubeTab(t,sz):
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
    cubeTab(t,sz)
    t.forward(sz)
    t.right(right_ang)
    square(t,sz)
    t.forward(sz)
    t.right(right_ang)
    cubeTab(t,sz)
    #print(x,y)
    
def CAC_with_tabs(t,sz,L):
    cubeTab(t,sz)
    t.forward(sz)
    t.right(right_ang)
    for i in range(3):
        square(t,sz)
        t.forward(sz)
    t.right(right_ang)
    cubeTab(t,sz)




tim.penup()
tim.goto(origin_x,origin_y)
tim.pendown()
square(tim,sz)
cubeTab(tim,sz) #This is the topmost square and trapezoid
tim.penup()
#tim.goto(origin_x,origin_y-100)
x=origin_x
y=origin_y-200
tim.goto(x,y)
#print (x,y)

B_with_tabs(tim,sz,L)
x-=100
y-=100
tim.penup()
tim.goto(x,y)
tim.left(flip)
CAC_with_tabs(tim,sz,L)
x=-0.00
y=-80
tim.penup()
tim.goto(x,y)
tim.left(right_ang)
B_with_tabs(tim,sz,L)
tim.penup()
tim.goto(origin_x,origin_y)
tim.left(right_ang)
