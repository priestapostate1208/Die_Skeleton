import turtle
tim = turtle.Turtle()
sz=100
flip = 180
right_ang = 90
origin_x= -0
origin_y= 200
x=origin_x #this is to start off with testing, without altering the origin_x/y values
y=origin_y #this is to start off with testing, without altering the origin_x/y values
checkerboard_x=0 #this is for the checkerboard function. 
checkerboard_y=0 #this is for the checkerboard function. 
trap_angle=120
L=sz/5 # This makes the trapezoid line length scale, relative to the sz
n=5
tim.speed(0)

'''Creating a square with the turtle function, with a passed in variable  by the user. '''
def square(t,side):
    t.pendown()
    '''Draw one square of side length side with turtle t - then goes back to point of origin.'''
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
    '''This creates the "B" box, with tabs on either side.'''
    t.left(right_ang)
    cubeTab(tim,sz,L)
    t.forward(sz)
    t.right(right_ang)
    square(t,sz)
    t.forward(sz)
    t.right(right_ang)
    cubeTab(tim,sz,L)
    #print(x,y)
    
def C_A_C_with_tabs(t,sz,L):
    '''This creates the "C" boxes, with an "A" box in between.'''
    t.fillcolor("yellow")
    t.begin_fill()
    t.end_fill()
    square(tim,sz)
    cubeTab(tim,sz,L)
    tim.penup()
    tim.forward(sz)
    tim.right(right_ang)
    tim.forward(sz)
    tim.pendown()
    square(tim,sz)
    checkerboard(tim,sz,n)
    tim.penup()
    tim.forward(2*sz)
    tim.right(right_ang)
    tim.pendown()
    square(tim,sz)
    cubeTab(tim,sz,L)

def checkerboard(t,sz,n):
    '''Checkerboard function, that colors in a 5x5 box set.'''
    x,y = t.pos()
    '''The x and y coordinates will be oriented off of the box's point of origin.''' 
    checkerboard_x,checkerboard_y = t.pos()
    '''These variables are to keep track of the checkerboard box's point of origin.'''
    for i in range(1,n+1):
        for j in range(1,n+1):

            if (i+j)%2==0:
                t.fillcolor("yellow")
                
            else:
                t.fillcolor("blue")
            t.begin_fill()
            square(t,sz/n)
            t.end_fill()
            t.forward(sz/n) # This moves the turtle forward to draw another square. 

        t.penup()
        t.goto(x,(y-sz/n))
        y=y-sz/n
        t.pendown()
        t.fillcolor("black")
    t.goto(checkerboard_x,checkerboard_y) #Go back to origin.

tim.penup()
tim.goto(origin_x,origin_y)
tim.pendown()
square(tim,sz)
cubeTab(tim,sz,L) #This is the topmost square and trapezoid
checkerboard(tim,sz,n)
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

C_A_C_with_tabs(tim,sz,L)
tim.penup()
tim.right(right_ang)
tim.forward(2*sz)

tim.left(right_ang)
tim.forward(2*sz)
tim.left(right_ang)
B_with_tabs(tim,sz,L)


