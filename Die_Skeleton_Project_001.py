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
l=20
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
        #x+=100
        t.forward(sz)
    t.right(right_ang)
    cubeTab(t,sz)


#     tim.penup()
#     tim.goto(x,y)
#     tim.right(flip)
#     cubeTab(tim,sz)
#     tim.forward(sz)
#     tim.right(right_ang)
#     for i in range(3):
#         square(tim,sz)
#         x+=100
#********************************
# x-=100
# y-=100
# tim.penup()
# tim.goto(x,y)
# tim.right(flip)
# cubeTab(tim,sz)
# tim.forward(sz)
# tim.right(right_ang)
# for i in range(3):
#     square(tim,sz)
#     tim.forward(100)

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



# print(x,y)
# 
# print (x,y)


# x=-100
# y=20
# tim.penup()
# tim.goto(x,y)
# tim.left(right_ang*2)
# tim.pendown()
# square(tim,sz)
# #tim.right(flip)
# tim.pendown()
# cubeTab(tim,sz)
# tim.forward(sz)
# tim.right(right_ang)


#def
#t.penup()
    #t.hideturtle()
# 
# tim.penup()
# tim.goto(-(x),y)
# tim.pendown()
# square(tim,sz)
# turtleTrapezoid(tim,sz)
# tim.penup()
# tim.goto(-x,y-200)
#**************************************
#tim.left(90)
#tim.pendown()
#turtleTrapezoid(tim,sz)
#print (tim.pos())
#tim.goto(-0.00,-0.00)
#tim.goto(-0.00,150.00)

# 
# for i in range(4):
#     #tim.speed(0)
#     tim.penup()
#     tim.goto(-x,y)
#     #print (tim.pos())
#     tim.pendown()
#     square(tim,sz)
#     y -= 100
# 
# y += 400
# tim.goto(-x,y)
# turtleTrapezoid(tim,sz)
# tim.goto(-0.00,120.00)
# tim.left(right_ang)
# turtleTrapezoid(tim,sz)
# tim.penup()
# tim.goto(100.00,220.00)
# tim.right(flip)
# tim.pendown()
# turtleTrapezoid(tim,sz)
# tim.penup()
# tim.goto(horiz_x,horiz_y)
# tim.left(right_ang)
# 
# for i in range(3):
#     tim.pendown()
#     square(tim,sz)
#     horiz_x+= 100
#     tim.goto(horiz_x,horiz_y)
#     tim.penup()
# tim.right(right_ang)
# turtleTrapezoid(tim,sz)
# #print(tim.pos())
# tim.penup()
# horiz_x-=100
# horiz_y-=100
# tim.goto(horiz_x,horiz_y)
# tim.pendown()
# turtleTrapezoid(tim,sz)
# tim.penup()
# horiz_x-=100
# horiz_y-=100
# tim.left(flip)
# tim.goto(horiz_x,horiz_y)
# tim.pendown()
# turtleTrapezoid(tim,sz)
# tim.penup()
# horiz_x-=100
# horiz_y+=100
# tim.goto(horiz_x,horiz_y)
# tim.pendown()
# turtleTrapezoid(tim,sz)
#     
# #     tim.goto(-x,y)
# #     print (tim.pos())
# #     tim.pendown()
# #     square(tim,sz)
# #     y = y-100
# 
# #     tim.penup()
# #     tim.goto(-x,y-200)
# #print (tim.pos())
# 