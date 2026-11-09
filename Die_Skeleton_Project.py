import turtle
tim = turtle.Turtle()
sz=100
flip = 180
right_ang = 90
x= float(0.00)
y= float(320.00)
#trap_angle=120
l=20
horiz_x = float(-100.00)
horiz_y = float(120)

tim.speed(0)

'''Creating a square with the turtle function, with a passed in variable  by the user. '''
def square(t,side):
    '''Draw one square of side length side with turtle t'''
    for x in range(4):
        #t.speed(0)
        t.forward(side)
        t.right(90)

def turtleTrapezoid(t,sz):
    t.pendown()
    t.forward(sz)
    t.left(120)
    t.forward(l)
    t.left(60)
    t.forward(sz-(2*(l/2)))
    t.left(60)
    t.forward(l)
    t.left(120)
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


for i in range(4):
    #tim.speed(0)
    tim.penup()
    tim.goto(-x,y)
    #print (tim.pos())
    tim.pendown()
    square(tim,sz)
    y -= 100

y += 400
tim.goto(-x,y)
turtleTrapezoid(tim,sz)
tim.goto(-0.00,120.00)
tim.left(right_ang)
turtleTrapezoid(tim,sz)
tim.penup()
tim.goto(100.00,220.00)
tim.right(flip)
tim.pendown()
turtleTrapezoid(tim,sz)
tim.penup()
tim.goto(horiz_x,horiz_y)
tim.left(right_ang)

for i in range(3):
    tim.pendown()
    square(tim,sz)
    horiz_x+= 100
    tim.goto(horiz_x,horiz_y)
    tim.penup()
tim.right(right_ang)
turtleTrapezoid(tim,sz)
#print(tim.pos())
tim.penup()
horiz_x-=100
horiz_y-=100
tim.goto(horiz_x,horiz_y)
tim.pendown()
turtleTrapezoid(tim,sz)
tim.penup()
horiz_x-=100
horiz_y-=100
tim.left(flip)
tim.goto(horiz_x,horiz_y)
tim.pendown()
turtleTrapezoid(tim,sz)
tim.penup()
horiz_x-=100
horiz_y+=100
tim.goto(horiz_x,horiz_y)
tim.pendown()
turtleTrapezoid(tim,sz)
    
#     tim.goto(-x,y)
#     print (tim.pos())
#     tim.pendown()
#     square(tim,sz)
#     y = y-100

#     tim.penup()
#     tim.goto(-x,y-200)
#print (tim.pos())