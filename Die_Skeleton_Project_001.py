import turtle
tim = turtle.Turtle()
#sz=120
side_length=120
origin_x= -0
origin_y= 200
#x=origin_x #this is to start off with testing, without altering the origin_x/y values
#y=origin_y #this is to start off with testing, without altering the origin_x/y values
#L=sz/5 # This makes the trapezoid line length scale, relative to the sz
trap_length=side_length/5
checkerboard_rows_and_columns=5
#tim.speed(0)

'''Creating a square with the turtle function, with a passed in variable  by the user. '''
def square(t,side):
    t.pendown()
    '''Draw one square of side length side with turtle t - then goes back to point of origin.'''
    for i in range(4):
        t.forward(side)
        t.right(90)

def cubeTab(t,sz,L):
    '''This function creates a trapezoid of length sz, in height of L.'''
    t.pendown()
    t.forward(sz)
    t.left(120)
    t.forward(L)
    t.left(60)
    t.forward(sz-(2*(L/2)))
    t.left(60)
    t.forward(L)
    t.left(120)

def B_square_decoration(t,sz):
    for m in range(3):
        for k in range(4):
            square(t,sz/4)
            t.forward(sz/4)
        t.right(90)
        
def B_with_tabs(t,sz,L):
    '''This creates the "B" box, with tabs on either side.'''
    t.left(90)
    cubeTab(t,sz,L)
    t.forward(sz)
    t.right(90)
    square(t,sz)
    t.forward(sz)
    t.right(90)
    cubeTab(t,sz,L)
    #B_square_decoration(t,sz/4)
    #print(x,y)


    
def C_A_C_with_tabs(t,sz,L):
    '''This creates the "C" boxes, with an "A" box in between.'''
    t.fillcolor("yellow")
    t.begin_fill()
    t.end_fill()
    square(t,sz)
    cubeTab(t,sz,L)
    t.penup()
    t.forward(sz)
    t.right(90)
    t.forward(sz)
    t.pendown()
    square(t,sz)
    checkerboard(t,sz,checkerboard_rows_and_columns)
    t.penup()
    t.forward(2*sz)
    t.right(90)
    t.pendown()
    square(t,sz)
    cubeTab(t,sz,L)

def checkerboard(t,sz,n):
    '''Checkerboard function, that colors in a 5x5 box set.'''
    x, y = t.pos()
#     print (type(t.pos))
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
        t.fillcolor("")
    t.goto(checkerboard_x,checkerboard_y) #Go back to origin.

tim.penup()
tim.goto(origin_x,origin_y)
tim.pendown()
#square(tim,sz)
square(tim,side_length)
cubeTab(tim,side_length,trap_length) #This is the topmost square and trapezoid
#cubeTab(tim,side_length,trap_length)
checkerboard(tim,side_length,checkerboard_rows_and_columns)
tim.penup()

x=origin_x
#y=origin_y-(sz*2)
y=origin_y
y-=(side_length*2)
tim.goto(x,y)

B_with_tabs(tim,side_length,trap_length)
x-=side_length
y-=side_length
tim.penup()
tim.goto(x,y)
tim.left(180)

C_A_C_with_tabs(tim,side_length,trap_length)
tim.penup()
tim.right(90)
tim.forward(2*side_length)

tim.left(90)
tim.forward(2*side_length)
tim.left(90)
B_with_tabs(tim,side_length,trap_length)
# tim.penup()
# tim.goto(origin_x,origin_y)
# tim.left(90)
tim.exitonclick()